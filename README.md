# Dolap Scrape

Scraper for dolap.com.

## 📕 Example

```python
from icecream import ic

from src.product import Product

p = Product('https://dolap.com/urun/lc-waikiki-cok-renkli-tshirt-body-yeni-etiketli-yonjastore-222973080')
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
ic| p.body_size: '7 yaş/122 Beden'
ic| p.brand: 'LC Waikiki'
ic| p.cargo_payer: <CargoPayer.BUYER: 'Alıcı Öder'>
ic| p.category: 'Tshirt & Body'
ic| p.color: 'Çok Renkli'
ic| p.description: ('sıfır, yeni etiketli,uzun kol, yuzde yuz pamuk, mevsımlık uzun kol, '
                    'lcwaikiki marka,orta kalınlık, standart kalıp, diğer bebek ve çocuk ürünleri '
                    'için sayfama bakabilirsiniz,yeni sezon ürünler için takıpte kalınız '
                    '#öneri#yorum#keşfet#trendyol#yeni#etiketli#sıfır#çocukgiyim#tshirt#cocuktakım#erkek#kız#kadın#cocuk#zara#hm#mango#kids#indirim#kızcocukgiyim#erkekcocukgiyim')
ic| p.like_count: 0
ic| p.price.purchase: None
ic| p.price.sale: 55.0
ic| p.status: <Status.NEW_AND_LABELLED: 'Yeni ve Etiketli'>
ic| p.seller.about: '©️LCW SATICISI,FİYATLAR GAYET MAKUL VE SONDUR👍İADE VE DEĞİŞİM YOKTUR 🚫'
ic| p.seller.favorite_count: 138
ic| p.seller.favorites: <generator object Profile.__explore at 0x0000027527AAAAB0>
ic| p.seller.followed_count: 19
ic| p.seller.follower_count: 56695
ic| p.seller.name: '@yonjastore'
ic| p.seller.product_count: 174
ic| p.seller.products: <generator object Profile.__explore at 0x0000027527AAA960>
ic| p.seller.sold_count: 10894
```
