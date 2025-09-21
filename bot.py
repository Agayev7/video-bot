from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()  # .env faylni o‘qiydi
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Bot ishga tushdi ✅")

def main():
    # Eski Updater ishlatilmaydi
    app = Application.builder().token(TOKEN).build()
    
    # Handler qo‘shamiz
    app.add_handler(CommandHandler("start", start))
    
    # Botni ishga tushuramiz
    app.run_polling()  # eski asyncio kerak emas

if __name__ == "__main__":
    main()
