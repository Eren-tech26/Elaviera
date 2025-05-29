import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()


API_ID = 21968859

API_HASH = "21a59d21687f01d448530ee88a26b1eb"

BOT_TOKEN = "7815129108:AAHZzstO_eClQhXHtNQT4TKyI2sl8IfUKZc"

BOT_ID = 7815129108

BOT_USERNAME = "@DLuffyprobot"

OWNER_USERNAME = "@Eren_Aethonix"

BOT_NAME = "Lᴜғғʏ ꭙ 𝐌ᴜsɪᴄ 🏀"

ASSUSERNAME = "@luffyassistant"

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://thebiggestcomebackever:EREN1234@cluster0.7q7ri.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = 500000

LOGGER_ID = int(getenv("LOGGER_ID", --1002346695101) 

DISASTER_LOG = -1001997798206

OWNER_ID = 7774827065

SPECIAL_USER = 5268691896

HEROKU_APP_NAME = "vipppp"

HEROKU_API_KEY = "HRKU-3a48d735-445f-49c4-a6cf-fea438f945ef"

UPSTREAM_REPO = "https://github.com/paradox-zenu/test"

UPSTREAM_BRANCH = "master"

GIT_TOKEN = "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"

SUPPORT_CHANNEL = "https://t.me/aethonixsupport"

SUPPORT_CHAT = "https://t.me/igrischatsupport"

AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = 9000

SPOTIFY_CLIENT_ID = "22b6125bfe224587b722d6815002db2b"

SPOTIFY_CLIENT_SECRET = "c9c63c6fbf2f467c8bc68624851e9773"

SERVER_PLAYLIST_LIMIT = 3000
PLAYLIST_FETCH_LIMIT = 25

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

SONG_DOWNLOAD_DURATION = 9999999
SONG_DOWNLOAD_DURATION_LIMIT = 9999999

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

STRING1 = getenv("STRING1", "BQE71UwAkqPoZOUEjRt37DGk1wkMLjfCzANARDxT7oj32GyWl1eX4JYMiTiYaH6UeozUa3eB4Ao8WJ5FXodYzqw65v_Y_sq3Mhv0KC9K6QZC14g6yghDerNNszNKB7-_9JlI3TElzVwzBgmXmVJT5Q6J4S3u8umC76gvU5HvY_PC8j-gt3Qr886wKq7pBg8qj1K6Reil602Pymzcg5K3Cc0AsPdOucEQeuM-ABsNdtFAVAEKX7bSZU7kRqGwXEVQl7jg7OE-NG_UnB-BQvMaHzkyZgzOgKSzzSg-rjkFzqrQlk3xfqFf8Uk1aTCzoTfNBxgnb-FiRVyMjZF6V1hWi07nNXHzagAAAAG072FsAA")
STRING2 = getenv("STRING2", None)
STRING3 = getenv("STRING3", None)
STRING4 = getenv("STRING4", None)
STRING5 = getenv("STRING5", None)
STRING6 = None
STRING7 = None


filter = filters.user()
BANNED_USERS = filter
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL =  "https://i.ibb.co/N6M43PFX/photo-2025-04-01-15-22-27-7488365447255949356.jpg"
PLAYLIST_IMG_URL = "https://i.ibb.co/N6M43PFX/photo-2025-04-01-15-22-27-7488365447255949356.jpg"
STATS_IMG_URL = "https://i.ibb.co/N6M43PFX/photo-2025-04-01-15-22-27-7488365447255949356.jpg"
TELEGRAM_AUDIO_URL = "https://i.ibb.co/N6M43PFX/photo-2025-04-01-15-22-27-7488365447255949356.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/N6M43PFX/photo-2025-04-01-15-22-27-7488365447255949356.jpg"
STREAM_IMG_URL = "https://i.ibb.co/N6M43PFX/photo-2025-04-01-15-22-27-7488365447255949356.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/N6M43PFX/photo-2025-04-01-15-22-27-7488365447255949356.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/N6M43PFX/photo-2025-04-01-15-22-27-7488365447255949356.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/N6M43PFX/photo-2025-04-01-15-22-27-7488365447255949356.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/N6M43PFX/photo-2025-04-01-15-22-27-7488365447255949356.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/N6M43PFX/photo-2025-04-01-15-22-27-7488365447255949356.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
