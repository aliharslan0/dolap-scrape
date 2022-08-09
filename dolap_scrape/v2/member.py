from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Member:
    id: int
    image: str
    cover_image: str
    nickname: str
    bio_text: str
    last_active_date: datetime
    feedback_count: int
    feedback_average: int
    follower_count: int
    followee_count: int
    sold_product_count: int
    sale_product_count: int
    liked_product_count: int

    def __init__(self, **kwargs):
        def set_attr(key: str, value):
            object.__setattr__(self, key, value)

        mr = kwargs['member']

        set_attr('id', mr['id'])
        set_attr('image', mr['image']['path'])
        set_attr('cover_image', mr['cover_image']['path'])
        set_attr('nickname', mr['nickname'])
        set_attr('bio_text', mr['bio_text'])
        set_attr('last_active_date', datetime.strptime(mr['raw_last_active_date'], '%Y%m%d%H%M%S'))
        set_attr('feedback_count', mr['feedback']['feedback_count'])
        set_attr('feedback_average', mr['feedback']['feedback_average'])
        set_attr('follower_count', kwargs['follower_count'])
        set_attr('followee_count', kwargs['followee_count'])
        set_attr('sold_product_count', kwargs['number_of_products_already_sold'])
        set_attr('sale_product_count', kwargs['number_of_products_on_sale'])
        set_attr('liked_product_count', kwargs['number_of_products_liked'])
