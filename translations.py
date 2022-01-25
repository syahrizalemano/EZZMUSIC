from config import ASSISTANT_NAME
from helpers.bot_utils import BOT_NAME, USERNAME


START_TEXT = "ℍ𝕒𝕝𝕝𝕠 𝕊𝕒𝕪𝕒 𝔼ℤℤ𝕄𝕌𝕊𝕀ℂ. 𝕊𝕒𝕪𝕒 𝕞𝕖𝕞𝕡𝕦𝕟𝕪𝕒𝕚 𝕗𝕚𝕥𝕦𝕣 : -𝕃𝕀𝕍𝔼 𝕊𝕋ℝ𝔼𝔸𝕄 [ℝ𝔸𝔻𝕀𝕆 𝕍𝕀𝔻𝔼𝕆/𝔸𝕌𝔻𝕀𝕆 𝔽𝕀𝕃𝔼 𝕄𝔸𝕌 𝕐𝕆𝕌𝕋𝕌𝔹𝔼] 𝕊𝕒𝕪𝕒 𝕕𝕚 𝕄𝕒𝕟𝕒𝕘𝕖 𝕠𝕝𝕖𝕙 𝔼ℤℤℝ𝔸"
HELP_TEXT = f"""
🛠-- **Setting Up Bot**:--

\u2022 Start Voice Chat In Your Group!
\u2022 Add Me (@{USERNAME}) & My Assistant (@{ASSISTANT_NAME}) To Your Group!
\u2022 Give Admin To Me (@{USERNAME}) & My Assistant (@{ASSISTANT_NAME}) In Your Group!

⚔️-- **Available Commands**:--

\u2022 `/play` - Stream An Audio
\u2022 `/stream` - Stream An Video
\u2022 `/pause` - Pause Current Stream
\u2022 `/resume` - Resume Paused Stream
\u2022 `/endstream` - End Stream & Left VC
\u2022 `/restart` - Restart Bot (Sudo Only)
"""
ABOUT_TEXT = f"💡-- **Information**:-- \n\nThis bot is created for streaming videos in telegram group video chats using several methods from WebRTC. Powered by pytgcalls the async client API for the Telegram Group Calls and Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users and Bots. \n\n**This bot licensed under GNU-GPL 3.0 License!**"
