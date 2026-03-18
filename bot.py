from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8558650689:AAH6YfMhqbGkd1FIA5Wl4PBX40aKRl016LY"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

    text = update.message.text

    if not text:
        return

    # реагируем только на reel
    if "instagram.com/reel/" in text:

        new_text = text.replace(
            "instagram.com/reel/",
            "kkinstagram.com/reel/"
        )

        await update.message.reply_text(new_text)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()
