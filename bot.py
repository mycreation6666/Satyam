import os
import logging
import asyncio
from yt_dlp import YoutubeDL
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Configurations
TOKEN = os.getenv("BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")
MAX_FILE_SIZE_MB = 49  # Telegram max limit

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎶 Welcome! Use /play <song_name> to play music.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands:\n/play <song_name> - Play a song\n/help - Show this message")

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Please provide a song name.")
        return

    song_name = " ".join(context.args)
    await update.message.reply_text(f"🔍 Searching for `{song_name}`...")

    file_path = await download_song(song_name)
    if not file_path:
        await update.message.reply_text("❌ Failed to download the song.")
        return

    file_size = os.path.getsize(file_path) / (1024 * 1024)
    if file_size > MAX_FILE_SIZE_MB:
        await update.message.reply_text("❌ This song is too large for Telegram.")
        os.remove(file_path)
        return

    await update.message.reply_audio(audio=open(file_path, "rb"))
    os.remove(file_path)

async def download_song(song_name: str) -> str:
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "song.%(ext)s",
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}],
        "quiet": True,
        "default_search": "ytsearch",
    }

    loop = asyncio.get_event_loop()
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = await loop.run_in_executor(None, lambda: ydl.extract_info(song_name, download=True))
            filename = ydl.prepare_filename(info_dict["entries"][0]).replace(".webm", ".mp3").replace(".m4a", ".mp3")
            return filename
    except Exception as e:
        logger.error(f"Download error: {e}")
        return None

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()

if __name__ == "__main__":
    main()
