import cv2
import face_recognition
import pickle
import os
from src.attendance import mark_attendance


def run_recognition():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ENCODING_PATH = os.path.join(BASE_DIR, "..", "Data", "encoding", "encodings.pkl")

    with open(ENCODING_PATH, "rb") as f:
        data = pickle.load(f)

    video = cv2.VideoCapture(0)

    frame_count = 0
    cap_recent = set()

    while True:
        ret, frame = video.read()
        if not ret:
            continue

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        frame_count += 1
        if frame_count % 2 != 0:
            cv2.imshow("Attendance System", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
            continue

        boxes = face_recognition.face_locations(rgb_small, model="hog")
        encodings = face_recognition.face_encodings(rgb_small, boxes)

        names = []

        for encoding in encodings:
            distances = face_recognition.face_distance(data["encodings"], encoding)
            name = "Unknown"

            if len(distances) > 0:
                match_index = distances.argmin()

                if distances[match_index] < 0.5:
                    name = data["names"][match_index]

                    if name not in cap_recent:
                        mark_attendance(name)
                        cap_recent.add(name)

            names.append(name)

        for (top, right, bottom, left), name in zip(boxes, names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Attendance System", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()