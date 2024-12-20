from authlib.integrations.flask_client import OAuth
from flask import Flask, request, url_for, redirect, session
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Fixed the secret_key assignment

# Initialize OAuth
oauth = OAuth(app)

# Register the OAuth client
oauth.register(
    name="toolwatch",
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    access_token_url="https://commons.wikimedia.org/w/rest.php/oauth2/access_token",
    authorize_url="https://commons.wikimedia.org/w/rest.php/oauth2/authorize",
    api_base_url="https://commons.wikimedia.org/w",
    client_kwargs={},
)

toolwatch = oauth.create_client("toolwatch")

# Define the login route
@app.route("/login")
def login():
    redirect_uri = url_for("authorize", _external=True)
    return toolwatch.authorize_redirect(redirect_uri)

# Define the callback route
@app.route("/api/auth/mediawiki/callback")
def authorize():
    token = toolwatch.authorize_access_token()
    if token:
        resp = toolwatch.get("/w/rest.php/oauth2/resource/profile", token=token)
        resp.raise_for_status()
        profile = resp.json()
        print(profile)
        session['profile'] = profile

    return redirect("/")

# Define the home route
@app.route("/")
def home():
    profile = session.get('profile')
    if profile:
        return f"Logged in as: {profile.get('username', 'Unknown')}"
    return "<a href='/login'>Login with Wikimedia Commons</a>"

if __name__ == "__main__":
    app.run(debug=True)
