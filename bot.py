import os
import yt_dlp
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# .env fayldan tokenni olish
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Menga video link yuboring, men yuklab beraman 📥")

# Link kelganda ishlaydi
async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    await update.message.reply_text("⏳ Video yuklanmoqda, biroz kuting...")

    try:
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': 'video.mp4',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        await update.message.reply_video(video=open("video.mp4", "rb"))
        os.remove("video.mp4")

    except Exception as e:
        await update.message.reply_text(f"Xato: {str(e)}")

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.get_event_loop().run_until_complete(main())
