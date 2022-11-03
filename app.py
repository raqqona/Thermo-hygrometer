from logging import exception
from urllib import response
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
import json
import requests

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


@app.message("何度")
def message_th(message, say):
    try:
        url = "http://127.0.0.1:8080/getLastInfo"
        say("ちょっとまってな～")

        response =requests.get(url)
        res_body = response.text
        res_json = json.loads(res_body)

        if res_json['health'] == False:
            thp = res_json['THP'].split(",")
            mem = "時刻 : " + thp[0] + "\n温度：" + thp[1] + "\n湿度：" + thp[2] + "\n気圧：" + thp[3]
        else:
            mem = "Please, check esp32's health"
        
        say(mem)
    except Exception as e:
        if e == "list index out of range":
            say("no data. please reboot esp32")
        else:
            say("Unknown Error")

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
