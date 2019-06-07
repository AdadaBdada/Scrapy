### Scrapy Items sample

Terminal code

```
cd Desktop/
scrapy startproject scrapy_items_example
cd scrapy_items_example/
scrapy genspider sample_items_spider quotes.toscrape.com

```

- open ```settings.py```

```
# Before
ROBOTSTXT_OBEY=True

# After
ROBOTSTXT_OBEY=False

```

- define them in ```items.py``` file

Before
```
import scrapy

class QuotesSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
```

After
```
import scrapy

class QuotesSpiderItem(scrapy.Item):
    authors = scrapy.Field()
```

- open ``` sample_items_spider.py``` remove wwww

Before

```
def parse(self, response):
    pass
```

Ordinary way After
```
import scrapy

class SampleItemsSpiderSpider(scrapy.Spider):
    def parse(self, response):
        authors= response.xpath('...')
        yield {'authors':authors}
```

Scrapy items After
```
import scrapy
from scrapy_items_example.items import ScrapyItemsExampleItem

class SampleItemsSpiderSpider(scrapy.Spider):
    def parse(self, response):
        authors= response.xpath('//*[@itemprop="author"]/text()').extract() # selector

        item = ScrapyItemsExampleItem()
        item['authors'] = authors

        return item
```

The generally layout of the items is different as we just yield it.
