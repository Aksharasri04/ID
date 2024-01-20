# 🌈 Chromocard - Smart College Student Care System

Chromocard is an advanced student care system designed to enhance the management of student who are still in the canteen during their designated break times. Leveraging state-of-the-art ID card detection and face recognition technologies, Chromocard automates the process of monitoring students, identifying late arrivals, and ensuring adherence to break schedules.

## Introduction

Chromocard addresses this challenge by integrating multiple technologies to create a comprehensive student care system. The project aims to streamline the identification of late arrivals, monitor break schedules, and alert the student care team in real-time.

## Features

### 1. ID Card Detection 🎨

Chromocard employs color-based ID card detection using the HSV (Hue, Saturation, Value) and YCbCr models. By analyzing the color tags on ID cards, the system identifies the student's academic year and break schedule. This information is crucial for tracking attendance and ensuring students are in the right place at the right time.

### 2. Face Detection and Recognition 👤

The heart of Chromocard lies in its ability to recognize faces using the Face Recognition library and OpenCV. When a late arrival is detected, the system captures the student's photo and extracts relevant information. This data, including the student's name, roll number, and department, is then communicated to the student care team for appropriate action.

### 3. Twilio Alert System 🚨

Chromocard integrates Twilio to provide a robust alert system. In the event of a late arrival or a student still being in the canteen after break time, the system sends real-time alert messages to the designated student care team. These messages contain comprehensive details, enabling the team to respond promptly.

### 4. Database Integration 📊

All student information, including photos, names, roll numbers, and departments, is stored in an SQLite database. This database serves as a central repository for historical data, enabling administrators to analyze trends and make informed decisions regarding student behavior and attendance.

## Technologies Used

- **Python:** The core programming language for implementing the project's logic.
- **OpenCV:** Utilized for computer vision tasks, such as ID card color detection and face recognition.
- **Face Recognition Library:** A powerful library for face recognition tasks.
- **Twilio:** Integrated for the real-time alert system via SMS.
- **SQLite:** The chosen database management system for storing and retrieving student information.

## Output Screenshots

### ID Card Detection

<img align="center" alt="coding" width="500" src="https://github.com/Aksharasri04/ID/blob/main/Output%20Screenshots/1.jpg">

### Message Alerting Notification

<img align="center" alt="coding" breadth="300" width="500" src="https://github.com/Aksharasri04/ID/blob/main/Output%20Screenshots/2.jpg">
