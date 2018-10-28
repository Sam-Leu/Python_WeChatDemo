# -*- coding: gb2312 -*-
import pymysql

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
    cursor.execute(sql)
    db.close()

if __name__ == '__main__':

    print('1-�������ݿ�  |  2-������')
    choose = input('��ѡ��')
    if choose == '1':
        create_databases()
    elif choose == "2":
        create_tables()
    else:
        print("ѡ������")