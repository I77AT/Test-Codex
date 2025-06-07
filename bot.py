from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = "YOUR_BOT_TOKEN_HERE"


def _message_type(message) -> str:
    if message.text:
        return "text"
    if message.photo:
        return "photo"
    if message.document:
        return "document"
    if message.sticker:
        return "sticker"
    if message.voice:
        return "voice"
    if message.audio:
        return "audio"
    if message.video:
        return "video"
    if message.location:
        return "location"
    if message.contact:
        return "contact"
    return "unknown"


def _media_details(obj, fallback_type: str) -> list[str]:
    details = [f"File ID: {obj.file_id}", f"File unique ID: {obj.file_unique_id}"]
    if getattr(obj, "file_size", None) is not None:
        details.append(f"Size: {obj.file_size}")
    mime = getattr(obj, "mime_type", None)
    details.append(f"Type: {mime or fallback_type}")
    return details


def _forward_details(message) -> list[str]:
    lines: list[str] = []
    origin = getattr(message, "forward_origin", None)
    if origin:
        user = getattr(origin, "from_user", None)
        chat = getattr(origin, "chat", None) or getattr(origin, "from_chat", None)
        if user:
            lines.append("Forwarded from user:")
            lines.append(f"  First name: {user.first_name}")
            lines.append(f"  Last name: {user.last_name or '—'}")
            lines.append(f"  Username: @{user.username}" if user.username else "  Username: —")
            lines.append(f"  ID: {user.id}")
        elif chat:
            lines.append("Forwarded from chat:")
            lines.append(f"  Title: {chat.title or chat.username}")
            lines.append(f"  Type: {chat.type}")
            lines.append(f"  ID: {chat.id}")
    else:
        user = getattr(message, "forward_from", None)
        chat = getattr(message, "forward_from_chat", None)
        if user:
            lines.append("Forwarded from user:")
            lines.append(f"  First name: {user.first_name}")
            lines.append(f"  Last name: {user.last_name or '—'}")
            lines.append(f"  Username: @{user.username}" if user.username else "  Username: —")
            lines.append(f"  ID: {user.id}")
        elif chat:
            lines.append("Forwarded from chat:")
            lines.append(f"  Title: {chat.title or chat.username}")
            lines.append(f"  Type: {chat.type}")
            lines.append(f"  ID: {chat.id}")
    if message.forward_sender_name:
        lines.append(f"Forward sender name: {message.forward_sender_name}")
    return lines


async def summarize(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    if not message:
        return

    lines = [
        f"Message ID: {message.message_id}",
        f"Message type: {_message_type(message)}",
        f"Date: {message.date}",
    ]

    if message.text:
        lines.append(f'Text: "{message.text}"')
    elif message.photo:
        lines.extend(_media_details(message.photo[-1], "photo"))
    elif message.document:
        lines.extend(_media_details(message.document, "document"))
    elif message.sticker:
        lines.extend(_media_details(message.sticker, "sticker"))
    elif message.voice:
        lines.extend(_media_details(message.voice, "voice"))
    elif message.audio:
        lines.extend(_media_details(message.audio, "audio"))
    elif message.video:
        lines.extend(_media_details(message.video, "video"))
    elif message.location:
        lines.append(f"Location: {message.location.latitude}, {message.location.longitude}")
    elif message.contact:
        contact = message.contact
        lines.append(
            f"Contact: {contact.first_name} {contact.last_name or ''} - {contact.phone_number}"
        )

    user = message.from_user
    lines.extend(
        [
            "",
            "Sender:",
            f"First name: {user.first_name}",
            f"Last name: {user.last_name or '—'}",
            f"Username: @{user.username}" if user.username else "Username: —",
            f"User ID: {user.id}",
        ]
    )

    chat = message.chat
    lines.extend(
        [
            "",
            "Chat:",
            f"Chat ID: {chat.id}",
            f"Chat type: {chat.type}",
            f"Title / Username: {chat.title or chat.username or '—'}",
        ]
    )

    fwd = _forward_details(message)
    if fwd:
        lines.append("")
        lines.extend(fwd)

    await message.reply_text("\n".join(lines))


def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.ALL, summarize))
    application.run_polling()


if __name__ == "__main__":
    main()
