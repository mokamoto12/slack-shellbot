import requests


class Client:

    def __init__(self):
        self.__host = 'http://php-evaluate-server'

    def eval(self, code):
        return requests.get(self.__host, params={"eval": code}).text
