import os
from src.attendance import mark_attendance
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_PATH = os.path.join(BASE_DIR, "..", "Data", "dataset")
ENCODING_PATH = os.path.join(BASE_DIR, "..", "Data", "encoding", "encodings.pkl")

def main():
    while True:
        print("\n====== SMART ATTENDANCE SYSTEM ======")
        print("1. Encode Faces")
        print("2. Start Attendance System")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n[INFO] Encoding faces...")
            os.system("python src/encode.py")

        elif choice == "2":
            print("\n[INFO] Starting recognition...")
            from src.recognize import run_recognition
            run_recognition()

        elif choice == "3":
            print("\n[INFO] Exiting system...")
            break

        else:
            print("\n[ERROR] Invalid choice. Try again.")

if __name__ == "__main__":
    main()