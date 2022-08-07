import profile
from dataclasses import dataclass, field

from requests import get
from selectolax.lexbor import LexborHTMLParser

import constants


@dataclass(frozen=True)
class Product:
    @dataclass
    class __Price:
        __purchase_price: float | None = field(init=False, repr=False)
        __sale_price: float = field(init=False, repr=False)
        __parser: LexborHTMLParser = field(repr=False)

        @property
        def purchase_price(self):
            return self.__purchase_price

        @property
        def sale_price(self):
            return self.__sale_price

        def __post_init__(self):
            def normalize(money: str):
                return ''.join(i for i in money.replace('.', '').replace(',', '.') if not i.isalpha())

            if sp := self.__parser.css_first(constants.SALE_PRICE):
                self.__purchase_price = float(normalize(self.__parser.css_first(constants.PURCHASE_PRICE).text()))
                self.__sale_price = float(normalize(sp.text()))
            else:
                self.__purchase_price = None
                self.__sale_price = float(normalize(self.__parser.css_first(constants.PURCHASE_PRICE).text()))

    url: str = field(repr=False)
    __seller: profile.Profile | None = field(init=False, repr=False, default=None)
    __parser: LexborHTMLParser | None = field(init=False, repr=False)

    @property
    def brand(self):
        return self.__parser.css_first(constants.BRAND).text().partition('-')[0].strip()

    @property
    def body_size(self):
        return self.__parser.css_first(constants.BODY_SIZE).text().partition('-')[2].strip()

    @property
    def cargo_payer(self):
        return constants.CargoPayer(self.__parser.css_first(constants.CARGO_PAYER).text())

    @property
    def category(self):
        return self.__parser.css_first(constants.CATEGORY).text()

    @property
    def color(self):
        return self.__parser.css_first(constants.COLOR).text()

    @property
    def description(self):
        return self.__parser.css_first(constants.DESCRIPTION).text()

    @property
    def like_count(self):
        return int(self.__parser.css_first(constants.LIKE_COUNT).text())

    @property
    def price(self):
        return self.__Price(self.__parser)

    @property
    def seller(self):
        if not self.__seller:
            p = profile.Profile(self.__parser.css_first(constants.SELLER_URL).attributes['href'])
            object.__setattr__(self, '_Product__seller', p)
            return self.__seller
        return self.__seller

    @property
    def status(self):
        return constants.Status(self.__parser.css_first(constants.STATUS).text())

    def __post_init__(self):
        object.__setattr__(self, '_Product__parser', LexborHTMLParser(get(self.url).content.decode()))
