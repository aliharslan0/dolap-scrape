from icecream import ic

from product import Product

p = Product('URL')
ic(p.brand)
ic(p.body_size)
ic(p.cargo_payer)
ic(p.category)
ic(p.color)
ic(p.description)
ic(p.like_count)
ic(p.price.purchase_price)
ic(p.price.sale_price)
ic(p.status)

s = p.seller
ic(s.name)
ic(s.follower_count)
ic(s.followed_count)
ic(s.products)
ic(s.sold)
ic(s.favorites)
