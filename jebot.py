import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config


Jebot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Jebot.on_message(filters.photo & filters.video)
async def telegraph(client, message): 
     if (
        (photo and photo.file_size <= 5242880)
        or (animation and animation.file_size <= 5242880)
        or (
            video
            and video.file_name.endswith('.mp4')
            and video.file_size <= 5242880
        )
        or (
            document
            and document.file_name.endswith(
                ('.jpg', '.jpeg', '.png', '.gif', '.mp4'),
            )
            and document.file_size <= 5242880
        ):
        await message.reply(message, text='Upto 5mb file size only supported!')
        return
    download_location = await client.download_media(
        message=message.reply_to_message, file_name='root/nana/',
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            message,
            text=f'**Link: https://telegra.ph{response[0]}**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)


print(
    """
Bot Started!
Join @Infinity_BOTs
"""
)

Jebot.run()