# Dolap Scrape

Scraper for dolap.com.

## 📕 Example

### V2
```python
from dolap_scrape.v2.api import Dolap

member = Dolap.member_from_url('https://dolap.com/profil/...')
member.id
member.image
member.cover_image
member.nickname
member.bio_text
member.last_active_date
member.feedback_count
member.feedback_average
member.follower_count
member.followee_count
member.sold_product_count
member.sale_product_count
member.liked_product_count

product = Dolap.product_from_url('https://dolap.com/urun/...')
product.id
product.price
product.original_price
product.condition
product.shipment_term
product.title
product.description
product.like_count
product.comment_count
product.brand
product.size
product.owner
product.category
product.updated_date
product.created_date
product.colours
product.images

```

### V1
```python
from dolap_scrape.v1.product import Product

p = Product('https://dolap.com/urun/...')
p.body_size
p.brand
p.cargo_payer
p.category
p.color
p.description
p.like_count
p.images
p.price.purchase
p.price.sale
p.status

p.seller.about
p.seller.favorite_count
p.seller.favorites
p.seller.followed_count
p.seller.follower_count
p.seller.name
p.seller.product_count
p.seller.products
p.seller.sold_count

```
