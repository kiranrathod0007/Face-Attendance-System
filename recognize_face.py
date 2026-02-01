#.\venv\Scripts\Activate.ps1
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import warnings
warnings.filterwarnings("ignore")

import os
import time
import cv2
import pandas as pd
from deepface import DeepFace
from datetime import datetime

# ---------------- CONFIG ----------------
DATASET_PATH = "dataset"
ATTENDANCE_FILE = "attendance.csv"

THRESHOLD = 0.35          # lower = stricter matching
SHOW_ERROR_AFTER = 2      # seconds before showing "Face not recognized"
FRAME_SKIP = 5            # run face matching every N frames
# ----------------------------------------

cap = cv2.VideoCapture(0)

print("Show your face to mark attendance. Press Q to quit.")

start_time = time.time()
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # ---------------- FRAME SKIP (PERFORMANCE BOOST) ----------------
    if frame_count % FRAME_SKIP != 0:
        cv2.putText(
            frame,
            "Align your face with the camera",
            (30, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )
        cv2.imshow("Face Attendance", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        continue
    # ----------------------------------------------------------------

    best_match_name = None
    best_match_score = 1.0  # lower is better

    try:
        # Compare live face with all registered faces
        for file in os.listdir(DATASET_PATH):
            if not file.lower().endswith(".jpg"):
                continue

            name = os.path.splitext(file)[0]
            img_path = os.path.join(DATASET_PATH, file)

            result = DeepFace.verify(
                img1_path=frame,
                img2_path=img_path,
                detector_backend="opencv",
                enforce_detection=False,
                distance_metric="cosine"
            )

            distance = result["distance"]

            if distance < best_match_score:
                best_match_score = distance
                best_match_name = name

        # ---------------- FINAL DECISION ----------------
        if best_match_name and best_match_score < THRESHOLD:
            now = datetime.now()
            date = now.strftime("%Y-%m-%d")
            time_now = now.strftime("%H:%M:%S")

            df = pd.read_csv(ATTENDANCE_FILE)
            person_records = df[df["Name"] == best_match_name]

            # TOGGLE LOGIC
            if person_records.empty:
                action = "Punch-In"
            else:
                last_action = person_records.iloc[-1]["Type"]
                action = "Punch-Out" if last_action == "Punch-In" else "Punch-In"

            # Save attendance
            new_entry = pd.DataFrame(
                [[best_match_name, date, time_now, action]],
                columns=["Name", "Date", "Time", "Type"]
            )

            new_entry.to_csv(
                ATTENDANCE_FILE,
                mode="a",
                header=False,
                index=False
            )

            # Message for Streamlit
            message = f"{best_match_name} - {action} marked"
            print(message)

            with open("last_action.txt", "w") as f:
                f.write(message)

            cap.release()
            cv2.destroyAllWindows()
            exit()

        else:
            elapsed_time = time.time() - start_time

            if elapsed_time > SHOW_ERROR_AFTER:
                cv2.putText(
                    frame,
                    "Face not recognized",
                    (30, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2
                )
            else:
                cv2.putText(
                    frame,
                    "Align your face with the camera",
                    (30, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    2
                )

    except Exception:
        pass

    cv2.imshow("Face Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
