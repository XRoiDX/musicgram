import pyrogram

START_TEXT_MSG = '🤖 Hello user!\n\n📩 I can download songs for you. Just send me the song name in below format:\n\n*/song*  _song name_  or\n*/song*  _musician name - song name_\n\nto download some songs. 🎶\n\n**■ ProTips**💡[ » ʙᴏᴛ ʙʏ ᴍᴜsɪᴄ ɢʀᴀᴍᴀᴍ](https://t.me/sanilaassistant_bot) \n                          [»ɢʀᴏᴜᴘ](https://t.me/sanilaassistant_bot)\n                          [»ᴏᴡɴᴇʀ](https://t.me/sanilaassistant_bot)\n                          [»ᴀʙᴏᴜᴛ ᴏᴡɴᴇʀ](https://t.me/sanilaassistant_bot)'

CONFIRMATION_TEXT_MSG = "✅ Song downloaded successfully!\n\n**■ ProTips**💡[ » ʙᴏᴛ ʙʏ ᴍᴜsɪᴄ ɢʀᴀᴍᴀᴍ](https://t.me/sanilaassistant_bot) \n                          [»ɢʀᴏᴜᴘ](https://t.me/sanilaassistant_bot)\n                          [»ᴏᴡɴᴇʀ](https://t.me/sanilaassistant_bot)\n                          [»ᴀʙᴏᴜᴛ ᴏᴡɴᴇʀ](https://t.me/sanilaassistant_bot)"

SPOTIFY_INPUT_ERROR_TEXT_MSG = '‼️ *Oops! The bot does not support Spotify links!*\nTry: "*/song* _song name_"\nor: "*/song* _musician name - song name_"\n\n**■ ProTips**💡[ » ʙᴏᴛ ʙʏ ᴍᴜsɪᴄ ɢʀᴀᴍᴀᴍ](https://t.me/sanilaassistant_bot) \n                          [»ɢʀᴏᴜᴘ](https://t.me/sanilaassistant_bot)\n                          [»ᴏᴡɴᴇʀ(https://t.me/sanilaassistant_bot)\n                          [»ᴀʙᴏᴜᴛ ᴏᴡɴᴇʀ](https://t.me/sanilaassistant_bot)'

INVALID_COMMAND_ERROR_TEXT_MSG = '‼️ *Oops! Invalid command!*\nTry: "*/song* _song name_"\nor: "*/song* _musician name - song name_"\n\n**■ ProTips**💡[ » ʙᴏᴛ ʙʏ ᴍᴜsɪᴄ ɢʀᴀᴍᴀᴍ](https://t.me/sanilaassistant_bot) \n                          [»ɢʀᴏᴜᴘ](https://t.me/sanilaassistant_bot)\n                          [»ᴏᴡɴᴇʀ](https://t.me/sanilaassistant_bot)\n                          [»ᴀʙᴏᴜᴛ ᴏᴡɴᴇʀ](https://t.me/sanilaassistant_bot)'

TOO_LONG_ERROR_TEXT_MSG = '‼️ *Oops! Video too long to convert!*\nOrder something 30 minutes or less.\n\n**■ ProTips**💡[ » ʙᴏᴛ ʙʏ ᴍᴜsɪᴄ ɢʀᴀᴍᴀᴍ](https://t.me/sanilaassistant_bot) \n                          [»ɢʀᴏᴜᴘ](https://t.me/sanilaassistant_bot)\n                          [»ᴏᴡɴᴇʀ](https://t.me/sanilaassistant_bot)\n                          [»ᴀʙᴏᴜᴛ ᴏᴡɴᴇʀ](https://t.me/sanilaassistant_bot)'


