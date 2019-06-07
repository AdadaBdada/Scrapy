### Steps


- open ```pipelines.py``` files

Before

```
class BooksCrawlerPipeline(object):
    def process_item(self, item, spider):
        return item
```
After
```
import os

class BooksCrawlerPipeline(object):
    def process_item(self, item, spider):
        os.chdir('/Users/jinshuo/Desktop/foobar')

        # if the path is existing then we will rename our image
        if item['images'][0]['path']:
            new_image_name = item['title'][0] + '.jpg'
            new_image_path = 'full/' + new_image_name

            os.rename(item['images'][0]['path'],new_image_path)
```

- open ```settings.py``` file to find the ITEM_PIPELINES

Before

```
ITEM_PIPELINES = {
   'scrapy.pipelines.images.ImagesPipeline': 1,
}
```

After

```

ITEM_PIPELINES = {
   'scrapy.pipelines.images.ImagesPipeline': 1,
   'books_crawler.pipelines.BooksCrawlerPipeline':2
}
```

- the number of 1,2 means the spider will execute the ImagesPipeline and then execute the BooksCrawlerPipeline which is rename the images. Lower number as a first thing that needs to happen and the bigger later
