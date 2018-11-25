# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymysql.cursors
import re

from scrapy.conf import settings

all_urls = set()
class QqScrapyPipeline(object):
    
    def process_item(self, item,spider):
        global all_urls
        #去重******************
        #print(all_urls)
        if item['url'] in all_urls:
            print('已经在set中')
            return
        else:
            all_urls.add(item['url'])
        print(len(all_urls))

        host = settings['MYSQL_HOST']
        user = settings['MYSQL_USER']
        psd = settings['MYSQL_PASSWD']
        db = settings['MYSQL_DBNAME']
        c = settings['CHARSET']
        port = settings['MYSQL_PORT']
        #数据库连接
        con=pymysql.connect(host=host,user=user,passwd=psd,db=db,charset=c,port=port)
        #数据库游标
        cue=con.cursor()
        
        # 当前月份 数据表
        tt = re.findall(r'\d+',item['time'])
        table = tt[0]+tt[1]
        
        cue.execute("select count(*) from `%s`"%table +" where url=%s",item['url'])
        result1 = cue.fetchone()
        if result1[0]==0: # 不存在重复值
            try:
                #插入月份表
                cue.execute("insert into `%s` (data_from,url,title,content,time)"%table + "values(%s,%s,%s,%s,%s)", 
                            (item['data_from'],item['url'],item['title'],item['content'],item['time'])) 
                ''' 开始日常更新以后就可以同时插入了，否则插入月份表会有重复
                #插入当天表
                cue.execute("insert into this_day (data_from,url,title,content,time) values(%s,%s,%s,%s,%s)", 
                            (item['data_from'],item['url'],item['title'],item['content'],item['time']))
                #插入当月表
                cue.execute("insert into this_month (data_from,url,title,content,time) values(%s,%s,%s,%s,%s)", 
                            (item['data_from'],item['url'],item['title'],item['content'],item['time']))
                '''
                print('Insert success')
            except Exception as e:
                print('Insert error:',e)
                con.rollback()
            else:
                con.commit()
                
#        cue.execute("select count(*) from this_day where url=%s",item['url'])
#        if cue.fetchone()[0]==0: 
#            try:
#                #插入当天表
#                cue.execute("insert into this_day (data_from,url,title,content,time) values(%s,%s,%s,%s,%s)", 
#                            (item['data_from'],item['url'],item['title'],item['content'],item['time']))
#                print('Insert success')
#            except Exception as e:
#                print('Insert error:',e)
#                con.rollback()
#            else:
#                con.commit()
#        cue.execute("select count(*) from this_month where url=%s",item['url'])
#        if cue.fetchone()[0]==0: 
#            try:
#                #插入当月表
#                cue.execute("insert into this_month (data_from,url,title,content,time) values(%s,%s,%s,%s,%s)", 
#                            (item['data_from'],item['url'],item['title'],item['content'],item['time']))        
#                print('Insert success')
#            except Exception as e:
#                print('Insert error:',e)
#                con.rollback()
#            else:
#                con.commit()
            
        con.close()
        return item