import cv2
import os

# Create dataset folder if not exists
if not os.path.exists("dataset"):
    os.makedirs("dataset")

name = input("Enter your name: ").strip()

cap = cv2.VideoCapture(0)

print("Look at the camera. Press 's' to save your face.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Register Face", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        img_path = f"dataset/{name}.jpg"
        cv2.imwrite(img_path, frame)
        print(f"Face saved as {img_path}")
        break

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
