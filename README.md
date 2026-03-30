# 🎯 MARK-ME — Smart Attendance System

A real-time attendance system powered by **face recognition**, built using Python.
It detects faces via webcam, identifies individuals, and automatically logs attendance with timestamps.

---

## 🚀 Overview

MARK-ME replaces traditional attendance methods with an automated, contactless system.
It uses deep learning–based face recognition to identify individuals and record their presence accurately.

---

## ✨ Key Features

* 📸 Real-time face detection (HOG-based, CPU optimized)
* 🧠 Face recognition using 128-dimensional embeddings (dlib)
* 🗂️ Dataset-driven identity management (one folder per individual)
* 📊 Automatic attendance logging (Excel format)
* ⏱️ IN / OUT time tracking
* 🖥️ Command-line interface for system control
* ⚡ Performance optimizations (frame resizing, frame skipping)

---

## 🧠 System Workflow

### 1. Dataset Preparation

* Store images in:

  ```
  Data/dataset/<person_name>/
  ```
* Each folder corresponds to one individual

---

### 2. Face Encoding

* Faces are detected and converted into numerical embeddings (128D vectors)
* Encodings are stored in:

  ```
  Data/encoding/encodings.pkl
  ```

---

### 3. Face Recognition

* Webcam captures live frames
* Faces are detected and encoded
* Encodings are compared with stored data
* Closest match determines identity

---

### 4. Attendance Logging

* First detection → **IN time recorded**
* Subsequent detection → **OUT time updated**
* Records stored in:

  ```
  Data/attendance/attendance.xlsx
  ```

---

## 📁 Project Structure

```
Mark-ME/
│
├── main.py
│
├── src/
│   ├── encode.py        # Generates face encodings
│   ├── recognize.py     # Handles real-time recognition
│   ├── attendance.py    # Manages attendance records
│
├── Data/
│   ├── dataset/         # Image dataset (per individual)
│   ├── encoding/        # Stored encodings
│   └── attendance/      # Attendance records (Excel)
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd Mark-ME
```

---

### 2. Create and activate virtual environment

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is unavailable:

```bash
pip install face-recognition opencv-python numpy pandas openpyxl
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

---

## 📌 Menu Options

```
1. Encode Faces
2. Start Attendance System
3. Show Attendance Records
4. Exit
```

---

## 🔄 Usage Flow

1. Add images to:

   ```
   Data/dataset/<person_name>/
   ```
2. Select **Encode Faces**
3. Start the recognition system
4. View attendance records

---

## 📊 Attendance Format

| Name     | In Time             | Out Time            |
| -------- | ------------------- | ------------------- |
| Person_A | YYYY-MM-DD HH:MM:SS | YYYY-MM-DD HH:MM:SS |

---

## ⚡ Performance Considerations

* Frame resizing (scale factor: 0.25)
* Alternate frame processing
* HOG-based detection for CPU efficiency
* Adjustable recognition threshold (~0.5–0.6)

---

## ⚠️ Requirements & Notes

* Python **3.11 recommended** (for dlib compatibility)
* Ensure proper lighting conditions
* Use multiple images per individual (10–20 recommended)
* Avoid low-quality or obstructed images

---

## 🛠️ Tech Stack

* Python
* OpenCV
* face_recognition (dlib)
* NumPy
* Pandas
* OpenPyXL

---

## 🔮 Future Enhancements

* Date-wise attendance tracking
* Working hours computation
* Database integration (SQLite/PostgreSQL)
* Web-based dashboard
* Graphical user interface (GUI)
* Face tracking for improved performance
* Liveness detection for spoof prevention

---

## 📄 License

This project is intended for educational and development purposes.
Add a license if distributing publicly.

---

## 👨‍💻 Author

Developed as part of a computer vision–based system design project.
