# Product
from enum import Enum


class BodySize(Enum):
    pass


class Status(Enum):
    pass


class CargoPayer(Enum):
    pass


class Color(Enum):
    pass


PURCHASE_PRICE = 'div.price-detail:nth-child(1) > span:nth-child(1)'
SALE_PRICE = 'div.price-detail:nth-child(1) > span:nth-child(2)'
BRAND = '.title-holder > h1:nth-child(1)'
BODY_SIZE = '.title-holder > h1:nth-child(1)'
STATUS = 'span.subtitle:nth-child(2)'
CARGO_PAYER = 'span.subtitle:nth-child(3)'
LIKE_COUNT = '.likes-block > a:nth-child(1) > span:nth-child(2)'
SELLER_URL = 'a.title'
DESCRIPTION = '.remarks-block > p:nth-child(1)'
COLOR = '.color-holder > span:nth-child(2)'

# Profile
NAME = 'div.title-block:nth-child(2) > h1:nth-child(1)'
FOLLOWER_COUNT = '.followers-list > li:nth-child(1) > strong:nth-child(1)'
FOLLOWED_COUNT = '.followers-list > li:nth-child(2) > strong:nth-child(1)'
