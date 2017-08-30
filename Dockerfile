# Set your Bots API Token on SLACKBOT_API_TOKEN
FROM python:3.6.2

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 443
CMD ["python", "./run.py"]
