# -*- coding: utf-8 -*-

from MyScrapy.items import QqScrapyItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
import datetime
import re
class SohuSpider(CrawlSpider):
    name = 'SohuSpider'
    allow_domains = ['www.sohu.com']
    start_urls = ['http://www.sohu.com']
    url_pattern = r'(https?:)?//www.sohu.com/a/[0-9]{9}_[0-9]{6}.*'
    year_Month = re.findall("\d+",datetime.datetime.now().strftime('%Y-%m-%d'))
    rules = [
            Rule(LxmlLinkExtractor(allow=[url_pattern]), callback= 'parse_news', follow=True)
            ]

    def parse_news(self, response):
       
        item = QqScrapyItem()
        selector = Selector(response)
        #url_pattern2 = r'(\w+)://(\w+)\.qq\.com/a/(\d{8})/(\d+)\.htm'
        #pattern = re.match(url_pattern2, str(response.url))
        #pattern = re.match(self.url_pattern, str(response.url))
        data_from = '搜狐网'
        url = response.url
                
        #cmtId = re.findall(re.compile(r'cmt_id = (\d+);'), str(response.body))[0]
        #comments = 'http://coral.qq.com/' + cmtId
        item['data_from'] = data_from
        item['time'] = selector.xpath('//*[@id="news-time"]/text()').extract()[0].strip()
        
        item['url'] = url
        
        #item['comments'] = {'link' : comments}
        #item['contents'] = {'link' : str(response.url), 'title' : u'', 'passage' : u''}
        item['title'] = selector.xpath('//*[@class="text-title"]/h1/text()').extract()[0].strip()
        content = selector.xpath("//article[@id='mp-editor']")
        item['content'] = content.xpath("string(.)").extract()[0].strip()        
        #contents = [txt.strip() for txt in response.xpath('//article//p/text()').extract()]
        #content = '\n'.join(contents)
        #item['content'] = content
          #只取一年内的新闻
#        lastYear = (datetime.datetime.now()-datetime.timedelta(weeks=52)).strftime('%Y-%m-%d %H:%M:%S')
#        if item['time']<lastYear:
#           return      
        yield item
# -*- coding: utf-8 -*-



