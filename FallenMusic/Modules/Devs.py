import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import app, Telegram
@app.on_message(
    command("صورص","سورس","السورس","ريفز", "ااسورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/6e4359dc87a11152d5951.jpg",
        caption=f"""
╭──── • ◈ • ────╮ 
么  𝒔𝒐𝒖𝒓𝒄𝒆 𝒓𝒆𝒇𝒛♡
么 𝒛𝒐𝒌𝒂]♡(t.me/U_U_X_M) 
么 [َ𝒚𝒐𝒖𝒔𝒆𝒇♡ (t.me/IC_X_K) 
╰──── • ◈ • ────╯ 
  
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝒛𝒐𝒌𝒂♡", url=f"https://t.me/U_U_X_M"), 
                ],[
                    InlineKeyboardButton(
                        "𝒔𝒐𝒖𝒓𝒄𝒆 𝒓𝒆𝒇𝒛 ♡", url=f"t.me/def_Zoka"),
                ],

            ]

        ),

    )
@app.on_message(
   command(["يوسف","المبرمج زوكا","محمد","زوكي"])
)

@app.on_edited_message(command(["يوسف","المبرمج يوسف","يسوفي""المطور"])
)
async def zohary(client: Client, message: Message):
  usr = await app.get_users(6099224368)
  user = await client.get_chat(6099224368)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(6099224368,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - {usr.mention} 🕷
                       
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @{usr.username} 🕷
                       
ႦᎥ᥆ | - {Bio} 🕷       
                         
Ꭵժ | - 6301863282 🕷 """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    sender_id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    sender_name = message.from_user.first_name
    invitelink = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(6099224368, f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
@app.on_message(
    command(["زوكا","المبرمج زوكي","زكو"])
)
@app.on_edited_message(command(["زوقا","المبرمج ز","محمد"])
)
async def zohary(client: Client, message: Message):
  usr = await app.get_users(6643261074)
  user = await client.get_chat(6643261074)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(6643261074,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - {usr.mention} 🕷
                       
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @{usr.username} 🕷
                       
ႦᎥ᥆ | - {Bio} 🕷       
                         
Ꭵժ | - 6643261074 🕷 """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    sender_id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    sender_name = message.from_user.first_name
    invitelink = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(6643261074, f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")@app.on_message(
    command(["زوكا","المبرمج زوكا","المطور يوسف"])
)
@app.on_edited_message(command(["زوكا","المبرمج يوسف","المطور يوسف"])
)
async def zohary(client: Client, message: Message):
  usr = await app.get_users(6301863282)
  user = await client.get_chat(6301863282)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(6301863282,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - {usr.mention} 🕷
                       
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @{usr.username} 🕷
                       
ႦᎥ᥆ | - {Bio} 🕷       
                         
Ꭵժ | - 6301863282 🕷 """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    sender_id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    sender_name = message.from_user.first_name
    invitelink = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(6301863282, f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")