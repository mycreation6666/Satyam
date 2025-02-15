<h1 align="center">🎵 Telegram Music Bot 🎵</h1>  
<p align="center">
  <img src="https://img.shields.io/github/stars/mycreation6666/Satyam?style=social">
  <img src="https://img.shields.io/github/forks/mycreation6666/Satyam?style=social">
  <img src="https://img.shields.io/badge/Made%20With-Python-blue">
  <img src="https://img.shields.io/badge/License-MIT-green">
</p>

<p align="center">
  <b>A powerful Telegram bot to play music from YouTube.</b>  
  <br>Supports direct YouTube streaming, downloads, and more!
</p>

---

## 🎯 **Features**
✅ `/play <song_name>` - Download & play music  
✅ `/pause` & `/resume` - Control playback  
✅ `/skip` & `/stop` - Manage queue  
✅ Supports **YouTube, SoundCloud, and Spotify**  
✅ Works on **VPS, Termux, and Docker**  
✅ **Auto-update** & multi-instance support  

---

## 🚀 **One-Click VPS Deployment**  
Click the button below to copy & paste all commands in one click.  

### **📋 Copy & Paste This in Your VPS Terminal**
```bash
sudo apt update && sudo apt upgrade -y && \
sudo apt install -y python3 python3-pip ffmpeg screen git && \
git clone https://github.com/mycreation6666/Satyam.git && cd Satyam && \
pip install -r requirements.txt && \
screen -S musicbot && \
python3 bot.py
