import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 1. /start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "Welcome to AMIZRAKEL Professional Services!\n\n"
        "Here are the available commands:\n"
        "/report — Report Writing Service\n"
        "/assignment — Assignment Writing Service\n"
        "/guide — Guide"
    )
    await update.message.reply_text(welcome_text)

# 2. /report Command
async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📑 *Report Writing Service*\n\n"
        "Need help preparing your academic report? We provide professional "
        "report-writing services tailored to your academic needs. Explore our "
        "report templates and services through our Telegram channel."
    )
    keyboard = [
        [InlineKeyboardButton("✈️ Join Report Writing Channel", url="https://t.me/amizrakel_report")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, parse_mode='Markdown', reply_markup=reply_markup)

# 3. /assignment Command
async def assignment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "✍️ *Assignment Writing Service*\n\n"
        "Looking for help with your university assignments? We provide "
        "assignment-writing services tailored to your academic requirements. "
        "Join our Telegram channel to explore our services."
    )
    keyboard = [
        [InlineKeyboardButton("✈️ Join Assignment Writing Channel", url="https://t.me/amizrakel_assignment")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, parse_mode='Markdown', reply_markup=reply_markup)

# 4. /guide Command
async def guide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📖 *Guide*\n\n"
        "Do you know how we work? Watch our step-by-step video guide to learn "
        "how to use our services and get started."
    )
    keyboard = [
        [InlineKeyboardButton("▶️ Watch the Guide", url="https://t.me/amizrakel_guide")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, parse_mode='Markdown', reply_markup=reply_markup)

if __name__ == '__main__':
    token = "8996652953:AAHVoORy03AJqC5BWCWr8O5nunbRixmHbss"
    application = ApplicationBuilder().token(token).build()

    # Add command handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('report', report))
    application.add_handler(CommandHandler('assignment', assignment))
    application.add_handler(CommandHandler('guide', guide))

    PORT = int(os.environ.get('PORT', 10000))
    
    print("Bot is up and running via Render webhook...")
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path="8996652953:AAHVoORy03AJqC5BWCWr8O5nunbRixmHbss",
        webhook_url=f"https://YOUR-RENDER-APP-NAME.onrender.com/8996652953:AAHVoORy03AJqC5BWCWr8O5nunbRixmHbss"
    )