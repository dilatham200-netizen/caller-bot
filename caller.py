from telegram.ext import Application, CommandHandler
import os

TOKEN = os.environ.get("8338230541:AAEYsmVq-J4ejj7stNhWZd0hSUpgHsNq-gE")

async def start(update, context):
    await update.message.reply_text("OK")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
