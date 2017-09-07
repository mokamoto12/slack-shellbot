# slack-shellbot
Run bash command with slack

## Installation

1. [Add bot integration](http://slack.com/services/new/bot) to slack, and note of API Token (use on deploy)

2. In terminal, clone this repository, and `cd` cloned project.
```
$ git clone https://github.com/mokamoto12/slack-shellbot.git && cd slack-shellbot
```


## Deploy

You had better deploy with using Docker.

### with Docker

1. Build image
```
$ docker build -t slack-shellbot:1 .
```

2. Run image with bot API Token
```
$ docker run -d -e SLACKBOT_API_TOKEN=xoxb-ABC~~ slack-shellbot:1
```

3. Mention to bot with slack!

### to Heroku

You can deploy to heroku with using [heroku container registry](https://devcenter.heroku.com/articles/container-registry-and-runtime).
