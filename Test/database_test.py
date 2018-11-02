# -*- coding: gb2312 -*-
import pymysql
import time


def log(msg):
    '''
    ��־����
    :param msg: ��־��Ϣ
    :return:
    '''
    print(u'%s: %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), msg))

def create_databases():
    '''
    �������ݿ�
    :return:
    '''
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306)
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE spider_test DEFAULT CHARACTER SET UTF8MB4")
    db.close()


def create_tables():
    '''
    ������
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
    confirm = input('ȷ��ɾ��wechat_article��Y/N')
    while 1:
        if confirm == 'Y':
            cursor.execute(sql)
            log('wechat_article����ɾ��')
            return
        elif confirm == 'N':
            log('ȡ��ɾ��wechat_article��')
            return
        else:
            log('��������')
            confirm = input('ȷ��ɾ��wechat_article��Y/N')
    db.close()

def delete_database():
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='spider_test')
    cursor = db.cursor()
    sql = 'DROP DATABASE spider_test'
    confirm = input('ȷ��ɾ��spider���ݿ⣿Y/N')
    while 1:
        if confirm == 'Y':
            cursor.execute(sql)
            log('spider���ݿ���ɾ��')
            return
        elif confirm == 'N':
            log('ȡ��ɾ��spider���ݿ�')
            return
        else:
            log('��������')
            confirm = input('ȷ��ɾ��spider���ݿ⣿Y/N')
    db.close()

if __name__ == '__main__':


    while 1:
        print('1-�������ݿ�  |  2-�������ݱ�  |  3-����Ψһ����')
        print('4-ɾ�����ݿ�  |  5-ɾ�����ݱ�  |  0-�˳�')
        choose = input('��ѡ��')
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
            print("ѡ������")