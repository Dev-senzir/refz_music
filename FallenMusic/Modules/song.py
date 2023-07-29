# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os

import requests
import yt_dlp
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch

from FallenMusic import BOT_MENTION, BOT_USERNAME, LOGGER, app


@app.on_message(filters.command(["song", "vsong", "video", "music"]) | filters.command(["تحميل","فيديو","صوت"],prefixes= ["/", "!","","#"]))
async def song(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    m = await message.reply_text("⎊ جارٍ التحميل...")

    query = "".join(" " + str(i) for i in message.command[1:])
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=5).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as ex:
        LOGGER.error(ex)
        return await m.edit_text(
            f"فشل إحضار المسار من ʏᴛ-ᴅʟ.\n\n**السبب :** `{ex}`"
        )

    await m.edit_text("⎊ جارٍ التحميل انتظر,\n\n⎊ بواسطه ‌SPIDER..")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"‌‌‏‌‌‏≪⊶⌯━‌‌‏♢ ⦓ ѕᴏᴜʀᴄᴇ ʀᴇғᴢ 𖤛 ⦔ ♢━‌‌‏⌯⊷≫\n⎊ **العنوان :** [{title[:23]}]({link})\n⎊ **المده :** `{duration}`\n⎊ ** بواسطة :** {BOT_MENTION}\n‌‌‏‌‌‏≪⊶⌯━‌‌‏♢ ⦓ ѕᴏᴜʀᴄᴇ ʀᴇғᴢ 𖤛 ⦔ ♢━‌‌‏⌯⊷≫"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
        try:
            visit_butt = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="يوتيوب",
                            url=link,
                        )
                    ]
                ]
            )
            await app.send_audio(
                chat_id=message.from_user.id,
                audio=audio_file,
                caption=rep,
                thumb=thumb_name,
                title=title,
                duration=dur,
                reply_markup=visit_butt,
            )
            if message.chat.type != ChatType.PRIVATE:
                await message.reply_text(
                    "يرجى التحقق من أن المسؤول قد أرسل الأغنية المطلوبة."
                )
        except:
            start_butt = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="اضغط هنا",
                            url=f"https://t.me/{BOT_USERNAME}?start",
                        )
                    ]
                ]
            )
            return await m.edit_text(
                text="اضغط فوق الزر أدناه وابدأ في تنزيل الأغاني",
                reply_markup=start_butt,
            )
        await m.delete()
    except:
        return await m.edit_text("فشل تحميل الصوت على الخادم")

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as ex:
        LOGGER.error(ex)
