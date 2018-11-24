# -*- coding: utf-8 -*-

from MyScrapy.items import QqScrapyItem
import datetime
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
import re

#all_urls = set()
class SinaSpider(CrawlSpider):
    #global all_urls
    name = 'SinaSpider'
    allow_domains = [".sina.com.cn/"]
    start_urls = ['https://www.sina.com.cn/']
#    url_pattern = r'https?://[a-z]+.sina.com.cn\/[a-z\/]+[0-9-]+\/[0-9a-z]+-+[0-9a-z]+.shtml'
    #当天新闻
    year_Month = re.findall("\d+",datetime.datetime.now().strftime('%Y-%m-%d'))
    url_pattern = 'https?://[a-z]+.sina.com.cn/[a-z\/]+'+year_Month[0]+'-'+year_Month[1]+'-'+year_Month[2]+'/[0-9a-z-]+.shtml'

    rules = [
                Rule(LxmlLinkExtractor(allow=[url_pattern]), callback= 'parse_news', follow=True)
            ]
        
    def parse_news(self, response):
        item = QqScrapyItem()
        selector = Selector(response)

        #来源、链接
        data_from = '新浪网'
        url = response.url
        item['data_from'] = data_from
        item['url'] = re.match(self.url_pattern, url).group()
        '''#去重******************
        if item['url'] in all_urls:
            print('已经在set中')
            return
        else:
            all_urls.add(item['url'])
        print(len(all_urls))'''
        
        #time
        if selector.xpath("//span[@id='pub_date']"):
            date = selector.xpath("//span[@id='pub_date']/text()").extract()[0].strip()
            if re.findall(r"\d+-\d+-\d+ \d+:\d+:\d+",date):# 2018-03-01 08:29:56  
                item['time'] = date
            elif re.findall(r"\d+年\d+月\d+日\d+:\d+",date):# 2018年08月25日10:01
                match = re.findall(r"\d+",date)
                item['time'] = match[0]+'-'+match[1]+'-'+match[2]+' '+match[3]+':'+match[4]+':00'
            elif re.findall(r"\d+年\d+月\d+日 \d+:\d+",date):# 2018年08月25日 10:01
                match = re.findall(r"\d+",date)
                item['time'] = match[0]+'-'+match[1]+'-'+match[2]+' '+match[3]+':'+match[4]+':00'
            else:
                item['time'] = "null"
                print('time error!',item['url'])
        elif selector.xpath("//span[@class='date']"):#2018年08月24日 10:37 #//body/div/div/div/div/div/span
            date = selector.xpath("//span[@class='date']/text()").extract()[0].strip()
            match = re.findall(r"\d+",date)
            item['time'] = match[0]+'-'+match[1]+'-'+match[2]+' '+match[3]+':'+match[4]+':00'  
        elif selector.xpath("//div[@id='page-info']/span"):   # 2017年02月07日03:25	 
            date = selector.xpath("//div[@id='page-info']/span/text()").extract()[0].strip()
            match = re.findall(r"\d+",date)
            item['time'] = match[0]+'-'+match[1]+'-'+match[2]+' '+match[3]+':'+match[4]+':00'           
        elif selector.xpath("//body/div/div/span/span"):#2018年08月24日 10:37 XXXX
            date = selector.xpath("//body/div/div/span/span/text()").extract()[0].strip()
            match = re.findall(r"\d+",date)
            item['time'] = match[0]+'-'+match[1]+'-'+match[2]+' '+match[3]+':'+match[4]+':00'
        elif selector.xpath("//div[@id='artibody']/div/p/span[1]/text()"):#2017-07-18 15:26
            date = selector.xpath("//div[@id='artibody']/div/p/span[1]/text()").extract()[0].strip()
            match = re.findall(r"\d+",date)
            item['time'] = match[0]+'-'+match[1]+'-'+match[2]+' '+match[3]+':'+match[4]+':00'
        elif selector.xpath("//span[@class='article-a__time']/text()"): # 2017年02月07日03:25	 
            date = selector.xpath("//span[@class='article-a__time']/text()").extract()[0].strip()
            match = re.findall(r"\d+",date)
            item['time'] = match[0]+'-'+match[1]+'-'+match[2]+' '+match[3]+':'+match[4]+':00'
        elif selector.xpath("//span/div/text()"): # xxx  2018-03-01 08:29:56 xxx
            date = selector.xpath("//span/div/text()").extract()[0].strip()
            match = re.findall(r"\d+-\d+-\d+ \d+:\d+:\d+",date)
            item['time'] = match[0]
        else:
            item['time'] = 'null'
            print('time error!',item['url'])
        
        #只取一年内的新闻
        #lastYear = (datetime.datetime.now()-datetime.timedelta(weeks=52)).strftime('%Y-%m-%d %H:%M:%S')
        #if item['time']<lastYear:
        #   return
                
        #title
        if selector.xpath("//div/h1"):
            if selector.xpath("//div/h1/text()").extract()[0]:
                item['title'] = selector.xpath("//div/h1/text()").extract()[0].strip()
            else:
                item['title'] = selector.xpath("//div/h1/text()").extract()[1].strip()
        elif selector.xpath("//span/h1"):    
            item['title'] = selector.xpath("//span/h1/text()").extract()[0].strip()
        else:
            item['title'] = "null"
            print('title error!',item['url'])
        
        #content
        if selector.xpath("//div[@id='artibody']"):
            content = selector.xpath("//div[@id='artibody']")
            item['content'] = content.xpath("string(.)").extract()[0].strip()
        elif selector.xpath("//div[@id='article']"):
            content = selector.xpath("//div[@id='article']")
            item['content'] = content.xpath("string(.)").extract()[0].strip()               
        else:
            item['content'] = "null"
            print('content error!',item['url'])
        
        #不存在的网页
        if item['title']=='null' and item['content']=='null' and item['time']=='null':
            return
        elif item['time']=='null':
            item['time'] = '2018-8-26 1:56:59'        
            
        yield item