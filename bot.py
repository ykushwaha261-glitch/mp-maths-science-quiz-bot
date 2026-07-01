from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import json
import random

BOT_TOKEN = os.getenv("BOT_TOKEN")

with open("data/questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 Welcome to MP Maths & Science Quiz Bot!\n\n"
        "Commands:\n"
        "/quiz - Random Quiz"
    )

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = random.choice(questions)

    if "question" in q:
        message = f"📚 {q.get('subject','Quiz')}\n\n"
        message += f"Q. {q['question']}\n\n"

        if "options" in q:
            for i, option in enumerate(q["options"]):
                message += f"{chr(65+i)}) {option}\n"

        if "answer" in q:
            message += f"\n✅ Answer: {q['answer']}"

    else:
        message = f"📄 Page {q['page']}\n\n{q['text'][:350]}..."

    await update.message.reply_text(message)

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("quiz", quiz)) print("BOT_TOKEN loaded:", BOT_TOKEN is not None)

if __name__ == "__main__":
    app.run_polling()
