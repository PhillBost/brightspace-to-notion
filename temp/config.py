import os

from dotenv import load_dotenv

load_dotenv()

BRIGHTSPACE_API_KEY = os.getenv("BRIGHTSPACE_API_KEY")
NOTION_API_KEY = os.getenv("NOTION_TOKEN") 
NOTION_DATABASE_ID = os.getenv("DATABASE_ID").strip('"')

