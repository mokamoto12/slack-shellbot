from slackbot.bot import default_reply
import html
import subprocess


@default_reply
def shell(message):
    text = modify(message.body['text'])
    print(text)
    res = subprocess.run(text, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, executable="/bin/bash")
    message.send(res.stdout.decode())


def modify(text):
    return modify_quote_char(html.unescape(remove_extra_char(text)))


def modify_quote_char(text):
    return text.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")


def remove_extra_char(text):
    return text.replace("<", "").replace(">", "")
