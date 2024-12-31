#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28243586"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002377004374"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5961139833"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://madarazbotz:C1wJMA7Yyq2IpWsi@cluster0.olxrn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002000365934"))
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", None)

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_PIC = os.environ.get("START_PIC","https://graph.org/file/6eb635397847d798b231b-9a91ae2772a3fa3ed5.png")
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}\n\nI can store private files in Animes Duo Channel and other users can access it from special link. \n\n ᴘᴏᴡᴇʀᴇᴅ ʙʏ <a href='https://t.me/VR_unreal'>ᴠʀ ᴜɴʀᴇᴀʟ✨</a></b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7871556756 6447084129 5961139833 6551906246 6586546549").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "1500"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "<b>➢ 𝗙𝗶𝗹𝗲𝘀 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗔𝘂𝘁𝗼 𝗗𝗲𝗹𝗲𝘁𝗲𝗱 𝗜𝗻 25 𝗠𝗶𝗻 🥹⏳️ \n➢ 𝗗𝘂𝗲 𝗧𝗼 𝗔𝘃𝗼𝗶𝗱 𝗖𝗼𝗽𝘆𝗿𝗶𝗴𝗵𝘁 𝗜𝘀𝘀𝘂𝗲𝘀 𝗙𝗼𝗿𝘄𝗮𝗿𝗱 & 𝗦𝗮𝘃𝗲 𝗜𝘁 ⚠️</b>")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "Your file has been successfully deleted. Thank you for using our service. ✅")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ᴛʜᴀɴᴋ ʏᴏᴜ! ꜰᴏʀ ᴜꜱɪɴɢ ᴍᴇ. ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴀɴɪᴍᴇꜱ ꜰɪʟᴇꜱ. ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ꜰɪʟᴇꜱ ᴠɪᴀ ᴛʜɪꜱ ᴄʜᴀɴɴᴇʟ.\n ○ 𝐎ᴡɴᴇʀ : <a href='https://t.me/Fushiguro_x'>𝐅ᴜsʜɪɢᴜʀᴏ</a> \n ○ 𝐀ɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_Duo'>𝐀ɴɪᴍᴇ 𝐇ɪɴᴅɪ</a> \n ○ 𝐇ᴀɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/+rqJjl4BBd3M4NDc1'>𝐇ᴜɴᴛᴀɪ 𝐖ᴏʀʟᴅ</a> \n ○ 𝐃ᴇᴠʟᴏᴘᴇʀ : <a href='https://t.me/VR_Necromancer'>ɴᴇᴄʀᴏᴍᴀɴᴄᴇʀ</a> \n ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ <a href='https://t.me/vr_unreal'>ᴠʀ ᴜɴʀᴇᴀʟ</a></b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
