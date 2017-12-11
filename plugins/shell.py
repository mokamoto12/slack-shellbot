from slackbot.bot import default_reply
import subprocess
from plugins.utils.Modifier import Modifier


@default_reply
def shell(message):
    modifier = Modifier()
    text = modifier.modify(message.body['text'])
    print(text)
    res = subprocess.run(text, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, executable="/bin/bash")
    message.send(res.stdout.decode())
