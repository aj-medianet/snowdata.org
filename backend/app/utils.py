import secrets
from datetime import date, timedelta, datetime
import smtplib
import credentials


# randomly generates an api key 40 characters long
def generate_api_key():
    return secrets.token_urlsafe(40)


# returns the last day of the previous month as a date obj
def get_prev_month():
    first = date.today().replace(day=1)  # first day of this month
    prev = first - timedelta(days=1)  # last day of last month
    return prev


# returns the last day from two months ago as a date obj
def get_two_months_ago():
    first = date.today().replace(day=1)  # first day of this month
    prev = first - timedelta(days=1)  # last day of last month
    first_prev = prev.replace(day=1)  # first day of last month
    prev_prev = first_prev - timedelta(days=1)  # last day of 2 months ago
    return prev_prev


# strips all special characters from string
def strip_special_chars(string):
    return ''.join(e for e in string if e.isalnum())


# sends snowdataorg@gmail.com an email
def send_email(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("snowdataorg@gmail.com", credentials.email_password)
    s.sendmail("snowdataorg@gmail.com", "snowdataorg@gmail.com", message)
    s.quit()


def print_error_message(message):
    print("[DEBUG] {}: {}".format(datetime.now(), message))

