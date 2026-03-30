# MARK-ME — Smart Attendance System

A real-time attendance system powered by face recognition. This project automates attendance tracking using a webcam, eliminating manual processes and ensuring accuracy.

---

## 📌 Overview

MARK-ME uses computer vision and facial recognition to identify individuals and record their attendance with timestamps. The system is lightweight, efficient, and designed to run on CPU-based environments.

---

## ✨ Features

* Real-time face detection using HOG (CPU optimized)
* Face recognition using 128-dimensional embeddings (dlib)
* Dataset-based identity management (one folder per person)
* Automatic attendance logging in Excel format
* IN and OUT time tracking
* Command-line interface for system control
* Performance optimizations for real-time execution

---

## 🧠 System Workflow

### 1. Dataset Preparation

Store images in the following structure:

```
Data/dataset/<person_name>/
```

Each folder represents a unique individual.

---

### 2. Face Encoding

* Faces are extracted and converted into numerical embeddings
* Encodings are stored in:

```
Data/encoding/encodings.pkl
```

---

### 3. Face Recognition

* Webcam captures live video frames
* Faces are detected and encoded
* Encodings are compared with stored data
* Closest match determines identity

---

### 4. Attendance Logging

* First detection → IN time recorded
* Second detection → OUT time updated

Attendance is stored in:

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
│   ├── encode.py       # Generates face encodings
│   ├── recognize.py    # Handles real-time recognition
│   ├── attendance.py   # Manages attendance records
│
├── Data/
│   ├── dataset/        # Image dataset (per individual)
│   ├── encoding/       # Stored encodings
│   └── attendance/     # Attendance records
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/AnkurSaini200/MARK-ME.git
cd Mark-ME
```

### 2. Create virtual environment

```bash
python3.11 -m venv .venv
```

### 3. Activate environment

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

```
face-recognition==1.3.0
opencv-python==4.13.0.92
numpy==2.4.3
openpyxl==3.1.5
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

---

## 📌 Menu Options

1. Encode Faces
2. Start Attendance System
3. Exit

---

## 🔄 Usage Flow

* Add images to:

```
Data/dataset/<person_name>/
```

* Select **Encode Faces**
* Start the recognition system
* Attendance will be recorded automatically

---

## 📊 Attendance Format

| Name     | In Time             | Out Time            |
| -------- | ------------------- | ------------------- |
| Person A | YYYY-MM-DD HH:MM:SS | YYYY-MM-DD HH:MM:SS |

---

## ⚡ Performance Considerations

* Frame resizing (scale factor: 0.25)
* Alternate frame processing
* HOG-based detection for CPU efficiency
* Adjustable recognition threshold (0.5–0.6)

---

## ⚠️ Notes

* Python 3.11 recommended (best compatibility with dlib)
* Ensure proper lighting conditions
* Use multiple images per individual (10–20 recommended)
* Avoid low-quality or obstructed images

---

## 🛠️ Tech Stack

* Python
* OpenCV
* face_recognition (dlib)
* NumPy
* OpenPyXL

---

## 🔮 Future Enhancements

* Date-wise attendance tracking
* Working hours calculation
* Database integration (SQLite/PostgreSQL)
* Web-based dashboard
* Graphical user interface (GUI)
* Face tracking for performance improvement
* Liveness detection for spoof prevention

---

## 👨‍💻 Author

Developed as part of a computer vision–based system project.
