from dataclasses import dataclass, fields
from datetime import datetime

from dolap_scrape.v2.member import Member
import dolap_scrape.v2.api as api


@dataclass(frozen=True, slots=True)
class Product:
    id: int
    price: float
    original_price: float
    condition: str
    shipment_term: str
    title: str
    description: str
    like_count: int
    comment_count: int
    brand: str
    size: str
    owner: Member
    category: str
    updated_date: datetime
    created_date: datetime
    colours: list[str]
    images: list[str]

    def __init__(self, **kwargs):
        def set_attr(key: str, value):
            object.__setattr__(self, key, value)

        def str_to_float(string: str) -> float | None:
            if not string:
                return None
            return float(string.replace('.', '').replace(',', '.'))

        fs = fields(self)
        for k, v in kwargs.items():
            field = any(i for i in fs if i.name == k and i.type == type(v))
            if k in self.__slots__ and field:
                set_attr(k, v)

        for k in self.__slots__:
            if not hasattr(self, k):
                set_attr(k, None)

        if kwargs.get('original_price'):
            set_attr('original_price', str_to_float(kwargs['original_price']))

        if kwargs.get('size'):
            set_attr('size', kwargs['size']['title'])

        set_attr('price', str_to_float(kwargs['price']))
        set_attr('brand', kwargs['brand']['title'])
        set_attr('owner', api.Dolap.member(kwargs['owner']['id']))
        set_attr('category', kwargs['category']['title'])
        set_attr('updated_date', datetime.strptime(kwargs['updated_date'], '%Y%m%d%H%M%S'))
        set_attr('created_date', datetime.strptime(kwargs['created_date'], '%d/%m/%Y %H:%M:%S'))
        set_attr('colours', [i['colour_code'] for i in kwargs['colours']])
        set_attr('images', [i['path'] for i in kwargs['images']])
