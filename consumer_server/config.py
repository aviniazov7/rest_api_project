from dotenv import load_dotenv
import os

load_dotenv()

DATA_API_URL = os.getenv("DATA_API_URL")
DATA_API_KEY = os.getenv("DATA_API_KEY")
