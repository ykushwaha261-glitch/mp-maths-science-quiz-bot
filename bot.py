from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import random

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 Welcome to MP Maths & Science Quiz Bot!\n\n"
        "Commands:\n"
        "/quiz - Random Quiz\n"
        "/maths - Maths Quiz\n"
        "/science - Science Quiz"
    )

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    questions = [
        "🧮 Maths\n\nQ. 12 × 8 = ?\n\nA) 84\nB) 96\nC) 108\nD) 88\n\n✅ Answer: B",
        "🔬 Science\n\nQ. पानी का रासायनिक सूत्र क्या है?\n\nA) CO₂\nB) H₂O\nC) O₂\nD) NaCl\n\n✅ Answer: B"
    ]
    await update.message.reply_text(random.choice(questions))

async def maths(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧮 Maths Quiz\n\n"
        "Q. 15 × 6 = ?\n\n"
        "A) 80\nB) 90\nC) 95\nD) 100\n\n"
        "✅ Answer: B"
    )

async def science(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔬 Science Quiz\n\n"
        "Q. मानव शरीर का सबसे बड़ा अंग कौन-सा है?\n\n"
        "A) हृदय\nB) यकृत\nC) त्वचा\nD) फेफड़ा\n\n"
        "✅ Answer: C"
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("quiz", quiz))
app.add_handler(CommandHandler("maths", maths))
app.add_handler(CommandHandler("science", science))

print("Bot is running...")

if __name__ == "__main__":
    app.run_polling()
