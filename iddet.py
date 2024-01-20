import cv2
import numpy as np

def preprocess_image(image):
    resized_image = cv2.resize(image, (100, 100))
    return resized_image

def quantize_colors(image, k=3):
    reshaped_image = image.reshape((-1, 3))
    reshaped_image = np.float32(reshaped_image)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(reshaped_image, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    centers = np.uint8(centers)
    quantized_image = centers[labels.flatten()]

    return quantized_image.reshape(image.shape)

def identify_colors(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

    # Define color ranges for detection (in HSV and YCbCr)
    color_ranges = {
        'red': {'hsv': {'lower': np.array([0, 100, 100]), 'upper': np.array([10, 255, 255])},
                'ycbcr': {'lower': np.array([0, 133, 77]), 'upper': np.array([255, 173, 127])}},
        'yellow': {'hsv': {'lower': np.array([20, 100, 100]), 'upper': np.array([40, 255, 255])},
                   'ycbcr': {'lower': np.array([0, 100, 0]), 'upper': np.array([255, 128, 127])}},
        'pink': {'hsv': {'lower': np.array([100, 50, 50]), 'upper': np.array([140, 255, 255])},
                 'ycbcr': {'lower': np.array([0, 128, 128]), 'upper': np.array([255, 173, 173])}},
    }

    # Initialize an empty dictionary to store color areas
    color_areas = {}

    # Detect colors within the defined ranges for both HSV and YCbCr
    for color, color_range in color_ranges.items():
        hsv_mask = cv2.inRange(hsv_image, color_range['hsv']['lower'] - 10, color_range['hsv']['upper'] + 10)
        ycbcr_mask = cv2.inRange(ycbcr_image, color_range['ycbcr']['lower'] - 10, color_range['ycbcr']['upper'] + 10)
        color_areas[color] = np.sum(np.logical_or(hsv_mask == 255, ycbcr_mask == 255))
    # Identify the dominant color based on the area
    dominant_color = max(color_areas, key=color_areas.get)

    # Return the dominant color and features from HSV color space
    return dominant_color, hsv_image.flatten()

def combine_features(hsv_features, ycbcr_features):
    return np.concatenate((hsv_features, ycbcr_features), axis=-1)

def extract_ycbcr_features(image):
    ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    ycbcr_features = ycbcr_image.flatten()
    return ycbcr_features

if __name__ == "__main__":
    # Load and preprocess the three images
    image_paths = [
        "C:\\Users\\akalyasri\\OneDrive\\Documents\\GitHub\\ID\\image.bascis2\\4thid.jpeg",
        "C:\\Users\\akalyasri\\OneDrive\\Documents\\GitHub\\ID\\image.bascis2\\3thid.jpeg",
        "C:\\Users\\akalyasri\\OneDrive\\Documents\\GitHub\\ID\\image.bascis2\\2ndid.jpeg",
    ]

    images = [cv2.imread(path) for path in image_paths]
    preprocessed_images = [preprocess_image(img) for img in images]

    # Perform color quantization on preprocessed images
    quantized_images = [quantize_colors(img) for img in preprocessed_images]

    # Open the webcam (0 corresponds to the default webcam)
    video_capture = cv2.VideoCapture(0)
    
    # Define the color to year mapping
    color_year_mapping = {
        'red': 'Year 2',
        'yellow': 'Year 3',
        'pink': 'Year 4',
        # Add more mappings as needed
    }

    while True:
        # Capture each frame from the video stream
        ret, frame = video_capture.read()
        if not ret:
            break

        # Resize the frame for consistency
        frame = cv2.resize(frame, (640, 480))

        # Perform color quantization on the current frame
        quantized_frame = quantize_colors(frame)
        
        # Identify colors in the quantized frame
        detected_color, hsv_features = identify_colors(quantized_frame)

        # Extract YCbCr features (replace this with the actual code to obtain YCbCr features)
        ycbcr_features = extract_ycbcr_features(frame)

        # Combine features from HSV and YCbCr
        combined_features = combine_features(hsv_features, ycbcr_features)

        # Map detected color to year
        detected_year = color_year_mapping.get(detected_color, 'Unknown Year')
        
        # Display the resulting frame with the identified year
        cv2.putText(frame, f"Detected Year: {detected_year}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        print(f"Detected Color: {detected_color}")
        print(f"HSV Values: {hsv_features}")


        # Now you can use combined_features as needed

        cv2.imshow('Video', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    video_capture.release()
    cv2.destroyAllWindows()
