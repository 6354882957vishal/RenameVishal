# Don't Remove Credit @SUMIT_KING_2
# Subscribe YouTube Channel For Amazing Bot @King1_devil
# Ask Doubt on telegram @King1_devil


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26489431")

API_HASH = os.environ.get("API_HASH", "9a2fce85339bb79254a55368a61ab92f")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6894711196:AAFbJwceoj8o1R-XP2DeQVup8VKqL_numCw") 

FORCE_SUB = os.environ.get("FORCE_SUB", "SUMIT_KING2") 

             # Don't Remove Credit @SUMIT_KING2
             # Subscribe YouTube Channel For Amazing Bot @SUMIT_KING9
             # Ask Doubt on telegram @King1_devil

DB_NAME = os.environ.get("DB_NAME", "Cluster0")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://loveyouhacker499:<7OPdxBQh4jnnh9yD>@cluster0.ftrtj6o.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2108417544').split()]

PORT = os.environ.get("PORT", "8000")

# Don't Remove Credit @SUMIT_KING_2
# Subscribe YouTube Channel For Amazing Bot @King1_devil
# Ask Doubt on telegram @King1_devil