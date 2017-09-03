from slackbot.bot import default_reply
import subprocess


@default_reply
def shell(message):
    text = modify(message.body['text'])
    print(text)
    res = subprocess.run(text, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, executable="/bin/bash")
    message.send(res.stdout.decode())


def modify(text):
    return unescapeHtml(trimExtra(text)).replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")


def unescapeHtml(text):
    return text.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")


def trimExtra(text):
    return text.replace("<", "").replace(">", "")
