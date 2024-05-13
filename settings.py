import os
from dotenv import load_dotenv

# Завантажимо дані середовища з файлу .env(За замовчуванням)
load_dotenv()

# Дістанемо токен бота з середовища
bot_token = os.getenv('BOT_TOKEN')
