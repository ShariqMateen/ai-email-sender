# ai-email-sender

# 📧 AI Email Sender using Gemini API & Gmail SMTP

This Python script automates professional email writing and sending. It takes user input, extracts the recipient's email, generates a professional email using the **Google Gemini API**, and sends it using **Gmail SMTP**.

---

## 🚀 Features
- 📝 **Takes user input** and extracts the recipient's email.
- 🤖 **Uses Google Gemini AI** to generate a well-formatted professional email.
- 📤 **Sends the email** using Gmail SMTP.
- 🔒 Secure authentication with **App Passwords** (no need for direct login).

---

## 🛠️ Setup Instructions

### 1️⃣ **Clone this repository**
```sh
git clone https://github.com/ShariqMateen/ai-email-sender.git
cd ai-email-sender


2️⃣ Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows

3️⃣ Install Required Dependencies
pip install -r requirements.txt

📌 requirements.txt
google-generativeai
smtplib
email
re


4️⃣ Set Up Google Gemini API
Get an API Key from Google AI Studio.
Replace GEMINI_API_KEY in email_sender.py with your API key.

5️⃣ Enable Gmail SMTP Access
✅ Generate an App Password
Go to Google Account Security: myaccount.google.com/security
Enable 2-Step Verification.
Generate an App Password under "App Passwords" settings.
Replace APP_PASSWORD in email_sender.py with the generated password.

**🎯 How to Use**
1️⃣ Run the Script
python email_sender.py

2️⃣ Enter the email content, including the recipient’s email (e.g.):
📝 Enter the email content (mention the receiver's email in the text):
Hello, I wanted to follow up on our discussion. You can reach me at example@gmail.com.

3️⃣ The script will:

Extract example@gmail.com as the recipient.
Generate a professional email using Gemini AI.
Send the email via Gmail.

**🛡️ Security Recommendations**
  Never expose your API key or App Password in public repositories.
  Use environment variables instead of hardcoding credentials.
  Enable 2-Step Verification for better security.

**📜 License**
This project is MIT licensed. Feel free to use, modify, and share!

**💡 Author**
👤 Shariq Mateen
📧 shariqmateen80@gmail.com
🔗 GitHub: ShariqMateen
