from dataclasses import dataclass, field
from functools import cached_property

from requests import get
from selectolax.lexbor import LexborHTMLParser

from src import constants
from src import profile


@dataclass(frozen=True, slots=True)
class Price:
    __price: tuple[str, str]
    purchase: float | None = field(init=False, repr=False, default=None)
    sale: float = field(init=False, repr=False)

    @staticmethod
    def __normalize(price: str):
        return float(''.join(i for i in price.replace('.', '').replace(',', '.') if not i.isalpha()))

    def __post_init__(self):
        p, s = self.__price

        if p:
            object.__setattr__(self, 'purchase', self.__normalize(p))
        object.__setattr__(self, 'sale', self.__normalize(s))


class Product:
    def __init__(self, url: str):
        self.__url = url

    @cached_property
    def __parser(self):
        return LexborHTMLParser(get(self.__url).content.decode())

    @property
    def url(self):
        return self.__url

    @cached_property
    def body_size(self):
        return self.__parser.css_first(constants.BODY_SIZE).text().partition('-')[2].strip()

    @cached_property
    def brand(self):
        return self.__parser.css_first(constants.BRAND).text().partition('-')[0].strip()

    @cached_property
    def cargo_payer(self):
        return constants.CargoPayer(self.__parser.css_first(constants.CARGO_PAYER).text())

    @cached_property
    def category(self):
        return self.__parser.css_first(constants.CATEGORY).text()

    @cached_property
    def color(self):
        return self.__parser.css_first(constants.COLOR).text()

    @cached_property
    def description(self):
        return self.__parser.css_first(constants.DESCRIPTION).text()

    @cached_property
    def like_count(self):
        return int(self.__parser.css_first(constants.LIKE_COUNT).text())

    @cached_property
    def price(self):
        purchase = self.__parser.css_first(constants.PURCHASE_PRICE)
        sale = self.__parser.css_first(constants.SALE_PRICE)

        if sale:
            p, s = purchase.text(), sale.text()
        else:
            p, s = None, purchase.text()

        return Price((p, s))

    @cached_property
    def seller(self):
        return profile.Profile(self.__parser.css_first(constants.SELLER_URL).attributes['href'])

    @cached_property
    def status(self):
        return constants.Status(self.__parser.css_first(constants.STATUS).text())
