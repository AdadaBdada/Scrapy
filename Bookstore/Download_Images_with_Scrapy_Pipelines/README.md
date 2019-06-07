### Steps

To download images locally to your file file system
- ```sudo pip install Pillow```

- open ```item.py``` files

Before

```
import scrapy

class BooksCrawlerPipeline(scrapy.Item):
    pass

```
After
```
import scrapy

class BooksCrawlerPipeline(scrapy.Item):
    title=scrapy.Field()
    price=scrapy.Field()

    images_urls=scrapy.Field()
    images=scrapy.Field()
```

- open ```settings.py``` file to find the ITEM_PIPELINES

Before

```
ROBOTSTXT_OBEY = True

#ITEM_PIPELINES = {
#   'books_crawler.pipelines.SomePipeline': 300,
#}
```

After

```
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
   'scrapy.pipelines.images.ImagesPipeline': 1,
    # 'ImagesPipeline' just a pipeline that Scrapy default offers it.
}

IMAGES_STORE = '/Users/jinshuo/Desktop/foobar'

```

- Then the ```books.py``` file

Before

```
from scrapy import Spider
from scrapy.http import Request

class BooksSpider(Spider):

    def parse_book(self, response):

        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@class="price_color"]/text()').extract_first()

        image_urls = response.xpath('//img/@src').extract_first()
        image_urls = image_urls.replace('../..', 'http://books.toscrape.com/')
```

After

```
from scrapy import Spider
from scrapy.http import Request
from scrapy.loader import ItemLoader
from books_crawler.items import BooksCrawlerItem


class BooksSpider(Spider):

    def parse_book(self, response):
        l = ItemLoader(item=BooksCrawlerItem(), response=response)

        title = response.css('h1::text').extract_first()
        price = response.xpath('//*[@class="price_color"]/text()').extract_first()

        image_urls = response.xpath('//img/@src').extract_first()
        image_urls = image_urls.replace('../..', 'http://books.toscrape.com/')

        l.add_value('title', title)
        l.add_value('price', price)
        l.add_value('image_urls', image_urls)

        return l.load_item()
```
