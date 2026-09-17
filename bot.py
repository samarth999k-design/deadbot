import os
import sys
import logging
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import telebot
from telebot import types, util

# ==============================================================================
# 🔑 BOT TOKEN (Aapka Token Yahan Set Kar Diya Gaya Hai)
# ==============================================================================
BOT_TOKEN = "8815378095:AAH5IOfoAalhGxB9oDzWFbuHbzSDVsaG1BY"
# ==============================================================================

# Logging Setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize Bot
bot = telebot.TeleBot(BOT_TOKEN)

# Notice Message with Telegram HTML Formatting (Bold + Blockquote `>` + ❤️‍🔥)
MESSAGE_TEXT = (
    "<b>We would like to inform you that we have migrated our SupremeOS from this bot to another bot, @SupremeOSbot. "
    "Please use our new bot to receive any information and to continuously host your Userbot and other bots.</b>\n\n"
    "<blockquote><b>Username - @SupremeOSbot</b> ❤️‍🔥</blockquote>"
)

# Inline Button (1-Tap direct redirect to @SupremeOSbot)
def get_reply_markup():
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(
        text="🚀 Open @SupremeOSbot",
        url="https://t.me/SupremeOSbot"
    )
    markup.add(button)
    return markup


# Har command (/start, /help, etc.) aur har message (text, photo, sticker, voice, docs) pe yahi reply aayega
@bot.message_handler(func=lambda message: True, content_types=util.content_type_media)
def handle_all_messages(message):
    try:
        bot.send_message(
            chat_id=message.chat.id,
            text=MESSAGE_TEXT,
            parse_mode="HTML",
            reply_markup=get_reply_markup(),
            disable_web_page_preview=True
        )
        user = message.from_user.username or message.from_user.first_name
        logger.info(f"Replied to user @{user} (Chat ID: {message.chat.id})")
    except Exception as e:
        logger.error(f"Error while replying to message: {e}")


# Kisi bhi button ya callback query click hone par bhi yahi bhejega
@bot.callback_query_handler(func=lambda call: True)
def handle_all_callbacks(call):
    try:
        bot.answer_callback_query(call.id)
        bot.send_message(
            chat_id=call.message.chat.id,
            text=MESSAGE_TEXT,
            parse_mode="HTML",
            reply_markup=get_reply_markup(),
            disable_web_page_preview=True
        )
    except Exception as e:
        logger.error(f"Error while replying to callback: {e}")


# Railway Dummy HTTP Health Server (Taaki Railway port-binding error na de aur 24/7 bina crash ke chale)
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"OK - SupremeOS Telegram Redirect Bot is active!")

    def log_message(self, format, *args):
        return  # Terminal clean rakhne ke liye access logs silence kiye hain


def start_health_server():
    port = int(os.getenv("PORT", 8080))
    try:
        server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
        logger.info(f"Health check HTTP server running on port {port}")
        server.serve_forever()
    except Exception as e:
        logger.warning(f"Could not start dummy health server (ignored): {e}")


if __name__ == "__main__":
    # Railway web service health check pass karne ke liye dummy server background daemon thread me start karo
    threading.Thread(target=start_health_server, daemon=True).start()

    logger.info("Bot is starting infinity polling (skip_pending=True)...")
    print(">>> SupremeOS Redirect Bot is running headless...")

    # Infinite polling with auto-reconnect and crash tolerance
    bot.infinity_polling(
        skip_pending=True,
        timeout=60,
        long_polling_timeout=30
    )
