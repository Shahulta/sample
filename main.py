from pyrogram import Client, filters

API_ID = "17296819"
API_HASH = "baa838bcf579f71dbcd5ef2ab9ca8f2b"
BOT_TOKEN = "5998095303:AAFDVVJBRQXKp5vyuo7uuwCp1fTsWZtFaRw"


BOT = Client(
    name="PyrogramBot"
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


print("BOT STARTED")


BOT.run()


