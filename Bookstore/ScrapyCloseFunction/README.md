### Scrapy Close Funtion

This function is executed once the Spider is completed scraping. So you can use it to analyze data, send the data file via e-mail or just receive SMS message as a status if it's completed successfully or not

- open ```books.py```

Before

```
from scrapy import Spider
from scrapy.http import Request
```

After

```
import os
import glob
from scrapy import Spider
from scrapy.http import Request

class BooksSpider(Spider):

    def close(self, reason):
        csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
        os.rename(csv_file,"foobar.csv")
```

- Terminal return

```
scrapy crawl books -a category="http://books.toscrape.com/catalogue/category/books/mystery_3/index.html" -o items.csv
```
