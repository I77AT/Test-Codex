from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = "YOUR_BOT_TOKEN_HERE"


async def _send_user_info(update: Update, context: ContextTypes.DEFAULT_TYPE, user) -> None:
    photos = await context.bot.get_user_profile_photos(user.id, limit=1)
    if photos.total_count > 0:
        file_id = photos.photos[0][-1].file_id
        await update.effective_chat.send_photo(photo=file_id)

    text = (
        f"First name: {user.first_name}\n"
        f"Last name: {user.last_name or ''}\n"
        f"Telegram ID: {user.id}"
    )
    await update.message.reply_text(text)


async def _send_chat_info(update: Update, context: ContextTypes.DEFAULT_TYPE, chat) -> None:
    chat_info = await context.bot.get_chat(chat.id)
    if chat_info.photo:
        await update.effective_chat.send_photo(photo=chat_info.photo.big_file_id)
    text = (
        f"Chat title: {chat_info.title}\n"
        f"Chat ID: {chat_info.id}"
    )
    await update.message.reply_text(text)

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await _send_user_info(update, context, update.effective_user)


async def forwarded(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    if message.forward_from:
        await _send_user_info(update, context, message.forward_from)
    elif message.forward_from_chat:
        await _send_chat_info(update, context, message.forward_from_chat)

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("about", about))
    application.add_handler(MessageHandler(filters.FORWARDED, forwarded))
    application.run_polling()

if __name__ == "__main__":
    main()
