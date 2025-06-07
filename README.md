# Test-Codex

This repository contains a simple Telegram bot example. It responds to the `/about` command by sending the user's first available profile photo along with their first name, last name and Telegram ID.
If you forward a message or file to the bot, it will reply with details about the original sender (forwards from users) or the original chat/channel.

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

Send `/about` to the bot in Telegram to receive your profile information.
You can also forward any message or file to the bot to get information about the original author or chat.
