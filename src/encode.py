import face_recognition
import os
import pickle

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_PATH = os.path.join(BASE_DIR, "..", "Data", "dataset")
ENCODING_PATH = os.path.join(BASE_DIR, "..", "Data", "encoding", "encodings.pkl")

os.makedirs("../Data/encoding", exist_ok=True)

known_encoding = []
know_names = []

print("Encoding faces...")

for person_name in os.listdir(DATASET_PATH):
    person_folder = os.path.join(DATASET_PATH, person_name)

    if not os.path.isdir(person_folder):
        continue

    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)

        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) == 0:
            print(f"No face in {image_path}")
            continue

        known_encoding.append(encodings[0])
        know_names.append(person_name)

print("Total encodings:", len(known_encoding))

data = {
    "encodings": known_encoding,
    "names": know_names
}

with open(ENCODING_PATH, "wb") as f:
    pickle.dump(data, f)

print("Encoding complete!")


def main():
    return None