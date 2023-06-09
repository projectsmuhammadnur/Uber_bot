import json
import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
try:
    with open("keys.json", 'r') as f:
        pass
except FileNotFoundError:
    with open("keys.json", 'w') as f:
        json.dump([[]], f)
try:
    with open("paths.json", 'r') as f:
        pass
except FileNotFoundError:
    with open("paths.json", 'w') as f:
        json.dump([[]], f)