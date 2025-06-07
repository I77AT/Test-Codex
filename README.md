# Test-Codex

This repository contains a simple Telegram bot example. It replies to **any** message you send with a summary of that message. The summary includes basic information about the message itself, the sender and the chat. If a message was forwarded, the bot also reports the original source.

## Setup

1. Install the required library (version 20 or later):
   ```bash
   pip install -U python-telegram-bot
   ```
2. Replace the `TOKEN` value in `bot.py` with your bot's token from BotFather.

## Usage

Run the bot with:
```bash
python bot.py
```

Send any message (text, photo, sticker, document, etc.) to the bot and it will reply with a detailed summary of that message and its sender.
