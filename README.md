🧠 Face Recognition–Based Attendance System

📌 Project Overview

This project is a real-time Face Recognition–Based Attendance System that automatically marks Punch-In and Punch-Out using a live webcam feed. The system identifies registered users by comparing their face with stored reference images and logs attendance records with timestamps.

A lightweight Streamlit user interface is added as a presentation layer to improve usability, while the core face recognition and attendance logic remains independent and can run without the UI.

🎯 Objectives

Register users using facial images

Identify users via real-time webcam input

Automatically mark attendance without manual input

Implement realistic Punch-In / Punch-Out toggle logic

Display attendance records through a simple UI

🛠️ Technologies Used

Python 3.11

OpenCV – webcam access and image processing

DeepFace – face recognition and verification

TensorFlow / Keras – deep learning backend

Pandas – attendance data handling

Streamlit – user interface (optional enhancement)

CSV file – attendance storage

📁 Project Structure
FaceAttendanceSystem/
│
├── dataset/               # Registered face images
│   ├── Kiran.jpg
│   ├── Prince.jpg
│
├── attendance.csv         # Attendance records
├── last_action.txt        # Last Punch-In / Punch-Out message (UI support)
├── register_face.py       # Face registration script
├── recognize_face.py      # Face recognition & attendance logic
├── app.py                 # Streamlit UI
└── README.md              # Project documentation

⚙️ How the System Works
1️⃣ Face Registration

A user’s face is captured using a webcam.

The captured image is saved in the dataset/ folder.

The image filename represents the user’s identity.

2️⃣ Face Recognition

Live webcam frames are continuously captured.

The system compares the live face with all registered faces.

The best match is selected using cosine distance.

A confidence threshold is applied to reduce false matches.

3️⃣ Attendance Logic

If a user appears for the first time, attendance is marked as Punch-In.

For every subsequent appearance:

If the last entry was Punch-In, the next is Punch-Out.

If the last entry was Punch-Out, the next is Punch-In.

Attendance is stored with Name, Date, Time, and Type.

4️⃣ Streamlit User Interface (Optional Enhancement)

The Streamlit UI acts only as a presentation layer and does not alter the core logic.

Features provided by Streamlit:

Button to start the camera

Display Punch-In / Punch-Out status messages

Show attendance records in a table

Display the latest attendance entry first for better visibility

Attendance data continues to be stored in chronological order in the CSV file to maintain data integrity.

🧾 Attendance Record Format
Name,Date,Time,Type
Kiran,2026-01-31,13:41:54,Punch-In
Kiran,2026-01-31,18:05:12,Punch-Out
Prince,2026-01-31,13:52:08,Punch-In

🔐 Spoof Prevention (Basic Level)

This project implements basic spoof prevention, suitable for internship-level systems:

Uses real-time webcam input, not static uploads

Processes continuous video frames

Applies a confidence threshold to reduce false positives

Rejects unknown faces

Advanced spoof prevention methods such as blink detection or depth-based liveness checks are not implemented and are considered future enhancements.

⚠️ Limitations

The system may accept photo-based attempts displayed on mobile screens.

Accuracy may reduce under:

Poor lighting

Significant appearance changes (beard, glasses)

Camera quality issues

Designed for small-scale usage, not enterprise deployment.

These limitations are acknowledged as part of responsible system design.

🚀 Future Enhancements

Eye-blink or head-movement detection for liveness

Database storage instead of CSV

Web or mobile front-end

Face embedding caching for faster recognition

Role-based access and admin dashboard

▶️ How to Run the Project
Run Core Logic Only (Without UI)
python recognize_face.py

Run with Streamlit UI
streamlit run app.py

🏁 Conclusion

This project demonstrates a practical application of face recognition using Python and deep learning. It automates attendance marking with realistic Punch-In / Punch-Out logic and includes a simple UI for demonstration purposes while clearly documenting system limitations and future scope.

The system is suitable for internship assessments, academic projects, and AI/ML demonstrations.

👤 Author
Kiran Rathod