# coding: utf-8

import re
import os
import time
import pymysql
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from pyquery import PyQuery as pq

class Spider:
    def __init__(self, wechat_ids):
        '''
        构造函数，根据公众号微信号获取对应文章的发布时间、文章标题, 文章链接等信息
        :param
        '''
        self.wechat_ids = wechat_ids

        # 请求头
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

        # 超时时长
        self.timeout = 5

        # 爬虫模拟在一个request.session中完成
        self.session = requests.Session()

        # 连接数据库
        self.db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='spider2')
        self.cursor = self.db.cursor()


    def log(self,msg):
        '''
        日志函数
        :param msg: 日志信息
        :return:
        '''
        print(u'%s: %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), msg))

    def get_infos(self):

        for wechat_id in self.wechat_ids:


            self.log(u'公众号为：%s' % wechat_id)

            # 搜索url
            search_url = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query=' + wechat_id
            search_html = self.session.get(search_url,headers=self.headers, timeout=self.timeout).content

            #获取公众号URL
            doc = pq(search_html)
            wechat_url = doc('div[class=txt-box]')('p[class=tit]')('a').attr('href')
            self.log(u'公众号url：%s' % wechat_url)

            # 获取html
            browser = webdriver.Chrome()
            browser.get(wechat_url)
            time.sleep(2)
            wechat_html = browser.execute_script("return document.documentElement.outerHTML")
            browser.close()

            # 检测是否被限制访问
            if pq(wechat_html)('#verify_change').text() != '':
                self.log(u'已限制访问，请稍后再试')

            else:
                # 获取发布时间，标题，首图，URL
                doc = pq(wechat_html)
                articles_list = doc('div[class="weui_media_box appmsg"]')
                articlesLength = len(articles_list)
                self.log(u'抓到文章%s篇' % articlesLength)

                if articles_list:
                    index = 0

                    for article in articles_list.items():

                        self.log('')
                        self.log('正在爬取(%s/%s)' % (index, articlesLength))
                        index += 1

                        # 获取标题
                        title = article('h4[class="weui_media_title"]').text().strip()
                        self.log(u'标题： %s' % title)

                        # 创建标题前五个字命名的文件夹
                        # if not os.path.exists(title[:10]):
                        #     os.makedirs(title[:10])
                        # path = os.getcwd()+ '/' + title[:10] +'/'
                        # print(path)


                        # 获取文章发表时间
                        # date = article('.weui_media_extra_info').text().strip()
                        # date = article('p[class="weui_media_extra_info"]').text().strip()
                        temp_date = article('p[class="weui_media_extra_info"]').text().strip()
                        if temp_date.endswith("原创"):
                            date = temp_date.replace('原创','')
                        else:
                            date = temp_date
                        self.log(u'发表时间： %s' % date)

                        # 获取标题对应的地址
                        temp_url = article('h4[class="weui_media_title"]').attr('hrefs')
                        # 存在某些推文的临时链接为完整链接，判断是否需要拼接
                        if temp_url.startswith('http://mp.weixin.qq.com'):
                            article_url = temp_url
                        else:
                            article_url = 'http://mp.weixin.qq.com' + temp_url
                        self.log(u'地址： %s' % article_url)

                        # 获取封面图片
                        cover = article('.weui_media_hd').attr('style')

                        pic = re.compile(r'background-image:url(.+)')
                        rs = pic.findall(cover)
                        if len(rs) > 0:
                            pic = rs[0].replace('(', '')
                            pic = pic.replace(')', '')
                            #self.log(u'封面图片：%s ' % pic)

                        # 获取正文内容
                        if title == "分享图片":     # 判断文章是否是为分享图片的类型
                            content = "null"
                        else:
                            content = self.get_atticle_info(article_url)

                        #print(content)

                        # 获取文章图片数量
                        img_counts = self.get_article_img(article_url)

                            # 下载图片到本地
                            # data = requests.get(img,headers=self.headers)
                            # fp = open(path+img_url[-15:],'wb')
                            # fp.write(data.content)
                            # fp.close()
                        # print(imgs)

                        # 获取html代码
                        html = requests.get(article_url)
                        html.encoding = 'utf-8'

                        # 保存数据到数据库
                        sql5 = 'INSERT INTO wechat_article(publish_date,article_title,wechat_id,article_url,cover_img,article_content,article_html,img_counts) values(%s, %s, %s, %s, %s, %s, %s, %s)'                        # 推文为分享其他文章则不入库
                        if content != 'null':
                            try:
                                self.cursor.execute(sql5,(date, title, wechat_id, article_url, pic, content, html.text, img_counts))
                                self.db.commit()
                                self.log(u'文章入库成功')
                            except:
                                self.db.rollback()
                                self.log(u'文章入库不成功')

                        #time.sleep(1)

        self.db.close()
        Spider.log("爬虫已完成任务 %s" % wechat_id[-1])

    def get_atticle_info(self,url):
        '''
        获取文章详细内容
        :param url:
        :return:
        '''
        html = requests.get(url,headers=self.headers)
        soup = BeautifulSoup(html.text,"lxml")
        content = soup.find('div', id='img-content')
        temp_contents = re.findall('此(.*?)无法查看', html.text, re.S)

        if len(temp_contents) > 0:
            if '内容因违规' in temp_contents[0]:
                return 'null'

        p_list = []

        ps = content.find_all('p')
        for i in ps:
            x = i.get_text()
            if '分享一篇文章' in x:       # 判断文章是否为分享其他文章的类型
                return 'null'
            p_list.append(x)

        main_content = '\n'.join(p_list)

        return main_content

    def get_article_img(self,url):
        '''
        获取文章图片
        :param url:
        :return:
        '''
        res = requests.get(url)
        if res.status_code == 200:
            contents = re.findall('data-src="(.*?)"', res.text, re.S)

        sql1 = 'SELECT count(*) FROM wechat_article'
        sql2 = 'SELECT id FROM wechat_article ORDER BY id DESC LIMIT 1'
        sql3 = 'INSERT INTO wechat_img(article_id,img_url,sequence_number) values(%s, %s, %s)'
        self.cursor.execute(sql1)
        #exist_count = self.cursor.fetchone()
        if self.cursor.fetchone() == None:
            new_id = 3
        else:
            self.cursor.execute(sql2)
            data = self.cursor.fetchone()
            new_id = data[0] +1         # 新爬取文章的id
        sequence_num = 0

        for img_url in contents:
            if img_url.endswith('jpg') or img_url.endswith('jpeg') or img_url.endswith('gif') or img_url.endswith('png'):
                sequence_num += 1
                try:
                    self.cursor.execute(sql3,(new_id, img_url, sequence_num))
                    self.db.commit()
                    self.log(u'图片入库成功')
                except:
                    self.db.rollback()
                    self.log(u'图片入库不成功')
        return sequence_num

if __name__ == '__main__':

    id = {
        'type':'tech',
        'tech':['CSDN','AppSo', '互联网思维'],
        'news':['人民日报','新华社','央视新闻']
    }

    type = id['type']
    for info in id[type]:
        print(info)

    ids = [ 'CSDN','AppSo', '互联网思维', '腾讯科技', '运营商头条', '新智元', '大数据文摘', '科技最前线', '最黑科技', '钱皓频道', '制造原理']

    Spider(ids).get_infos()

