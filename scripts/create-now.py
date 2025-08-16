import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

EXPORT_DIR = os.getenv("BASE_DIR") + "/_wer-now/"

status = input("Update: ")
date = str(datetime.today().strftime("%Y-%m-%d"))

contents = f"""---
layout: now
status: {status}
title: {date}
embed_content: true
---
"""
with open(f"{EXPORT_DIR}{date}.md", "w") as f:
    f.write(contents)