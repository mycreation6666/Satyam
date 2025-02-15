import os
import logging
import asyncio
from yt_dlp import YoutubeDL
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from concurrent.futures import ThreadPoolExecutor

# Enable logging
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurations
TOKEN = os.getenv("BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")
MAX_FILE_SIZE_MB = 49  # Telegram max limit

# Threading for parallel downloads
executor = ThreadPoolExecutor(max_workers=5)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎶 Welcome! Use /play <song_name> to play music.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands:\n/play <song_name> - Play a song\n/help - Show this message")

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Please provide a song name.")
        return

    song_name = " ".join(context.args)
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(executor, download_and_send_song, update, song_name)

def download_and_send_song(update: Update, song_name: str):
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "song.%(ext)s",
            "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}],
            "quiet": True
        }

        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(f"ytsearch:{song_name}", download=True)
            filename = ydl.prepare_filename(info_dict["entries"][0]).replace(".webm", ".mp3").replace(".m4a", ".mp3")

        file_size = os.path.getsize(filename) / (1024 * 1024)
        if file_size > MAX_FILE_SIZE_MB:
            update.message.reply_text("❌ This song is too large for Telegram.")
            os.remove(filename)
            return

        with open(filename, "rb") as audio_file:
            update.message.reply_audio(audio_file)

        os.remove(filename)

    except Exception as e:
        logger.error(f"Error: {e}")
        update.message.reply_text("❌ Failed to play the song. Try again later.")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()

if __name__ == "__main__":
    main()
