from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()  # faqat lokal test uchun
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Bot ishga tushdi ✅")

def main():
    # Eski Updater ishlatilmaydi
    app = Application.builder().token(TOKEN).build()
    
    # Handler qo‘shamiz
    app.add_handler(CommandHandler("start", start))
    
    # Botni ishga tushuramiz
    app.run_polling()  # asyncio kerak emas

if __name__ == "__main__":
    main()
git add bot.py
git commit -m "Update bot.py to PTB 20+ format"
git push origin main




