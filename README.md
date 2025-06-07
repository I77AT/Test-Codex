# Test-Codex

This repository contains a simple Telegram bot example. It responds to the `/about` command by sending the user's first available profile photo along with their first name, last name and Telegram ID.

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
