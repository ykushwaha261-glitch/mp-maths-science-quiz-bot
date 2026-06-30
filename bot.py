from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8910718113:AAF9bSR0_HROZ4qJ8mVDR2DLOAXqDwWxOk0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 Welcome to MP Maths & Science Quiz Bot!\n\n"
        "जल्द ही Quiz शुरू होंगे।"
    )

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
