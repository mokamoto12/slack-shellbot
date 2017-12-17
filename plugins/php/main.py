import re
from slackbot.bot import respond_to
from plugins.php.Client import Client as PhpClient
from plugins.utils.Modifier import Modifier


@respond_to('^-php (.*)', re.IGNORECASE)
def main(message, php_message):
    modifier = Modifier()
    client = PhpClient()
    php_code = modifier.modify(php_message)
    message.send(client.eval(php_code))
