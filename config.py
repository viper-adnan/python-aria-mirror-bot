import os
import pickle

# Making authorized_chats.txt file
AUTH_CHATS = os.environ.get('AUTH_CHATS', '999197022')
AUTHCHAT = AUTH_CHATS.replace(' ', '\n')
with open('authorized_chats.txt', 'w') as authchat:
  print(AUTHCHAT, file=authchat)

# I will find a better way to do that.
GDRIVE_TOKEN = os.environ.get("GDRIVE_TOKEN", None)
if GDRIVE_TOKEN is not None:
   with open('token.pickle', 'wb') as token:
     pickle.dump(GDRIVE_TOKEN, token)

# Importing config.env from vars
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "")
OWNER_ID = os.environ.get("OWNER_ID", None)
DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "/app/downloads")
DOWNLOAD_STATUS_UPDATE_INTERVAL = os.environ.get("DOWNLOAD_STATUS_UPDATE_INTERVAL", "5")
AUTO_DELETE_MESSAGE_DURATION = os.environ.get("AUTO_DELETE_MESSAGE_DURATION", "20")
IS_TEAM_DRIVE = os.environ.get("IS_TEAM_DRIVE", "False")
INDEX_URL = os.environ.get("INDEX_URL", "")
USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
TELEGRAM_API = os.environ.get("TELEGRAM_API", None)
TELEGRAM_HASH = os.environ.get("TELEGRAM_HASH", "")
USE_SERVICE_ACCOUNTS = os.environ.get("USE_SERVICE_ACCOUNTS", "False")
config = """BOT_TOKEN = "{}"
GDRIVE_FOLDER_ID = "{}"
OWNER_ID = {}
DOWNLOAD_DIR = "{}"
DOWNLOAD_STATUS_UPDATE_INTERVAL = {}
AUTO_DELETE_MESSAGE_DURATION = {}
IS_TEAM_DRIVE = "{}"
INDEX_URL = "{}"
USER_SESSION_STRING = "{}"
TELEGRAM_API = {}
TELEGRAM_HASH = "{}"
USE_SERVICE_ACCOUNTS = "{}"
""".format(
  BOT_TOKEN,
  GDRIVE_FOLDER_ID,
  OWNER_ID,
  DOWNLOAD_DIR,
  DOWNLOAD_STATUS_UPDATE_INTERVAL,
  AUTO_DELETE_MESSAGE_DURATION,
  IS_TEAM_DRIVE,
  INDEX_URL,
  USER_SESSION_STRING,
  TELEGRAM_API,
  TELEGRAM_HASH,
  USE_SERVICE_ACCOUNTS
  )
with open('config.env', 'w') as conf:
  print(config, file=conf)