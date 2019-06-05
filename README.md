# Scrapy

Asynchronous scraping framework

### Scrapy
**Pros**
- pros: when using Scrapy, of course, first and foremost it's Asynchronous
- but if you are building something robust and want to make it as efficient as possible with lots of flexibility and a bunch of functions, then you should deifitely use it.
- One case example when using some other tools, like the previously mentioned tools, kind of makes sense is if you had a project where you need to load the Home Page or something like that or you favorite, let's say, restaurant and check if they are having your favorite dish on the menu. And for this type of cases, you should not use Scrapy because, to be honest, it would be overkill

**Drawbacks**
Since it's really a full-fledged framework, it's not that begineer-friendly and the learning curve is a little steeper than some other tools


- Old specialized libraries with very focused functionality and they don’t claim or they are not really a complete web scraping solution like Scrapy is.

##### urllib2, Request
HTTP for humans are modules for reading or opening web pages, so HTTP modules

**Urllib2**:

- Advantage: it's included in the Pyhton standard libaray so it's batteries-included and as long as you have Python installed, you are good to go

**Requests**:
- I personally use it for quick and dirty scraping jobs and both urllib2 and requests are supported with python2 and python3

##### Beautiful soup and LXML(XML and HTML with Python)

really for extracting data points from those pages that are loaded with urllib2 and then Requests

**Beautiful Soup**:
- it's used for extracting data points from the pages that are loaded. Beautiful Soup is quite robust and it handles nicely malformed markup
- So, in other words, if you have a page that is not getting validated as a proper HTML but you know for a fact taht it's a page and that it's and HTML specifically page, then you should give it a try scraping data from it with Beautiful Soup.
- So actually the name came from the expression 'tag soup' which is used to describe a really invalid markup
- Beautiful Soup creates a parse tree that can be used to extract data from HTML

**LXML - XML and HTML with Python**:
- it handles or it's used for *scraping data*
- it's the most feature-rich(功能丰富) Python library for processing both XML and HTML.
- It's also really fast and memory efficient.
- A fun fact is that Scrapy selectors are built over lxml and for example, Beautiful Soup also supports it as a parser.

**Selenium**
The last tool for scraping is called Selenium

- selenium is first of all a tool writing automated tests for web applications
- It's used for web scraping mainly beacuse it's beginner-friendly and if a site uses JavaScript so if a site is heavy on JavaScript which more and more sites are. Selenium is a good option beacuse, once again, it's easy to extract the data if you are a beginner or if JavaScript interactions are very complex. If we have a bunch of get and post requests
- I use it sometimes solely or in pair with Scrapy and most of the time when I'm using it with Scrapy. I, kind of, try to iterate over once again JavaScript heavy pages and then use Scrapy Selectors to grab the HTML that Selenium produces.
- Overall, Selenium support is really extensive
- Bear in mind that(请记住), from my testing, for example, Scraping thousand pages from Wikipedia was 20 times faster in Scrapy than in Selenium
- Also, on top of that Scrapy consumed a lot less memory and CPU usage was a lot lower with Scrapy than with Selenium
