from icecream import ic

from product import Product

p = Product('URL')
ic(p.brand)
ic(p.body_size)
ic(p.cargo_payer)
ic(p.color)
ic(p.description)
ic(p.like_count)
ic(p.price.purchase_price)
ic(p.price.sale_price)
ic(p.status)

ic(p.seller.name)
ic(p.seller.follower_count)
ic(p.seller.followed_count)
ic(p.seller.products)
ic(p.seller.sold)
ic(p.seller.favorites)
