# Dolap Scrape

Scraper for dolap.com.

## ⚙ Features

<details> 

- Profile
    - Name
    - Follower Count
    - Followed Count
    - Products
    - Sold Products
    - Favorite Products

- Product
    - Brand
    - Body Size
    - Cargo Payer
    - Category
    - Color
    - Description
    - Like Count
    - Purchase Price
    - Sale Price
    - Status

</details>

## 📕 Example

```python
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

ic(p.seller.name)
ic(p.seller.follower_count)
ic(p.seller.followed_count)
ic(p.seller.products)
ic(p.seller.sold)
ic(p.seller.favorites)
```

Output

```
ic| p.brand: 'Diğer'
ic| p.body_size: 'XL Beden'
ic| p.cargo_payer: <CargoPayer.BUYER: 'Alıcı Öder'>
ic| p.category: 'Gömlek'
ic| p.color: 'Bej'
ic| p.description: 'Ürün sıfır etıketlıdır'
ic| p.like_count: 0
ic| p.price.purchase_price: 189.0
ic| p.price.sale_price: 89.0
ic| p.status: <Status.NEW_AND_LABELLED: 'Yeni ve Etiketli'>
ic| p.seller.name: '@snazzyofficial'
ic| p.seller.follower_count: 3122
ic| p.seller.followed_count: 0
ic| p.seller.products: list[product.Product]
ic| p.seller.sold: list[product.Product]
ic| p.seller.favorites: list[product.Product]
```
