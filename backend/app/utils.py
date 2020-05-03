from app import app
from scraper import skiarea
import secrets
import os
from datetime import date, timedelta


# randomly generates an api key 40 characters long
def generate_api_key():
    return secrets.token_urlsafe(40)


# returns the previous days date so you can call prev.month and prev.year
def get_prev_date():
    first = date.today().replace(day=1) # first day of this month
    prev = first - timedelta(days=1) # last day of last month
    return prev