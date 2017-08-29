from slackbot.bot import default_reply
import subprocess

@default_reply
def shell(message):
    text = message.body['text']
    res = subprocess.run(text, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    message.send(res.stdout.decode())
