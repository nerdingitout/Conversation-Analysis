from flask import Flask
import secrets

secret = secrets.token_urlsafe(32)

app = Flask(__name__)
app.secret_key = secret

from app import views 

