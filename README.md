# SupremeOS Telegram Redirect Bot 🚀

Ye ek lightweight aur 100% headless Telegram Python bot script hai jo purane bot pe aane wale har message aur command (`/start`, text, media, etc.) pe direct ye notice bhejti hai:

> **We would like to inform you that we have migrated our SupremeOS from this bot to another bot, @SupremeOSbot. Please use our new bot to receive any information and to continuously host your Userbot and other bots.**
> 
> **Username - @SupremeOSbot** ❤️‍🔥

---

## 📁 Project Structure

```text
├── bot.py           # Main Python bot script (Headless + Healthcheck server)
├── requirements.txt # Dependencies (pyTelegramBotAPI)
├── Procfile         # Railway / Render worker process configuration
├── railway.json     # Railway auto-deploy & restart policy
├── .env.example     # Environment variables format
└── README.md        # Guide
```

---

## ⚡ Railway pe Host Kaise Kare (Step-by-Step)

### Step 1: GitHub pe Repository Banaye
1. Apne GitHub account pe ek nayi repo banaye (e.g. `supremeos-redirect-bot`).
2. Ye saare files (`bot.py`, `requirements.txt`, `Procfile`, `railway.json`) us repository me upload kar de.

### Step 2: Railway pe Deploy Kare
1. [Railway.app](https://railway.app/) pe login kare.
2. **"New Project"** pe click kare.
3. **"Deploy from GitHub repo"** select kare aur apni repo choose kare.

### Step 3: Environment Variable Set Kare
1. Railway Dashboard me apne project ke **Variables** tab me jaye.
2. **`New Variable`** pe click kare:
   - **Key**: `BOT_TOKEN`
   - **Value**: Apne Bot ka Token daale (jo aapko [@BotFather](https://t.me/BotFather) se mila hai).
3. Save / Deploy kare.

> **Note:** Script ke andar ek chhota built-in lightweight HTTP health server add kiya gaya hai taaki Railway ka port healthcheck 100% pass ho aur bot bina kisi crash ke 24/7 headless background me chalta rahe!

---

## 💻 Local Machine ya VPS pe Kaise Run Kare

```bash
# 1. Repo clone / download kare
git clone <your-repo-url>
cd <repo-folder>

# 2. Virtual environment banaye aur activate kare (Optional but recommended)
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Dependencies install kare
pip install -r requirements.txt

# 4. Token set kare aur run kare
export BOT_TOKEN="your_bot_token_here"
python bot.py
```
