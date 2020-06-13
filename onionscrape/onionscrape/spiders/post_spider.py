import scrapy

class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls = [ 
        'https://www.theonion.com/latest?startTime=1591279920321' 
    ]

    def parse(self, response):
        for post in response.css('article.cw4lnv-0.iTueKC.js_post_item'):
            category = post.css('.vxl3c2-0.eYptU::text').get()
            newtitle = post.css('.cw4lnv-5.aoiLP a h2::text')[0].get()
            if category not in ['American Voices', 'Infographic', 'Slideshow', 'Entertainment', 'Editorial Cartoon'] and category is not None:
                yield{
                    'title': post.css('.cw4lnv-5.aoiLP a h2::text')[0].get().replace('"', ""),
                    'category' : post.css('.vxl3c2-0.eYptU::text').get(),
                    'date': post.css('.sc-3nbvzd-1.kpXIm::text')[0].get(),
                    'time': post.css('.sc-3nbvzd-1.kpXIm::text')[1].get()
                }
        next_page = response.css('div.row a::attr(href)').get()
        if next_page is not None:
            next_page = 'https://www.theonion.com/latest' + next_page
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            
#python3 -m venv venv
#source venv/bin/activate
#scrapy startproject onionscrape
#cd onionscrape

#scrapy crawl posts

#scrapy shell https://blog.scrapinghub.com/
#>>> response.css('title')
#>>> response.css('title').get()
#>>> response.css('title::text').get()
#>>> response.css('h3::text').get()
#>>> response.css('h3::text').get()
#>>> response.css('h3::text').get()
#>>> response.css('p::text').re(r'scraping')
#>>> response.css('p::text').re(r'scraping')
#>>> response.css('p::text').re(r'scraping')

#>>> post = response.css('div.post-item')
#>>> post = response.css('div.post-item')[0]
#post
#>>> title = post.css('.post-header h2 a::text')[0].get()
#>>> date = post.css('.post-header a::text')[0].get()

#onion
#>>> post = response.css('article.cw4lnv-0.iTueKC.js_post_item')
#>>> title = post.css('.cw4lnv-5.aoiLP a h2::text')[0].get()
#>>> category = post.css('.vxl3c2-0.eYptU::text')[0].get()
#>>> date = post.css('.sc-3nbvzd-1.kpXIm::text')[0].get()
#>>> time = post.css('.sc-3nbvzd-1.kpXIm::text')[1].get()

#>>> for post in response.css('article.cw4lnv-0.iTueKC.js_post_item'):
#...     title = post.css('.cw4lnv-5.aoiLP a h2::text')[0].get()
#...     category = post.css('.vxl3c2-0.eYptU::text')[0].get()
#...     date = post.css('.sc-3nbvzd-1.kpXIm::text')[0].get()
#...     time = post.css('.sc-3nbvzd-1.kpXIm::text')[1].get()
#...     print(dict(title=title, category=category, date = date, time=time))

#next_page = response.css('div.row a::attr(href)').get() return time only
#need to do onion.com/next_page(variable)

#scrapy crawl posts -o posts.csv