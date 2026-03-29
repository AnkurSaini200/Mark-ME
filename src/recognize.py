import cv2
import os
from config import IMAGE_SIZE
from src.attendance import mark_attendance

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dataset_path = os.path.join(BASE_DIR, "Data", "dataset")
model_path = os.path.join(BASE_DIR, "Data", "trainer", "model.xml")
cascade_path = os.path.join(BASE_DIR, "models", "haarcascade_frontalface_default.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(model_path)

face_cascade = cv2.CascadeClassifier(cascade_path)

label_map = {}
for idx, person_name in enumerate(sorted(os.listdir(dataset_path))):
    label_map[idx] = person_name

print("label map:", label_map)

cap = cv2.VideoCapture(0)
marked = set()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.05, minNeighbors=7, minSize=(120, 120)
    )

    for (x, y, w, h) in faces:
        face_crop = gray[y:y+h, x:x+w]
        face_crop = cv2.resize(face_crop, IMAGE_SIZE)

        label, confidence = recognizer.predict(face_crop)

        if confidence < 70:
            name = label_map.get(label, "Unknown")

            if name not in marked:
                mark_attendance(name)
                marked.add(name)

            text = f"{name} ({confidence:.2f})"
            color = (0, 255, 0)
        else:
            text = "Unknown"
            color = (0, 0, 255)

        text_y = y - 10 if y - 10 > 20 else y + h + 30

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, text, (x, text_y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


def main():
    pass