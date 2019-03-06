class GetMonzoSpider(scrapy.Spider):
    name = 'get_monzo'

    def start_requests(self):
        urls = [
            'http://reddit.com/r/monzo'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        filename = "monzo_response"
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('%s has been saved' % filename)