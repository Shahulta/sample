from pyrogram import Client, filters

API_ID = "17296819"
API_HASH = "baa838bcf579f71dbcd5ef2ab9ca8f2b"
BOT_TOKEN ="5998095303:AAElI1_jxNpH20FchT6TQnupX-0jLvbpHuQ"


BOT = Client(
    name="PyrogramBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)



@BOT.on_message(filters.command("start"))
async def start_cmd(client, message):
  await message.reply_photo(
    photo="https://telegra.ph/file/8ac514e8c71ec61a9a051.jpg",
    caption="Helo! \nHow are you? \n\n\nplease click /about"
  )

@BOT.on_message(filters.command("about"))
async def about_cmd(client, message):
  await message.reply_text("My Owner Name is @Shanib_c_k ")


print("BOT STARTED")


BOT.run()


