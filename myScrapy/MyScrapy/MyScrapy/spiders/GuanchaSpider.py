# -*- coding: utf-8 -*-
from MyScrapy.items import QqScrapyItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
import re
import datetime

#all_urls = set()
class GuanchaSpider(CrawlSpider):
    #global all_urls
    name = 'GuanchaSpider'
    allow_domains = [".guancha.cn"] #过滤广告？
    start_urls = ['https://www.guancha.cn/']  
    #url_pattern = r'https://www.guancha.cn\/[a-zA-Z]+\/[0-9]{4}_[0-9]{2}_[0-9]{2}_[0-9]{6}[_0-9]*.shtml'
    #每日更新，只取当天的url
    year_Month = re.findall("\d+",datetime.datetime.now().strftime('%Y-%m-%d'))
    url_pattern = 'https?://www.guancha.cn/[a-zA-Z]+/'+ year_Month[0] +'_' + year_Month[1] + '_'+year_Month[2]+'_[0-9]{6}[_0-9]*.shtml'
    
    rules = [
                Rule(LxmlLinkExtractor(allow=[url_pattern]), callback= 'parse_news', follow=True)
            ]

    def parse_news(self, response):
        item = QqScrapyItem()
        selector = Selector(response)
        
        #来源、链接
        data_from = '观察者网'
        url = response.url
        item['data_from'] = data_from
        
        #处理url的后缀问题，不同后缀而内容相同导致重复
        item['url'] = re.match(self.url_pattern, url).group()
#        print(item['url'])
                      
        #time
        if selector.xpath("//div[@class='time fix']/span[1]"):
            item['time'] = selector.xpath('//div[@class="time fix"]/span[1]/text()').extract()[0].strip()
        elif selector.xpath("//span[@class='time1']"):#08-29 11:23
            date = selector.xpath("//span[@class='time1']/text()").extract[0].strip()
            item['time'] = '2018-'+date+':00'
        else:
            print("time error",item['url'])
        #只取一年内的新闻***************************************可以删除
        #lastYear = (datetime.datetime.now()-datetime.timedelta(weeks=51)).strftime('%Y-%m-%d %H:%M:%S')
        #if item['time']<lastYear:
        #    return
        
        #每日更新时，url上的日期和发表时间不一致的话，按发表时间来，不计入当日新闻
        year_Month = re.findall("\d+",datetime.datetime.now().strftime('%Y-%m-%d'))
        showTime = re.findall(r"\d+",item['time'])
        if showTime[2]!=year_Month[2] or showTime[1]!=year_Month[1]:
            return
        
        if selector.xpath("//h1"):          
            item['title'] = selector.xpath("//h1/text()").extract()[0].strip()
        elif selector.xpath("//h3"):
            item['title'] = selector.xpath("//h3/text()").extract()[0].strip()
        else:
            print("title error",item['url'])    
         
            
        if selector.xpath("//div[@class='content all-txt']"):
            content = selector.xpath("//div[@class='content all-txt']")   
            item['content']=content.xpath("string(.)").extract()[0].strip()
        elif selector.xpath("//li[@class='left left-main']"):            
            content = selector.xpath("//li[@class='left left-main']")   
            item['content']=content.xpath("string(.)").extract()[0].strip()
        elif selector.xpath("//div[@class='article-txt clearfix']"):
            content = selector.xpath("//div[@class='article-txt clearfix']")
            item['content']=content.xpath("string(.)").extract()[0].strip()
        else:
            print("content error",item['url'])

        
        yield item
        