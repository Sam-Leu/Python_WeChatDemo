# coding: utf-8

from pyquery import PyQuery as pq
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pymysql
import time
import re
import os

class Spider:
    def __init__(self, wechat_id):
        '''
        构造函数，根据公众号微信号获取对应文章的发布时间、文章标题, 文章链接等信息
        :param
        '''
        self.wechat_id = wechat_id

        # 请求头
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

        # 搜索url
        self.search_url = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query='+wechat_id

        # 超时时长
        self.timeout = 5

        # 爬虫模拟在一个request.session中完成
        self.session = requests.Session()


    def log(self,msg):
        '''
        日志函数
        :param msg: 日志信息
        :return:
        '''
        print(u'%s: %s' % (time.strftime('%Y-%m-%d %H-%M-%S'), msg))

    def get_url(self):

        self.log(u'公众号微信号为：%s' % self.wechat_id)

        search_html = self.session.get(self.search_url,headers=self.headers, timeout=self.timeout).content

        #获取公众号URL
        doc = pq(search_html)
        wechat_url = doc('div[class=txt-box]')('p[class=tit]')('a').attr('href')
        self.log(u'公众号url：%s' % wechat_url)

        # 获取html
        browser = webdriver.Chrome()
        browser.get(wechat_url)
        time.sleep(3)
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
                    if not os.path.exists(title[:10]):
                        os.makedirs(title[:10])
                    path = os.getcwd()+ '/' + title[:10] +'/'
                    print(path)


                    # 获取文章发表时间
                    # date = article('.weui_media_extra_info').text().strip()
                    date = article('p[class="weui_media_extra_info"]').text().strip()
                    self.log(u'发表时间： %s' % date)

                    # 获取标题对应的地址
                    article_url = 'http://mp.weixin.qq.com' + article('h4[class="weui_media_title"]').attr('hrefs')
                    self.log(u'地址： %s' % article_url)

                    # 获取封面图片
                    cover = article('.weui_media_hd').attr('style')

                    pic = re.compile(r'background-image:url(.+)')
                    rs = pic.findall(cover)
                    if len(rs) > 0:
                        pic = rs[0].replace('(', '')
                        pic = pic.replace(')', '')
                        self.log(u'封面图片：%s ' % pic)

                    # 获取正文内容
                    content = self.get_atticle_info(article_url)
                    print(content)
                    time.sleep(1)

                    # 获取文章图片
                    imgs = self.get_article_img(article_url)
                    for img in imgs:
                        if img.endswith('gif'):
                            img_url = img + '.gif'
                        if img.endswith('jpg'):
                            img_url = img + '.jpg'
                        if img.endswith('jpeg'):
                            img_url = img + '.jpeg'
                        if img.endswith('png'):
                            img_url = img + '.png'

                        # 下载图片到本地
                        # data = requests.get(img,headers=self.headers)
                        # fp = open(path+img_url[-15:],'wb')
                        # fp.write(data.content)
                        # fp.close()
                    print(imgs)

                    # 获取html代码
                    html = requests.get(article_url)
                    html.encoding = 'utf-8'

                    # 保存数据到数据库
                    sql = 'INSERT INTO article(date,title,wechat_id,url,cover_img,content,img,html) values(%s, %s, %s, %s, %s, %s, %s, %s)'
                    try:
                        cursor.execute(sql,(date, title, self.wechat_id, article_url, pic, content, imgs[0], html.text))
                        db.commit()
                    except:
                        db.rollback()

                    time.sleep(1)


    def get_atticle_info(self,url):
        '''
        获取文章详细内容
        :param url:
        :return:
        '''
        html = requests.get(url,headers=self.headers)
        soup = BeautifulSoup(html.text,'lxml')
        content = soup.find('div', id='img-content')

        p_list = []
        ps = content.find_all('p')
        for i in ps:
            x = i.get_text()
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

        imgs = []
        for img in contents:
            if img.endswith('jpg') or img.endswith('jpeg') or img.endswith('gif') or img.endswith('png'):
                imgs.append(img)
        return imgs

    def save_in_sql(self):
        return


if __name__ == '__main__':

    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='spider')
    cursor = db.cursor()
    Spider("python6359").get_url()
    db.close()



