import os
from dotenv import load_dotenv

load_dotenv()

BRIGHTSPACE_API_KEY = os.getenv("BRIGHTSPACE_API_KEY")
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
