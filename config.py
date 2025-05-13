import os
from dotenv import load_dotenv

load_dotenv()  # .env 불러오기

DATA_PATH = os.getenv("DATA_PATH")
SAVE_EMB_PATH = os.getenv("SAVE_EMB_PATH")
CHROMA_DIR = os.getenv("CHROMA_DIR")
MODEL_NAME = os.getenv("MODEL_NAME")
BATCH_SIZE = int(os.getenv("BATCH_SIZE", 100))
