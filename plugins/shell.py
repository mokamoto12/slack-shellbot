from slackbot.bot import default_reply
import subprocess
from logging import getLogger, basicConfig, INFO


@default_reply
def shell(message):
    text = modify(message.body['text'])
    res = subprocess.run(text, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    basicConfig(format='%(asctime)s %(message)s', filename='exec.log', level=INFO)
    logger = getLogger(__name__)
    logger.info(text)
    message.send(res.stdout.decode())


def modify(text):
    return text.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
