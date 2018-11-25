# -*- coding: utf-8 -*-
from MyScrapy.items import QqScrapyItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
import datetime
import re

class BjnewsSpider(CrawlSpider):
    name = 'BjnewsSpider'
    allow_domains = ['www.bjnews.com.cn']
    start_urls= ['http://www.bjnews.com.cn/']
#    url_pattern = r'http://www.bjnews.com.cn\/[a-z]+/2018/[0-9]{2}/[0-9]{2}/[0-9]+.html'
    #每日更新，这里是月份
    year_Month = re.findall("\d+",datetime.datetime.now().strftime('%Y-%m-%d'))
    url_pattern = r'http://www.bjnews.com.cn\/[a-z]+/' +year_Month[0]+'/'+year_Month[1]+'/'+year_Month[2]+ '/[0-9]+.html'
    rules = [
                Rule(LxmlLinkExtractor(allow=[url_pattern]), callback= 'parse_news', follow=True)
            ]
    
    def parse_news(self, response):
       
        item = QqScrapyItem()
        selector = Selector(response)
        #url_pattern2 = r'(\w+)://(\w+)\.qq\.com/a/(\d{8})/(\d+)\.htm'
        #pattern = re.match(url_pattern2, str(response.url))
        #pattern = re.match(self.url_pattern, str(response.url))
        data_from = '新京报'
        url = response.url
                
        #cmtId = re.findall(re.compile(r'cmt_id = (\d+);'), str(response.body))[0]
        #comments = 'http://coral.qq.com/' + cmtId
        item['data_from'] = data_from
        item['time'] = selector.xpath("//span[@class='date']/text()").extract()[0].strip()
        item['url'] = url
        
        #item['comments'] = {'link' : comments}
        #item['contents'] = {'link' : str(response.url), 'title' : u'', 'passage' : u''}
        item['title'] = selector.xpath("//div[@class='title']/h1/text()").extract()[0].strip()
        content = selector.xpath("//div[@class='content']/p/text()").extract()
        if content:
            str = ''.join(content)
            item['content'] = str
        else:
            print("content error:", item['url'])
            
        if item['title'] == None:
            print("title error:", item['url'])
            
            
        #只取一年内的新闻
#        lastYear = (datetime.datetime.now()-datetime.timedelta(weeks=52)).strftime('%Y-%m-%d %H:%M:%S')
#        if item['time']<lastYear:
#            return
        
        
        yield item
