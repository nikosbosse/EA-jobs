from typing import Union
import json
import requests


class Webhook:
    def __init__(self):
        self.url = "http://eajobs.ddns.net"
        self.headers = {
            "Content-Type": "application/json"
        }

    def post(self, tweet: dict[str, Union[int, str]]) -> None:
        r = requests.post(
            f"{self.url}/api/add.php",
            headers=self.headers,
            data=json.dumps(tweet),
        )
        if r.status_code == 200:
            print("Successfully posted to webhook.")
        elif r.status_code == 409:
            t_id = tweet["id"]
            print("Webhook responded with conflict.")
            print(f"Tweet {t_id} already posted!")
        else:
            print("An unknown error occured posting to webhook!")
            print(f"{r.status_code}: {r.text}")
