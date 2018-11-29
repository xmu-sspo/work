# -*- coding: utf-8 -*-
from MyScrapy.items import QqScrapyItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
import datetime
import re

class TencentSpider(CrawlSpider):
    name = 'TencentSpider'
    allow_domains = ['.qq.com']
    start_urls= ['https://www.qq.com/']
#    url_pattern = r'https?://[a-zA-Z./]+.qq.com/(a|omn|cmsn)/2018[0-9]{4}/[a-zA-Z0-9_]+.html?'
    #当日新闻
    year_Month = re.findall("\d+",datetime.datetime.now().strftime('%Y-%m-%d'))
    url_pattern = r'https?://[a-zA-Z.]+.qq.com/(a|omn|cmsn)/'+year_Month[0]+year_Month[1]+year_Month[2]+'/[a-zA-Z0-9_]+.html?'
    rules = [
                Rule(LxmlLinkExtractor(allow=[url_pattern]), callback= 'parse_news', follow=True)
            ]

    def parse_news(self, response):
       
        item = QqScrapyItem()
        selector = Selector(response)
        
        item['data_from'] = '腾讯新闻'
        url = response.url
        item['url'] = url
        # 分
        if selector.xpath('//meta[@name="apub:time"]/@content'):
            date = selector.xpath('//meta[@name="apub:time"]/@content').extract()[0].strip()
            item['time']=date
        elif selector.xpath('//meta[@name="_pubtime"]/@content'):
            date = selector.xpath('//meta[@name="_pubtime"]/@content').extract()[0].strip()
            item['time']=date
        elif selector.xpath("//span[@class='a_time']/text()"):
            date = selector.xpath('//span[@class="a_time"]/text()').extract()[0].strip()
            match = re.findall(r"\d+",date)
            item['time'] = match[0]+'-'+match[1]+'-'+match[2]+' '+match[3]+':'+match[4]+':00'
#        elif selector.xpath("//div[@id='ArtFrom']/text()"):  # 2009年03月18日16:47  很多年前的新闻格式
#            date = selector.xpath("//div[@id='ArtFrom']/text()").extract()[1].strip()
#            match = re.findall(r"\d+",date)
#            item['time'] = match[0]+'-'+match[1]+'-'+match[2]+' '+match[3]+':'+match[4]+':00'
#            print("fourth:",item['time'])
        elif selector.xpath("//div[@class='info']/text()"):
            date = selector.xpath("//div[@class='info']/text()")
            match = re.findall(r"\d+",date)
            item['time'] = match[0]+'-'+match[1]+'-'+match[2]+' '+match[3]+':'+match[4]+':00'
            print("five:",date)
        else:
            print("time error:",url)
            
            
        #只取一年内的新闻
#        lastYear = (datetime.datetime.now()-datetime.timedelta(weeks=52)).strftime('%Y-%m-%d %H:%M:%S')
#        if item['time']<lastYear:
#           return
        
        if selector.xpath('//h1/text()'):
            item['title'] = selector.xpath('//h1/text()').extract()
        elif selector.xpath("//div[@id='ArticleTit']/text()"):
            item['title'] = selector.xpath("//div[@id='ArticleTit']/text()")
        else:
            print("title error:",url)
        
        if selector.xpath("//div[@class='content-article']"):
            content = selector.xpath("//div[@class='content-article']")
            item['content'] = content.xpath("string(.)").extract()[0].strip()
        elif selector.xpath("//div[@id='Cnt-Main-Article-QQ']"):
            content = selector.xpath("//div[@id='Cnt-Main-Article-QQ']")
            item['content'] = content.xpath("string(.)").extract()[0].strip()
        elif selector.xpath("//div[@id='ArticleCnt']"):
            content = selector.xpath("//div[@id='ArticleCnt']")
            item['content'] = content.xpath("string(.)").extract()[0].strip()
        else:
            print("content error:",url)

        yield item
