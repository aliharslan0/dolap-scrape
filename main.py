from icecream import ic

from src.product import Product

p = Product('https://dolap.com/urun/...')
ic(p.body_size)
ic(p.brand)
ic(p.cargo_payer)
ic(p.category)
ic(p.color)
ic(p.description)
ic(p.like_count)
ic(p.price.purchase)
ic(p.price.sale)
ic(p.status)

ic(p.seller.about)
ic(p.seller.favorite_count)
ic(p.seller.favorites)
ic(p.seller.followed_count)
ic(p.seller.follower_count)
ic(p.seller.name)
ic(p.seller.product_count)
ic(p.seller.products)
ic(p.seller.sold_count)
