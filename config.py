


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26069929")

API_HASH = os.environ.get("API_HASH", "b0551dd4dd9e81b47fe6aa92173aff24")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7728674789:AAE1pcL7yI4je-zaatKOmZIbEXQb3S28o1w
API_ID=26069929") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Dan_Da_Dan_Tamil") 

             

DB_NAME = os.environ.get("DB_NAME", "Rename")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://Luefvt:6369@rename.jjkcm.mongodb.net/?retryWrites=true&w=majority&appName=Rename")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6586630448').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @Exclusivetamilcc 
# Subscribe YouTube Channel For Amazing Bot @Exclusivetamilcc 
# Ask Doubt on telegram @Exclusivetamilcc 
