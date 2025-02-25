from datetime import datetime, timezone

from notion_api import create_page
from temp.config import NOTION_DATABASE_ID

title = "Test Title"
description = "Test Description"
published_date = datetime.now().astimezone(timezone.utc).isoformat()
data = {
    "Name": {"title": [{"text": {"content": "Test Entry"}}]}
}

print("NOTION_DATABASE_ID:", NOTION_DATABASE_ID)

res = create_page(data)
print(res.json())

