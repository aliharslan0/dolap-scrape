from dataclasses import dataclass, field

from requests import get
from selectolax.lexbor import LexborHTMLParser

import constants
import product


@dataclass(slots=True)
class Profile:
    url: str = field(repr=False)
    __parser: LexborHTMLParser = field(init=False, repr=False)

    @property
    def name(self):
        return self.__parser.css_first(constants.NAME).text()

    @property
    def followed_count(self):
        return int(self.__parser.css_first(constants.FOLLOWED_COUNT).text())

    @property
    def follower_count(self):
        return int(self.__parser.css_first(constants.FOLLOWER_COUNT).text())

    @property
    def favorites(self):
        return list[product.Product]

    @property
    def products(self):
        return list[product.Product]

    @property
    def sold(self):
        return list[product.Product]

    def __reinit(self):
        self.__parser = LexborHTMLParser(get(self.url).content.decode())

    def __post_init__(self):
        self.__reinit()

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)
        if hasattr(self, key) and key == 'url':
            self.__reinit()
