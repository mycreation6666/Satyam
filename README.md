# Telegram Music Bot 🎶

A simple Telegram bot that plays YouTube music.

## 🚀 Features
✅ `/play <song_name>` - Download & play music  
✅ Supports YouTube audio  
✅ Works on VPS & Docker  

---

## **🚀 Deploy on VPS (One-Click Copy)**
Click the button below to copy all VPS deployment commands in one click:  

### **📋 Copy & Paste This in Your VPS Terminal**
```bash
sudo apt update && sudo apt upgrade -y && \
sudo apt install -y python3 python3-pip ffmpeg screen git && \
git clone https://github.com/mycreation6666/Satyam.git && cd Satyam && \
pip install -r requirements.txt && \
screen -S musicbot && \
python3 bot.py
