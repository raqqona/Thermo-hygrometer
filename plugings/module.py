from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

@respond_to('何度'):
def printData(message):
    env_data = getData()

    message.replay(env_data)

def getData():
    url = "*****"
    res = requests.get(url)
    values = json.loads(res.text)

    return values
