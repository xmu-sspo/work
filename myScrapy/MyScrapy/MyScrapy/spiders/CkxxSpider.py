# -*- coding: utf-8 -*-
from MyScrapy.items import QqScrapyItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
import datetime
import re
class CkxxSpider(CrawlSpider):
    name = 'CkxxSpider'

    allow_domains = ['.cankaoxiaoxi.com']
    start_urls= ['http://www.cankaoxiaoxi.com/']
    year_Month = re.findall("\d+",datetime.datetime.now().strftime('%Y-%m-%d'))
    url_pattern = '(https?:)?//www.cankaoxiaoxi.com/[a-z]+/'+year_Month[0]+''+year_Month[1]+''+year_Month[2]+'/[0-9]+.shtml'
   
    rules = [
                Rule(LxmlLinkExtractor(allow=[url_pattern]), callback='parse_news', follow=True)
            ]

    def parse_news(self, response):
       
        item = QqScrapyItem()
        selector = Selector(response)
       
        data_from = '参考消息网'
        item['data_from'] = data_from
        url = response.url
        item['url'] = url       
        print(item['url']) 

        item['title'] = selector.xpath('//*[@class="articleHead"]/text()').extract()[0].strip()
        item['time'] = selector.xpath('//*[@id="pubtime_baidu"]/text()').extract()[0]
        content = selector.xpath('//div[@class="articleText"]')
        item['content'] = content.xpath("string(.)").extract()[0].strip()

            #item['comments'] = {'link' : comments}
            #item['contents'] = {'link' : str(response.url), 'title' : u'', 'passage' : u''}      

        yield item
        #只取一年内的新闻
#        lastYear = (datetime.datetime.now()-datetime.timedelta(weeks=51)).strftime('%Y-%m-%d %H:%M:%S')
#        if item['time']<lastYear:
#            return
    '''   
#        当日新闻！！！       
        day = re.findall(r'\d+',item['time'])
        year_Month = re.findall("\d+",datetime.datetime.now().strftime('%Y-%m-%d'))
        if day[2] != year_Month[2]:
            return
        '''

# -*- coding: utf-8 -*-

