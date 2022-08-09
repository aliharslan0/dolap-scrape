from requests import get, post
from selectolax.lexbor import LexborHTMLParser

from dolap_scrape.v2.member import Member
from dolap_scrape.v2.product import Product


def to_snake_case(string: str):
    return ''.join(f'_{x.lower()}' if x.isupper() else x for x in string)


class Dolap:

    @classmethod
    def dict2snake(cls, dictionary: dict):
        new_dict = {}
        for k, v in dictionary.items():
            if isinstance(v, dict):
                v = cls.dict2snake(v)
            if isinstance(v, list):
                for i in range(len(v)):
                    if isinstance(v[i], dict):
                        v[i] = cls.dict2snake(v[i])
            new_dict[to_snake_case(k)] = v
        return new_dict

    @classmethod
    def product(cls, product_id: int | str):
        return Product(**cls.dict2snake(get(f'https://api.dolap.com/product/{product_id}').json()))

    @classmethod
    def product_from_url(cls, url: str):
        return cls.product(url.split('-')[-1])

    @classmethod
    def member(cls, member_id: int | str):
        headers = {'AppPlatform': 'None', 'AppVersion': '0', 'Content-Type': 'application/json; charset=UTF-8'}
        resp = post('https://api.dolap.com/member/closet', json={'memberId': member_id}, headers=headers)

        return Member(**cls.dict2snake(resp.json()))

    @classmethod
    def member_from_url(cls, url: str):
        content = get(url).content.decode()
        parser = LexborHTMLParser(content)
        member_id = parser.css_first('.person-img span').attributes['data-imageid'][6:]

        return cls.member(member_id)
