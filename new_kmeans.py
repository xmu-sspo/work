# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 14:47:52 2018

@author: 朱何莹
"""
import sys
import pymysql.cursors
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.manifold import TSNE
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime

# 标题title在数据库中的序号
title_order = 3
# 内容content在数据库中的序号
content_order = 4
# 新闻时间time在数据库中的序号
time_order = 5
# 发布平台data_from在数据库中的序号
platform_oreder = 1
# 类别数
cluster_num = 10
# 标题中的关键字的权重
key_weight = 5
# 聚类中心节点索引列表
center_index = []
# 聚类中心的标题列表
topic = []
# 各个类中包含的数据索引列表
news_list = []
# 各个时段（日期）内新闻条数
# day=1,有效长度为24
# day！=1，有效长度为day
news_number = []
# 新闻平台
platforms = ['新浪网', '腾讯新闻', '搜狐网', '网易', '凤凰网', '新华网', '人民网',
             '中青在线', '北青网', '新京报', '澎湃网', '参考消息网', '环球网', '观察者网']
# 各个平台的新闻条数
platform_number = []



# 连接数据库
def connect_to_db():
    # 连接数据库sspo
    connection = pymysql.Connect(
        host='47.107.57.121',
        port=3306,
        user='root',
        passwd='EC096d4864ae',
        db='sspo',
        charset='utf8'
    )
    return connection

# 从数据库读取数据，并利用jieba进行分词
def load_data(day):
    '''
    从数据库读取数据，并利用jieba进行分词
    :param day: 需要读取的天数
    :return: results:从数据库中读取的数据， dataset：jieba分词后的数据
    '''
    # 连接数据库sspo
    connection = connect_to_db()
    # 数据库里的记录
    results = []
    # 提取出记录的标题（title）和内容（content）
    data = []
    try:
        with connection.cursor() as cursor:
            if day==1:
                # sql_1 = 'select * from this_month where date(time) = curdate();'
                sql_1 = 'select * from this_day'

            else:
                # sql_1 = 'select * from `201810` where DATE_SUB(CURDATE(), INTERVAL ' + str(day) + ' DAY) <= date(time);'
                sql_1 = 'select * from this_month where DATE_SUB(CURDATE(), INTERVAL ' + str(day) + ' DAY) <= date(time);'
            cout_1 = cursor.execute(sql_1)
            # print("新闻条数： "+str(cout_1))
            for row in cursor.fetchall():
                results.append(row)
                data.append(str(row[title_order]) * key_weight + "\n" + str(row[content_order]))
    finally:
        connection.close()

    # 利用jieba进行分词
    for i in range(len(data)):
        seg_list = jieba.cut(data[i], cut_all=False)
        s = " ".join(seg_list)
        data[i] = s

    return results, data

# 利用TfidfVectorizer计算tf-idf,采用自定义的停用词表
def transform(dataset, n_features=1000):
    # 从文件导入停用词表
    stpwrdpath = "D:/莹/大创/舆情监督/中文分词/stopwords.txt"
    stpwrd_dic = open(stpwrdpath, 'r',encoding='utf-8')
    stpwrd_content = stpwrd_dic.read()
    # 将停用词表转换为list
    stpwrdlst = stpwrd_content.splitlines()
    stpwrd_dic.close()

    tfidf_vectorizer = TfidfVectorizer(max_df=0.5, stop_words=stpwrdlst,
                                     max_features=n_features,
                                     min_df=2, use_idf=True)
    tfidf = tfidf_vectorizer.fit_transform(dataset)    # 转为tf-idf
    return tfidf, tfidf_vectorizer

# 聚类结果可视化——tsne，分为10类
def tsne_draw_result(X, labels_, title):
    """
    做出聚类图像，用tsne
    labels_ 是预测标签，是一列
    """
    plt.title(title + " cluster result")

    tsne = TSNE()
    tsne.fit_transform(X)
    tsne = pd.DataFrame(tsne.embedding_)

    r = labels_
    r = pd.DataFrame(r, dtype='int')
    r.columns = ['result']

    labels_unique = np.unique(labels_)
    n_clusters_ = len(labels_unique)

    # 颜色列表
    colors = ['b', 'g', 'r', 'k', 'c', 'm', 'y', 'teal', 'lightpink', 'gold',  # 10
              'lightgreen', 'indigo', '#e24fff', '#524C90', '#845868',  # 15
              'orange', 'lightcoral', 'blueviolet', 'brown', 'burlywood',  # 20
              'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue',  # 25
              'cornsilk', 'crimson', 'cyan', 'lightblue', 'lightcyan',  # 30
              'navy', 'darkgray', 'mediumturquoise', 'olive', 'palegoldenrod',  # 35
              'royalblue', 'rosybrown', 'saddlebrown', 'salmon', 'seagreen',  # 40
              'seashell', 'tomato', 'violet', 'yellowgreen', 'turquoise',  # 45
              'thistle', 'tan', 'springgreen', 'slategray', 'plum',  # 50
              'peru', 'orchid', 'oldlace', 'mistyrose', 'mediumvioletred']  # 55
    for i in range(n_clusters_):
        d = tsne[r['result'] == i]
        plt.scatter(d[0], d[1], color=colors[i])

    # 图例
    label = range(n_clusters_)
    number = int(n_clusters_ / 10 + 1)
    plt.legend(label, loc=2, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.,
               ncol=number)
    plt.show()

# 显示每个聚类中心的关键词
def show_keywords(centers, tfidf_vectorizer, true_k):
    print("Top terms per cluster:")
    order_centroids = centers.argsort()[:, ::-1]
    terms = tfidf_vectorizer.get_feature_names()

    for i in range(true_k):
        print("Cluster %d:" % i, end='')
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind], end='')
        print()

# 将话题添加到topic,并显示
def setTopic(center_list, results):
    for i in range(len(center_list)):
        s = results[center_list[i] - 1][title_order].replace("\n", "")
        topic.append(s)
        # print("Topic %d:" % i, end='')
        # print(s)

# 获取聚类中心在数据集中的索引
def get_cluster_center(X, center):
    # 对于每一个聚类中心
    for i in range(center.shape[0]):
        x = X -center[i]
        x = x**2
        x = np.sum(x, axis=1)
        x = x.tolist()
        index = x.index(min(x))
        center_index.append(index+1)

# 获取各个类中包含的数据索引列表
def setNewsList(labels):
    labels = pd.DataFrame(labels, dtype='int')
    labels.columns = ['result']

    labels_unique = np.unique(labels)
    n_clusters = len(labels_unique)

    for i in range(n_clusters):
        news_index = labels[labels.result == i].index.tolist()
        news_index = [x+1 for x in news_index]
        news_list.append(news_index)

# 获取每个时段（日期）包含的新闻条数以及每个新闻平台包含的新闻条数
def setNewsNumber_PlatformNumber(results, day):
    # 对于每个聚类后的话题
    for i in range(0, len(news_list)):
        # 根据天数对时段计数列表初始化
        if day == 1:
            news_count = [0] * 24
        else:
            news_count = [0] * day
        # 对平台计数列表初始化，长度为新闻平台数
        platform_count = [0] * len(platforms)
        son_news_list = news_list[i]  # 当前话题包含的所有新闻
        # 对每个话题包含的所有新闻进行统计
        for j in range(0, len(news_list[i])):
            r_time = results[son_news_list[j]-1][time_order]    # 当前新闻的发布时间
            # print(i, "\t", r_time, type(r_time))
            if day == 1:
                # print(r_time.hour)
                news_count[r_time.hour] = news_count[r_time.hour] + 1
            else:
                delta = (datetime.datetime.now().date() - r_time.date()).days
                news_count[day - 1 - delta] = news_count[day - 1 - delta] + 1
            # 当前新闻的发布平台
            r_platform = results[son_news_list[j] - 1][platform_oreder]
            platform_count[platforms.index(r_platform)] = platform_count[platforms.index(r_platform)] + 1
        news_number.append(news_count)
        platform_number.append(platform_count)

# 获取每个平台包含的新闻条数
def setPlatformNumber(results):
    # 对于每个话题
    for i in range(0, len(news_list)):
        platform_count = [0] * len(platforms)
        # 该话题包含的所有新闻
        for j in range(0, len(news_list[i])):
            son_news_list = news_list[i]
            r_platform = results[son_news_list[j]-1][platform_oreder]
            platform_count[platforms.index(r_platform)] = platform_count[platforms.index(r_platform)] + 1
        platform_number.append(platform_count)


# k-means聚类算法
def kmeans(X, vectorizer, true_k=10, minibatch=False, showLable=False):
    X = X.toarray()
    # 使用采样数据还是原始数据训练k-means，
    if minibatch:
        km = MiniBatchKMeans(n_clusters=true_k, init='k-means++', n_init=10,
                             init_size=1000, batch_size=1024, verbose=False)
    else:
        km = KMeans(n_clusters=true_k, init='k-means++', max_iter=300, n_init=10,
                    verbose=False)
    km.fit(X)
    if showLable:
        show_keywords(km.cluster_centers_, vectorizer, true_k)    # 显示每个类的关键词
    label = km.predict(X)
    setNewsList(label)    # 设置每个类中包含的数据的索引
    get_cluster_center(X, km.cluster_centers_)    # 获取每个聚类中心的索引
    # print("center_list", self.center_index)

    # 聚类结果可视化——tsne
    # self.tsne_draw_result(X, label, "kmeans")

# 总流程
def kmeans_cluster(day):
    results, dataset = load_data(day)
    print(len(results))
    tfidf, tfidf_vectorizer = transform(dataset, n_features=500)
    kmeans(tfidf, tfidf_vectorizer, minibatch=False, true_k=cluster_num, showLable=False)
    setNewsNumber_PlatformNumber(results, day)
    setTopic(center_index, results)

# 将聚类结果保存到数据库
def to_database(day):
    # 连接数据库sspo
    connection = connect_to_db()
    # 批量插入数据
    try:
        with connection.cursor() as cursor:
            dt = time.strftime("%Y-%m-%d")

            # 测试时用
            # today = datetime.date.today()  # 今天
            # yesterday = today - datetime.timedelta(days=2)  # 昨天
            # dt = datetime.date.strftime(yesterday, '%Y-%m-%d')
            # print(type(dt), dt)

            if day == 1:
                table_name = "topic_this_day"
            elif day == 3:
                table_name = "topic_three_days"
            elif day == 7:
                table_name = "topic_this_week"
            elif day == 30:
                table_name = "topic_this_month"

            sql_0 = "truncate table " + table_name    # 清空表
            # sql_0 = "delete from " + table_name +" where label=" + str(day) + " and date='" + dt + "'"  # 删除当天上次聚类产生的结果
            cursor.execute(sql_0)

            sql = "insert into " + table_name + "(id,center_index,title,news_list,news_number,platform_number) values" # (%d,%d,'%s','%s','%s',%d)"
            for i in range(0, len(center_index)):
                str_news_list = ",".join([str(x) for x in news_list[i]])
                str_news_number = ",".join([str(x) for x in news_number[i]])
                str_platform_number = ",".join([str(x) for x in platform_number[i]])
                sql += " (" + str(i+1) + "," + str(center_index[i]) + ",'" + str(topic[i]) + "','" + str_news_list + \
                       "', '" + str_news_number + "', '" + str_platform_number + "'),"
            sql = sql[:-1]
            # print(sql)
            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()

if __name__ == '__main__':
    day = sys.argv[1]
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("-----------python begin:", start_time, "----------")
    # day = 30
    print("day =", day)
    kmeans_cluster(day)
    to_database(day)
    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("-----------python end:", end_time, "----------")
