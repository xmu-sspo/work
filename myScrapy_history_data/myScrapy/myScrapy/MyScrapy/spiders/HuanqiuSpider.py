# -*- coding: utf-8 -*-

from MyScrapy.items import QqScrapyItem
import datetime
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
import re

#all_urls=set()
class HuanqiuSpider(CrawlSpider):
    #global all_urls
    name = 'HuanqiuSpider'
    allow_domains = [".huanqiu.com"]
    start_urls = ['http://www.huanqiu.com/']
    #去掉error.huanqiu.com 和 v.huanqiu.com
    url_pattern = r'http://[^ev][a-z]*.huanqiu.com\/[a-zA-Z]*\/2018-[0-9]{2}\/[0-9]{8}.html'
    #每日更新，这里是月份
#    year_Month = re.findall("\d+",datetime.datetime.now().strftime('%Y-%m-%d'))
#    url_pattern = 'http://[^ev][a-z]*.huanqiu.com/[a-zA-Z]*/'+year_Month[0]+'-'+year_Month[1]+'/[0-9]{8}.html'
    
    rules = [
                Rule(LxmlLinkExtractor(allow=[url_pattern]), callback= 'parse_news', follow=True)
            ]

    def parse_news(self, response):
        item = QqScrapyItem()
        selector = Selector(response)

        #来源、链接
        data_from = '环球网'
        url = response.url
        item['data_from'] = data_from
        item['url'] = url
#        print(item['url'])
        
        '''去重******************
        if item['url'] in all_urls:
            print('已经在set中')
            return
        else:
            all_urls.add(item['url'])
        print(len(all_urls))
        '''
        
        #标题 
        if selector.xpath('//div[@class="con"]/div[@class="con_left"]/div[@class="l_a"]/h1/text()'):
            item['title'] = selector.xpath('//div[@class="l_a"]/h1/text()').extract()[0].strip()
            content = selector.xpath('//div[@class="l_a"]/div[@class="la_con"]')
            item['content']=content.xpath("string(.)").extract()[0].strip()
            date = selector.xpath('//span[@class="la_t_a"]/text()').extract()[0]
            date += ':00'
            item['time']=date
        elif selector.xpath('//div[@class="con"]/div[@class="conLeft"]/div[@class="conText"]/h1/text()'):
            item['title'] = selector.xpath('//div[@class="conText"]/h1/text()').extract()[0].strip()
            content = selector.xpath('//div[@class="conText"]/div[@id="text"]')
            item['content']=content.xpath("string(.)").extract()[0].strip()
            date = selector.xpath('//div[@class="conText"]/div[@class="summaryNew"]/strong[@id="pubtime_baidu"]/text()').extract()[0]
            item['time']=date
        else:         
            return
        
        #只取一年内的新闻
#        lastYear = (datetime.datetime.now()-datetime.timedelta(weeks=51)).strftime('%Y-%m-%d %H:%M:%S')
#        if item['time']<lastYear:
#            return
        
#        当日新闻！！！
        day = re.findall(r'\d+',item['time'])
        year_Month = re.findall("\d+",datetime.datetime.now().strftime('%Y-%m-%d'))
        if day[2] != year_Month[2]:
            return
            
        yield item