# 🎵 Telegram Music Bot 🎵

A powerful Telegram bot to play music from YouTube.

## 🎯 Features
✅ `/play <song_name>` - Download & play music  
✅ `/pause` & `/resume` - Control playback  
✅ `/skip` & `/stop` - Manage queue  
✅ Supports **YouTube**  
✅ Works on **VPS, Termux, and Docker**  

---

## 🚀 **One-Click VPS Deployment**  
Click the button below to copy & paste all commands in one click.  

### 📋 **Copy & Paste This in Your VPS Terminal**
```bash
sudo apt update && sudo apt upgrade -y && sudo apt install -y python3 python3-pip ffmpeg screen git && git clone https://github.com/mycreation6666/Satyam.git && cd Satyam && pip install -r requirements.txt && screen -S musicbot && python3 bot.py
```

➡ **To detach screen without stopping bot, press:**
```
CTRL + A, then D
```

---

### 📌 **Deploy on Termux**
```bash
pkg update && pkg upgrade -y && pkg install python git ffmpeg && git clone https://github.com/mycreation6666/Satyam.git && cd Satyam && pip install -r requirements.txt && python3 bot.py
```

### 🐳 **Run with Docker**
```bash
docker build -t musicbot .
docker run -d --name musicbot musicbot
```
➡ **To stop the bot:** `docker stop musicbot`  
➡ **To restart:** `docker start musicbot`  

---

## 🔄 **Update to Latest Version**
```bash
cd Satyam && git pull && pip install -r requirements.txt
screen -r musicbot
```
➡ **To stop the bot:** Press `CTRL + C`  
➡ **To restart:** Run `python3 bot.py`  

---

## ❓ **FAQ (Common Issues & Fixes)**  

### 🔹 **Bot is not responding in chat?**  
✔ Make sure your **API keys & tokens** are correct.  

### 🔹 **Bot stops after a few minutes?**  
✔ Use `screen` to keep it running in the background.  

### 🔹 **How to restart the bot?**  
✔ Use these commands:  
```bash
screen -r musicbot
CTRL + C  # Stop the bot
python3 bot.py  # Restart
```
---

## ❤️ **Support & Contributions**
💡 **Got an idea?** Open an **issue** or create a **pull request**!  
⭐ **Like this project?** Consider **starring** it on GitHub!  

---

## 📜 **License**
This project is licensed under the **MIT License**.  
**Free to use & modify!**
© ™️ ʏᴏ ᴍʏsᴛᴇʀɪᴏᴜs
