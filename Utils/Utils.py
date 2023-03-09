import re
import requests
import os

def validate_discord_webhook(url : str):
    regex = re.compile(r"https://discord(?:app)?\.com/api/webhooks/\d+/(?P<token>[A-Za-z0-9_\-]+)", re.IGNORECASE)
    match = regex.match(url)

    if match is not None:
        return match.group("token")

    return False

def is_webhook_active(url : str):
    if not validate_discord_webhook(url):
        return False

    response = requests.get(url)
    if response.status_code == 200:
        return True

    return False

def clear():
    command = "clear"
    if os.name == "nt":
        command = "cls"

    os.system(command)
