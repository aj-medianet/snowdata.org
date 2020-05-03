from app import app
from scraper import skiarea
import secrets
import os



def generate_api_key():
    return secrets.token_urlsafe(40)

