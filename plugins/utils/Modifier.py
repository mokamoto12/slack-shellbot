import html
from functools import reduce


class Modifier:
    def __init__(self):
        self.__replaces = [
            ("“", '"'),
            ("”", '"'),
            ("‘", "'"),
            ("’", "'"),
        ]
        self.__removes = [
            "<",
            ">",
        ]

    def modify(self, text):
        return self.__replace(html.unescape(self.__remove(text)))

    def __replace(self, text):
        return reduce(lambda carry, item: carry.replace(item[0], item[1]), self.__replaces, text)

    def __remove(self, text):
        return reduce(lambda carry, item: carry.replace(item[0], ""), self.__removes, text)
