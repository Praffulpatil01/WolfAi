import requests
import webbrowser
from urllib.parse import urlencode

# Step 1: Replace with your actual keys
CLIENT_ID = "120151"
CLIENT_SECRET ="6tVoKUnpSZmOimOioFQ0bI2JltpPwthsD3hRbnCQgmEWy7bPvOXqWWz4StjfvxIY"
REDIRECT_URI = "https://localhost/callback"

# Step 2: Authorize URL
params = {
    "client_id": CLIENT_ID,
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": "global",
}
url = f"https://public-api.wordpress.com/oauth2/authorize?{urlencode(params)}"
print("Opening browser for authorization...")
webbrowser.open(url)

# Step 3: After logging in, you'll get ?code= in the URL — paste it here
code = input("Paste the authorization code from the URL: ")

# Step 4: Exchange for access token
token_url = "https://public-api.wordpress.com/oauth2/token"
data = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "redirect_uri": REDIRECT_URI,
    "grant_type": "authorization_code",
    "code": code,
}

res = requests.post(token_url, data=data)
print("Access Token:", res.json())