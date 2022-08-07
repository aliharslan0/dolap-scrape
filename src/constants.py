# Product
from enum import Enum


class Status(Enum):
    LITTLE_USED = 'Az Kullanılmış'
    NEW = 'Yeni'
    NEW_AND_LABELLED = 'Yeni ve Etiketli'


class CargoPayer(Enum):
    BUYER = 'Alıcı Öder'
    SELLER = 'Satıcı Öder'


BODY_SIZE = '.title-holder > h1:nth-child(1)'
BRAND = '.title-holder > h1:nth-child(1)'
CARGO_PAYER = 'span.subtitle:nth-child(3)'
CATEGORY = '.breadcrumb > li:nth-last-child(-n+2)'
COLOR = '.color-holder > span:nth-child(2)'
DESCRIPTION = '.remarks-block > p:nth-child(1)'
LIKE_COUNT = '.likes-block > a:nth-child(1) > span:nth-child(2)'
PURCHASE_PRICE = 'div.price-detail:nth-child(1) > span:nth-child(1)'
SALE_PRICE = 'div.price-detail:nth-child(1) > span:nth-child(2)'
SELLER_URL = 'a.title'
STATUS = 'span.subtitle:nth-child(2)'

# Profile
ABOUT = '.text-block > p:nth-child(1)'
NAME = 'div.title-block:nth-child(2) > h1:nth-child(1)'
FOLLOWED_COUNT = '.followers-list > li:nth-child(2) > strong:nth-child(1)'
FOLLOWER_COUNT = '.followers-list > li:nth-child(1) > strong:nth-child(1)'
PRODUCTS = 'div.col-xs-6 > div:nth-child(1) > div:nth-child(2) > a:nth-child(2)'
FAVORITES_PAGE = 'https://dolap.com/profil/favorileri/{}'
PRODUCT_COUNT = '.nav > li:nth-child(1) > a:nth-child(1)'
SOLD_COUNT = '.nav > li:nth-child(2) > a:nth-child(1)'
FAVORITE_COUNT = '.nav > li:nth-child(3) > a:nth-child(1)'
NOT_FOUND = '.visual > h2:nth-child(1)'
