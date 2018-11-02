# -*- coding: gb2312 -*-
import pymysql
import time


def log(msg):
    '''
    日志函数
    :param msg: 日志信息
    :return:
    '''
    print(u'%s: %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), msg))

def create_databases():
    '''
    创建数据库
    :return:
    '''
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306)
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE spider_test DEFAULT CHARACTER SET UTF8MB4")
    db.close()


def create_tables():
    '''
    创建表
    :return:
    '''
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='spider_test')
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS wechat_article(id INT UNSIGNED AUTO_INCREMENT,publish_date VARCHAR(20) NOT NULL,article_title VARCHAR(200) NOT NULL,wechat_id VARCHAR(20) NOT NULL,article_url TEXT NOT NULL,times VARCHAR(50) NOT NULL,PRIMARY KEY (id))'
    #,UNIQUE KEY ac_uq (article_content)
    cursor.execute(sql)
    db.close()

def create_index():
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='spider_test')
    cursor = db.cursor()
    sql = 'CREATE UNIQUE INDEX index_name ON wechat_article (publish_date,article_title)'
    cursor.execute(sql)
    db.close()

def delete_table():
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='spider_test')
    cursor = db.cursor()
    sql = 'DROP TABLE wechat_article'
    confirm = input('确定删除wechat_article表？Y/N')
    while 1:
        if confirm == 'Y':
            cursor.execute(sql)
            log('wechat_article表已删除')
            return
        elif confirm == 'N':
            log('取消删除wechat_article表')
            return
        else:
            log('输入有误！')
            confirm = input('确定删除wechat_article表？Y/N')
    db.close()

def delete_database():
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='spider_test')
    cursor = db.cursor()
    sql = 'DROP DATABASE spider_test'
    confirm = input('确定删除spider数据库？Y/N')
    while 1:
        if confirm == 'Y':
            cursor.execute(sql)
            log('spider数据库已删除')
            return
        elif confirm == 'N':
            log('取消删除spider数据库')
            return
        else:
            log('输入有误！')
            confirm = input('确定删除spider数据库？Y/N')
    db.close()

if __name__ == '__main__':


    while 1:
        print('1-创建数据库  |  2-创建数据表  |  3-建立唯一索引')
        print('4-删除数据库  |  5-删除数据表  |  0-退出')
        choose = input('请选择：')
        if choose == '1':
            create_databases()

        elif choose == "2":
            create_tables()

        elif choose == "3":
            create_index()

        elif choose == "4":
            delete_database()

        elif choose == "5":
            delete_table()

        elif choose == '0':
            break;
        else:
            print("选择有误")