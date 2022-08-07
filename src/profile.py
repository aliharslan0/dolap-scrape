from functools import cached_property

from requests import get
from selectolax.lexbor import LexborHTMLParser

from src import constants
from src import product


class Profile:
    def __init__(self, url: str):
        self.__url = url

    @cached_property
    def __parser(self):
        return LexborHTMLParser(get(self.__url).content.decode())

    @property
    def url(self):
        return self.__url

    @cached_property
    def about(self):
        return self.__parser.css_first(constants.ABOUT).text()

    @cached_property
    def favorite_count(self):
        return int(''.join(i for i in self.__parser.css_first(constants.FAVORITE_COUNT).text() if i.isdigit()))

    @cached_property
    def favorites(self):
        return self.__explore(constants.FAVORITES_PAGE.format(self.name[1:]))

    @cached_property
    def followed_count(self):
        return int(self.__parser.css_first(constants.FOLLOWED_COUNT).text())

    @cached_property
    def follower_count(self):
        return int(self.__parser.css_first(constants.FOLLOWER_COUNT).text())

    @cached_property
    def name(self):
        return self.__parser.css_first(constants.NAME).text()

    @cached_property
    def product_count(self):
        return int(''.join(i for i in self.__parser.css_first(constants.PRODUCT_COUNT).text() if i.isdigit()))

    @cached_property
    def products(self):
        return self.__explore(self.url)

    @cached_property
    def sold_count(self):
        return int(''.join(i for i in self.__parser.css_first(constants.SOLD_COUNT).text() if i.isdigit()))

    @staticmethod
    def __explore(url: str):
        n = 1
        while True:
            resp = get(url, params={'sayfa': n})
            parser = LexborHTMLParser(resp.content.decode())

            if parser.css_first(constants.NOT_FOUND):
                break

            for p in parser.css(constants.PRODUCTS):
                yield product.Product(p.attributes['href'])

            n += 1
