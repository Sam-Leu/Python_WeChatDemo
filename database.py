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
    cursor.execute("CREATE DATABASE bee_database DEFAULT CHARACTER SET UTF8MB4")
    db.close()
    log('bee_database���ݿ��Ѵ�����')


def create_tables():
    '''
    ������
    :return:
    '''
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='bee_database')
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS wechat_article(id INT UNSIGNED AUTO_INCREMENT,publish_date VARCHAR(20) NOT NULL,article_title VARCHAR(200) NOT NULL,wechat_id VARCHAR(20) NOT NULL,article_url TEXT NOT NULL,cover_img TEXT NOT NULL,article_content TEXT,article_img TEXT,article_html MEDIUMTEXT NOT NULL,PRIMARY KEY (id))'
    cursor.execute(sql)
    db.close()
    log('wechat_article���Ѵ�����')


def create_index():
    '''
    ����Ψһ����
    :return:
    '''
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='bee_database')
    cursor = db.cursor()
    sql = 'CREATE UNIQUE INDEX unique_index ON wechat_article (publish_date,article_title)'
    cursor.execute(sql)
    db.close()
    log('unique_index�����Ѵ�����')

def delete_database():
    '''
    ɾ�����ݿ�
    :return:
    '''
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='bee_database')
    cursor = db.cursor()
    sql = 'DROP DATABASE bee_database'
    confirm = input('ȷ��ɾ��bee_database���ݿ⣿Y/N:')
    while 1:
        if confirm == 'Y':
            cursor.execute(sql)
            log('bee_database���ݿ���ɾ��')
            return
        elif confirm == 'N':
            log('ȡ��ɾ��bee_database���ݿ�')
            return
        else:
            log('��������')
            confirm = input('ȷ��ɾ��bee_database���ݿ⣿Y/N:')
    db.close()

def delete_table():
    '''
    ɾ����
    :return:
    '''
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='bee_database')
    cursor = db.cursor()
    sql = 'DROP TABLE wechat_article'
    confirm = input('ȷ��ɾ��wechat_article��Y/N:')
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
            confirm = input('ȷ��ɾ��wechat_article��Y/N:')
    db.close()

if __name__ == '__main__':

    while 1:
        print('\n1-�������ݿ�  |  2-�������ݱ�  |  3-����Ψһ����')
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