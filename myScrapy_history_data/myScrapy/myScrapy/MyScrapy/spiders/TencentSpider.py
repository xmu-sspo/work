# -*- coding: utf-8 -*-
from MyScrapy.items import QqScrapyItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
import datetime
import re

class TencentSpider(CrawlSpider):
    name = 'TencentSpider'
    allow_domains = ['qq.com']
    start_urls= ['http://news.qq.com/']
    #url_pattern = r'(https?:)?//news?\.qq\.com\/(a|omn|cmsn)\/((\d{8})\/)?[a-zA-Z0-9_]+(\.html?)?'
    #当日新闻
    year_Month = re.findall("\d+",datetime.datetime.now().strftime('%Y-%m-%d'))
    url_pattern = '(https?:)?//new.qq.com/(a|omn|cmsn)/'+year_Month[0]+year_Month[1]+year_Month[2]+'/[a-zA-Z0-9_]+.html'
    rules = [
                Rule(LxmlLinkExtractor(allow=[url_pattern]), callback= 'parse_news', follow=True)
            ]

    def parse_news(self, response):
       
        item = QqScrapyItem()
        selector = Selector(response)
        #url_pattern2 = r'(\w+)://(\w+)\.qq\.com/a/(\d{8})/(\d+)\.htm'
        #pattern = re.match(url_pattern2, str(response.url))
        #pattern = re.match(self.url_pattern, str(response.url))
        data_from = '腾讯新闻'
        url = response.url
                
        #cmtId = re.findall(re.compile(r'cmt_id = (\d+);'), str(response.body))[0]
        #comments = 'http://coral.qq.com/' + cmtId
        item['data_from'] = data_from
        if selector.xpath('//*[@class="a_time"]/text()'):
            item['time'] = selector.xpath('//*[@class="a_time"]/text()').extract()[0].strip()

        item['url'] = url
        
        #item['comments'] = {'link' : comments}
        #item['contents'] = {'link' : str(response.url), 'title' : u'', 'passage' : u''}
        item['title'] = selector.xpath('//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/h1/text()').extract()
        content = response.xpath('//*[@id="Cnt-Main-Article-QQ"]/p/text()').extract()  
        if content:
            str = ''.join(content)
            item['content'] = str

        yield item
