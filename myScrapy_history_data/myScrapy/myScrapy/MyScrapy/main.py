# -*- coding: utf-8 -*-

import sys
import os
from scrapy import cmdline

fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
ffpath = os.path.abspath(os.path.join(fpath,".."))
sys.path.append(ffpath)


#cmdline.execute("scrapy crawl InfzmSpider".split())
cmdline.execute("scrapy crawl HuanqiuSpider".split())
cmdline.execute("scrapy crawl GuanchaSpider".split())
cmdline.execute("scrapy crawl SinaSpider".split())
cmdline.execute("scrapy crawl BjnewsSpider".split())
