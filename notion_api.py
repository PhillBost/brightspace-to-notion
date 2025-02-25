import requests
import os

from temp.config import NOTION_API_KEY, NOTION_DATABASE_ID

headers = {
    "Authorization": "Bearer " + NOTION_API_KEY,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"
    payload = {"parent": {"database_id": NOTION_DATABASE_ID}, "properties": data}

    res = requests.post(create_url, headers=headers, json=payload)
    print("ID: " + NOTION_DATABASE_ID)
    print(res.status_code)
    return res
