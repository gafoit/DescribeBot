import os

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = "/webhook"
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "supersecret")
BASE_WEBHOOK_URL = os.getenv("BASE_WEBHOOK_URL","https://describebot.onrender.com")  # например, https://your-domain.com
WEBHOOK_URL = f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}"

ADMIN_ID = os.getenv("ADMIN_ID", None)