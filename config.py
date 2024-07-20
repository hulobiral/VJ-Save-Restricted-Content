import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "7146753"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "524a20714ffc3a161c33f31dd7d361cd")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://roysayanwelder:EV3SEMDlndAsqgRA@cooldude.jnjp9ji.mongodb.net/?retryWrites=true&w=majority&appName=cooldude")
