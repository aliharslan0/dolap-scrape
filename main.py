from icecream import ic

from product import Product

p = Product('https://dolap.com/urun/diger-bej-gomlek-yeni-etiketli-snazzyofficial-222883147')
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

ic(p.seller.favorites)
ic(p.seller.followed_count)
ic(p.seller.follower_count)
ic(p.seller.name)
ic(p.seller.products)
ic(p.seller.sold)

