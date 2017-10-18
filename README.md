# slack-shellbot
Run bash command with slack

## Installation

[Add bot integration](http://slack.com/services/new/bot) to slack, and note of API Token (use on deploy)


## Deploy

You had better deploy with using Docker.

### with Docker

1. Run container with bot API Token
```
$ docker run -d -e SLACKBOT_API_TOKEN=xoxb-ABC~~ mokamoto12/slack-shellbot
```

2. Mention to bot with slack!

### to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
