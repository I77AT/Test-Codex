from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "YOUR_BOT_TOKEN_HERE"

def about(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    photos = context.bot.get_user_profile_photos(user.id, limit=1)
    if photos.total_count > 0:
        photo_file_id = photos.photos[0][-1].file_id
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_file_id)
    text = (
        f"First name: {user.first_name}\n"
        f"Last name: {user.last_name}\n"
        f"Telegram ID: {user.id}"
    )
    update.message.reply_text(text)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("about", about))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
