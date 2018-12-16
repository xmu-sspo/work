# -*- coding: utf-8 -*-
from MyScrapy.items import QqScrapyItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor

import datetime
import scrapy
import re

#from urllib.parse import urljoin

#class ThepaperSpider(CrawlSpider):
class ThepaperSpider(CrawlSpider):
    name = 'ThepaperSpider'
    allow_domains = ['www.thepaper.cn']
    start_urls= ['https://www.thepaper.cn/']
  
    #url_pattern = r'newsDetail_forward_[0-9]{7}'
    #['https://www.thepaper.cn/'+'url_pattern']
    #urljoin('https://www.thepaper.cn/', url_pattern)
    #url_pattern1 = urljoin('https://www.thepaper.cn/', url_pattern)
    #/@href
    def parse(self, response):
        for href in response.xpath('//h2/a/@href'):
            #print (href)
            full_url = response.urljoin(href.extract())
            #print (full_url)
            yield scrapy.Request(full_url, callback=self.parse_news)

    def parse_news(self, response): 
        

        item = QqScrapyItem()
        selector = Selector(response)

        data_from = '澎湃网'
        url = response.url
                
        #cmtId = re.findall(re.compile(r'cmt_id = (\d+);'), str(response.body))[0]
        #comments = 'http://coral.qq.com/' + cmtId
        item['data_from'] = data_from
        item['time'] = selector.xpath('//div[@class="news_about"]/p[2]/text()').extract()[0].strip()
        item['url'] = url
        
        #item['comments'] = {'link' : comments}

        #item['contents'] = {'link' : str(response.url), 'title' : u'', 'passage' : u''}
        item['title'] = selector.xpath("//h1[@class='news_title']/text()").extract()
        content = selector.xpath('//div[@class="news_txt"]/text()').extract()  
        if content:
            str = ''.join(content)
            item['content'] = str.strip()
        for next_href in response.xpath('//ul[@id="listhot1"]/li/a/@href'):
            next_url = response.urljoin(next_href.extract())

            # 发送新的url请求加入待爬队列，并调用回调函数 self.parse_news
            yield scrapy.Request(next_url, callback = self.parse_news)
       
        yield item
'''
   
        for next_href in response.xpath('//div[@class="ctread_name"]/a/@href'):
            next_url = response.urljoin(next_href.extract())

            # 发送新的url请求加入待爬队列，并调用回调函数 self.parse_news
            yield scrapy.Request(next_url, callback = self.parse_news)
            
            
            
             next_urls = response.xpath('//div[@class="ctread_name"]/a/@href')
        if next_urls is not None:
            for next_url in next_urls:
                next_url = response.urljoin(next_url.extract()) 
                print (next_url)
                yield scrapy.Request(next_url, callback = self.parse_news)
'''