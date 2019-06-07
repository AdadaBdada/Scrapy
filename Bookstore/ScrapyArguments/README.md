### What is the Scrapy Arguments

Scrapy can be used for isolating different categories.
For example if you want to scrape just Philosophy related books. In this case we will gather 11 books and will only scrape pretty much this URLs and then from then on extract data points from the code that we build last time


- open ```books.py```

Before
```
class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']
```

After

```
class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']

    def __init__(self, category):
        self.start_urls = [category]
```

- Terminal code

```
# Before
scrapy crawl books

# After
scrapy crawl books -a category="http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html"
```
