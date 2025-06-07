from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

TOKEN = "YOUR_BOT_TOKEN_HERE"

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    photos = await context.bot.get_user_profile_photos(user.id, limit=1)
    if photos.total_count > 0:
        photo_file_id = photos.photos[0][-1].file_id
        await update.effective_chat.send_photo(photo=photo_file_id)

    text = (
        f"First name: {user.first_name}\n"
        f"Last name: {user.last_name}\n"
        f"Telegram ID: {user.id}"
    )
    await update.message.reply_text(text)

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("about", about))
    application.run_polling()

if __name__ == "__main__":
    main()
