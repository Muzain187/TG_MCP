import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("TG_HOST")
GRAPH = os.getenv("TG_GRAPH")
SECRET = os.getenv("TG_SECRET")
