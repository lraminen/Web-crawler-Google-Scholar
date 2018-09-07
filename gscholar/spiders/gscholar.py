import scrapy
from gscholar.items import GscholarItem
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.conf import settings
import re

class GscholarSpider(scrapy.Spider):
    name='gscholar'
    page=settings['ALL_PAGE']
    allowed_domains=['scholar.google.com']
    def start_requests(self):
        yield scrapy.Request('https://scholar.google.com/scholar?start=0&q=%s&hl=en&as_sdt=0,47' % self.category)

def parse(self,response):
    item=GscholarItem()
    for art in response.css('.gs_r.gs_or.gs_scl .gs_ri'):
        item['authors']=obj.css('.gs_a'.xpath('string(.)')).extract_first()
        item['title']=obj.css('.gs_rt a').xpath('string(.)').extract_first()
        item['doi']=obj.css('.gs_rt a::attr(href)').extract_first()
    yield item
        
        
        
