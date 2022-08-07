from dataclasses import dataclass, field

from requests import get
from selectolax.lexbor import LexborHTMLParser

import constants
import product


@dataclass(frozen=True)
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

    def __post_init__(self):
        object.__setattr__(self, '_Profile__parser', LexborHTMLParser(get(self.url).content.decode()))
