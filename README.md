# Dolap Scrape

Scraper for dolap.com.

## 📕 Example

```python
from icecream import ic

from src.product import Product

p = Product('https://dolap.com/urun/https://dolap.com/urun/diger-bej-gomlek-yeni-etiketli-snazzyofficial-222883147')
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
```

Output

```
ic| p.body_size: 'XL Beden'
ic| p.brand: 'Diğer'
ic| p.cargo_payer: <CargoPayer.BUYER: 'Alıcı Öder'>
ic| p.category: 'Gömlek'
ic| p.color: 'Bej'
ic| p.description: 'Ürün sıfır etıketlıdır'
ic| p.like_count: 0
ic| p.price.purchase: 189.0
ic| p.price.sale: 89.0
ic| p.status: <Status.NEW_AND_LABELLED: 'Yeni ve Etiketli'>
ic| p.seller.about: ('snazzy.com.tr 🎉Sıfır Etiketli Ürün Satışı Yapılmakta 🎉 ❌ İADE YOK ❌AYNI GÜN '
                     'KARGO 📦🛍')
ic| p.seller.favorite_count: 199
ic| p.seller.favorites: <generator object Profile.__explore at 0x00000215E2CEA9D0>
ic| p.seller.followed_count: 0
ic| p.seller.follower_count: 3124
ic| p.seller.name: '@snazzyofficial'
ic| p.seller.product_count: 1796
ic| p.seller.products: <generator object Profile.__explore at 0x00000215E2CEAB90>
ic| p.seller.sold_count: 2034
```
