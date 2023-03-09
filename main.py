import requests
import time

from Utils import Utils


class Main:
    def __init__(self, url: str, action_type: int):
        self.webhook_url = url

        self.action_type = action_type

        if action_type == 2:
            self.spam_content = input("Enter the text to spam:\n> ")
            self.spam_count = input("How many messages do you want to send?\n> ")

    def delete_webhook(self):
        requests.delete(self.webhook_url)

        if not Utils.is_webhook_active(self.webhook_url):
            print("Webhook was successfully deleted.")
            return True
        else:
            print("Unable to delete the webhook.")

        return False

    def spam_webhook(self):
        data = {
            "content": self.spam_content
        }

        headers = {
            "Content-Type": "application/json"
        }

        for i in range(int(self.spam_count)):
            response = requests.post(self.webhook_url, json=data, headers=headers)

            if 200 <= response.status_code < 300:
                print(f"[{i+1}/{self.spam_count}] Message sent")
            else:
                print(f"[{i+1}/{self.spam_count}] Could not send the message. Status code: {response.status_code}\nResponse: {response.json()}")


def start():
    Utils.clear()

    url = input("Please enter the webhook url:\n> ")

    if not Utils.is_webhook_active(url):
        print("This webhook is not active or an invalid URL was supplied!")
        return

    print("Please choose what to do with the webhook.")
    print("Type 1 to delete it\nType 2 to spam it")

    action_type = input("> ")
    if not action_type.isdigit():
        print("Invalid action type. Please try again.")
        time.sleep(0.7)
        start()
    else:
        action_type = int(action_type)

    main = Main(url, action_type)

    if action_type == 1:
        main.delete_webhook()
    elif action_type == 2:
        main.spam_webhook()
    else:
        print("Invalid action type. Please try again.")
        time.sleep(0.7)
        start()


if __name__ == "__main__":
    start()
