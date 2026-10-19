import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# The link you want to share. You can change this easily later.
CURRENT_URL = "https://example.com/guncel-giris"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the current entry address when /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Merhaba {user.mention_html()}! 👋" + "\n\n"
        "İşte güncel giriş adresi:\n"
        f"{CURRENT_URL}"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a help message."""
    await update.message.reply_text("Güncel adresi almak için /start komutunu kullanın.")

def main() -> None:
    """Start the bot."""
    # Railway will provide the token via Environment Variable
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        logger.error("TELEGRAM_TOKEN environment variable is missing!")
        return

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    # drop_pending_updates=True helps avoid replaying old messages on restart
    application.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)

if __name__ == "__main__":
    main()
