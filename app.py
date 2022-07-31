from urllib import response
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
import requests

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


@app.message("何度")
def message_hello(message, say):
    url = "****"
    response =requests.get(url)
    res_body = response.text
    env =res_body.split(",")
    mem = "温度：" + env[1] + "\n湿度：" + env[2] + "\n気圧：" + env[3]
    say(mem)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
