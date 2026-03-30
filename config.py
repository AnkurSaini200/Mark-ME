import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_PATH = "../Data/dataset"
ENCODING_PATH = "../Data/encoding/encodings.pkl"
file_path = "../Data/attendance/attendance.xlsx"

IMAGE_SIZE = (200, 200)
CONFIDENCE_THRESHOLD = 65