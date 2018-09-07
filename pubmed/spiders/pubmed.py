import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'pubmed'
    def __init__(self, category=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        allowed_domains = ['https://www.ncbi.nlm.nih.gov/pubmed/']
        self.start_urls = ['https://www.ncbi.nlm.nih.gov/pubmed/?term=%s' % category]

        rules = (
            # Extract links matching 'category.php' (but not matching 'subsection.php')
            # and follow links from them (since no callback means follow=True by default).
            Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

            # Extract links matching 'item.php' and parse them with the spider's method parse_item
            Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = scrapy.Item()
        item['title']=Info1.xpath('./div[@class="cit"]/a/@title').extract()[0][:-1]
        item['date'] =Info1.xpath('./div[@class="cit"]/text()').extract()[0].split(';')[0]
        item['doi'] = response.xpath('./div[@class="cit"]/a/@alterm').extract()
        return item
