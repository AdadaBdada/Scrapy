
### Usage

  ```
  scrapy <command> [options] [args]
  ```

### Available Command
- **bench**: Run quick benchmark test
  - it's mainly used for benching out, or really figuring out the exact performance of your spider code.
- **fetch**: Fetch a URL using the Scrapy downloader
  - or in other word, it will just open the URL with Scrapy

- **genspider** Generate new spider using pre-defined templates

- **runspider** Run a self-contained spider (without creating a project)

  - it's mainly used when you have some simple, maybe, Scrapy projects or when you would like to simplify the Scrapy structure

- **settings** Get settings values

- **shell**
  - shell is one of the most well-known Scrapy features and it will be heavily used whenever we develop any kind of Scrapy projects to test out, or to see if data points are there and to test out our code, in general, in small pieces and then copy and paste the output or really the commands that we write in our shell to the Scrapy code.

- **startproject** Create new project
- **version** Print Scrapy version
- **view** Open URL in browser, as seen by Scrapy
  - To figure out what actually Scrapy sees.
  - On JavaScript-heavy pages, the data will be not sometimes generated or seen, really by Scrapy

```
In [1]: fetch("http://quotes.toscrape.com/")                                                         
2019-06-05 14:33:10 [scrapy.core.engine] INFO: Spider opened
2019-06-05 14:33:11 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/> (referer: None)
```

- The first one just the date and the time that the message was sent and that INFO message is that the spider is opened
- The second one is that DEBUG message and it's Crawled
- The 200 in parenthesis indicates that response is successful (404 would be return probably if the page was not found. 301 if it's redirected, etc.) So as long as it's either on 200 or 300, we are pretty much good to go.

```

In [11]: response                                                                                                                                                                  
Out[11]: <200 http://quotes.toscrape.com/>

In [2]: response.css('h1')                                                                                                                                                         
Out[2]: [<Selector xpath='descendant-or-self::h1' data='<h1>\n                    <a href="/" sty'>]

In [4]: response.xpath('h1')                                                                                                                                                  
Out[4]: []

In [5]: response.xpath('//h1')                                                                                                                                                     
Out[5]: [<Selector xpath='//h1' data='<h1>\n                    <a href="/" sty'>]

In [6]: response.xpath('//h1/a')                                                                                                                                                   
Out[6]: [<Selector xpath='//h1/a' data='<a href="/" style="text-decoration: none'>]

In [8]: response.xpath('//h1/a/text()')                                                                                                                                            
Out[8]: [<Selector xpath='//h1/a/text()' data='Quotes to Scrape'>]

In [9]: response.xpath('//h1/a/text()').extract()                                                                                                                                  
Out[9]: ['Quotes to Scrape']

In [10]: response.xpath('//h1/a/text()').extract_first()                                                                                                                           
Out[10]: 'Quotes to Scrape'

```

- **response** will be pretty much as the name indicates, really reasponse that is going to be returned. So in this case we have 200 as a successful one and then the URL to the response
  - response is going to offer for selecting data either **xpath** or **css** selectors

- **request** is for requesting the URLs and figuring out the FormRequest, etc.

```
In [13]: response.xpath('//*[@class="tag"]')                                                                                                                    
Out[13]:
[<Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/change/page/1/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/deep-thoughts/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/thinking/page/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/world/page/1/"'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/abilities/page'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/choices/page/1'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/inspirational/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/life/page/1/">'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/live/page/1/">'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/miracle/page/1'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/miracles/page/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/aliteracy/page'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/books/page/1/"'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/classic/page/1'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/humor/page/1/"'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/be-yourself/pa'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/inspirational/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/adulthood/page'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/success/page/1'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/value/page/1/"'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/life/page/1/">'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/love/page/1/">'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/edison/page/1/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/failure/page/1'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/inspirational/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/paraphrased/pa'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/misattributed-'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/humor/page/1/"'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/obvious/page/1'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" href="/tag/simile/page/1/'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 28px" h'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 26px" h'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 26px" h'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 24px" h'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 22px" h'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 14px" h'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 10px" h'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 8px" hr'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 8px" hr'>,
 <Selector xpath='//*[@class="tag"]' data='<a class="tag" style="font-size: 6px" hr'>]

 In [14]: response.xpath('//*[@class="tag-item"]')                                                                                                               
Out[14]:
[<Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>,
 <Selector xpath='//*[@class="tag-item"]' data='<span class="tag-item">\n            <a c'>]

In [15]: response.xpath('//*[@class="tag-item"]/a/text()')                                                                                                      
Out[15]:
[<Selector xpath='//*[@class="tag-item"]/a/text()' data='love'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='inspirational'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='life'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='humor'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='books'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='reading'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='friendship'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='friends'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='truth'>,
 <Selector xpath='//*[@class="tag-item"]/a/text()' data='simile'>]

In [16]: response.xpath('//*[@class="tag-item"]/a/text()').extract_first()                                                                                      
Out[16]: 'love'

In [17]: response.xpath('//*[@class="tag-item"]/a/text()').extract()                                                                                            
Out[17]:
['love',
 'inspirational',
 'life',
 'humor',
 'books',
 'reading',
 'friendship',
 'friends',
 'truth',
 'simile']

 In [20]: len(response.xpath('//*[@class="tag-item"]'))                                                                                                          
 Out[20]: 10
```

### Scrapy by default

```
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domain = ["quotes.toscrape.com"]
    start_urls = (
         'http://www.quotes.toscrape.com/',
    )
    def parse(self, response):
        pass
```

- the spider subclassess scrapy.spider and defines some attributes and methods
- **name** for example, identifies obviously the Spider name. It must be **unique** within the project, so you can't really set the same name for a different Spider even though they are in the same project structure
- **allowed_domain** is a list of, obviously, allowed domains. If Scrapy encounters for example, some different domain other than quotes.toscrape.com it will not process it and it will automatically filter it out. Most of the time, you would encounter this if you are crawling every URL on the site.
- **start_urls** is either by default tuple or you can define it as a list. And it's just, it will be pretty much the first URL that Scrapy will process. You don't actually need to use www. in that part so let's exclude this.
- **parse** And parse is Scrapy default callback method in the scrapy.Spider or a.k.a. the basic template that Scrapy offers. So this method is called when or for the Request without an explicitly assigned callback. Defining some other name. It has self, obviously, and the response self is because it's in a class right and response because it will get the response object or HTML nodes or HTML source code from this page.
