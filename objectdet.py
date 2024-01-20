
import face_recognition
import cv2

def load_known_faces(image_paths, names, roll_numbers, depts):
    known_face_encodings = []
    known_names = []
    known_roll_numbers = []
    known_depts = []

    for image_path, name, roll_number, dept in zip(image_paths, names, roll_numbers, depts):
        image = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(image)
        known_face_encodings.extend(face_encodings)
        known_names.extend([name] * len(face_encodings))
        known_roll_numbers.extend([roll_number] * len(face_encodings))
        known_depts.extend([dept] * len(face_encodings))

    return known_face_encodings, known_names, known_roll_numbers, known_depts

def recognize_faces(video_capture, known_face_encodings, known_names, known_roll_numbers, known_depts):
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        face_locations = face_recognition.face_locations(frame)

        for face_location in face_locations:
            top, right, bottom, left = face_location

            face_encoding = face_recognition.face_encodings(frame, [face_location])[0]
            name = "Unknown"
            roll_number = "Unknown"
            dept = "Unknown"

            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
            

            if True in matches:
                first_match_index = matches.index(True)
                name = known_names[first_match_index]
                roll_number = known_roll_numbers[first_match_index]
                dept = known_depts[first_match_index]

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

            print("Recognized Name:", name)
            print("Roll Number:", roll_number)
            print("Department:", dept)

            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break 

    video_capture.release()
    cv2.destroyAllWindows()

person_image_paths = [
    "image.basics/ak.jpeg",
    "image.basics/daddy.jpg", 
    "image.basics/dur.jpg",
    "image.basics/ragavi.jpeg"    
]
person_names = [
    "AKSHARA",
    "SHIVARAJ",
    "DHARSHINI",
    "RAGAVI"]
person_roll_numbers = [
    "201501005",
    "201501049",
    "201501010",
    "201501039"]
person_depts = [
    "AIML",
    "AIML",
    "AIML",
    "AIML"
]

known_face_encodings, known_names, known_roll_numbers, known_depts = load_known_faces(
    person_image_paths, person_names, person_roll_numbers, person_depts)

video_capture = cv2.VideoCapture(0)

recognize_faces(video_capture, known_face_encodings, known_names, known_roll_numbers, known_depts)
