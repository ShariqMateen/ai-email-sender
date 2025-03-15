import smtplib
import re
import google.generativeai as genai
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up Google Gemini API
GEMINI_API_KEY = "AIzaSyCaj3PKGaxlOFlpWEpfYp6rpC3y_ltFyKQ"
genai.configure(api_key=GEMINI_API_KEY)

# Gmail credentials
SENDER_EMAIL = "shariqmateen80@gmail.com"
APP_PASSWORD = "eeyb momc dttk kgeu"  # Generated from Google Security settings

def extract_receiver_email(text):
    """Extracts the receiver's email from the input text using regex."""
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group(0) if match else None

def generate_email(input_text):
    """Uses Gemini API to generate a professional email from the input text."""
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    prompt = f"""
    Write a professional email based on the following input:
    "{input_text}"
    Format it formally with greetings, body, and closing.
    """
    response = model.generate_content(prompt)
    return response.text.strip()

def send_email(receiver_email, subject, body):
    """Sends the email via Gmail SMTP."""
    msg = MIMEMultipart()
    msg['From'] = "Shariq Mateen <" + SENDER_EMAIL + ">"
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Error sending email:", str(e))

# 📝 Take Input from User
if __name__ == "__main__":
    input_text = input("📝 Enter the email content (mention the receiver's email in the text):\n")
    
    receiver_email = extract_receiver_email(input_text)
    
    if receiver_email:
        email_body = generate_email(input_text)
        subject = "Follow-up on Discussion"  # You can modify or take this as input

        print("📧 Sending email to:", receiver_email)
        send_email(receiver_email, subject, email_body)
    else:
        print("⚠️ No valid email address found in input text.")
