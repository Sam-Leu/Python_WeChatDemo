# -*- coding: gb2312 -*-
import pymysql

def create_databases():
    '''
    �������ݿ�
    :return:
    '''
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306)
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE spider2 DEFAULT CHARACTER SET UTF8MB4")
    db.close()
    print("�������ݿ�ɹ���")


def create_article_tables():
    '''
    ������
    :return:
    '''
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='spider2')
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS wechat_article(id INT UNSIGNED AUTO_INCREMENT,publish_date VARCHAR(20) NOT NULL,article_title VARCHAR(200) NOT NULL,wechat_id VARCHAR(20) NOT NULL,article_url TEXT NOT NULL,cover_img TEXT NOT NULL,article_content TEXT,article_html MEDIUMTEXT NOT NULL,img_counts INT,PRIMARY KEY (id))'
    cursor.execute(sql)
    db.close()
    print("�������±�ɹ���")

def create_img_tables():
    '''
    ������
    :return:
    '''
    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='spider2')
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS wechat_img(id INT UNSIGNED AUTO_INCREMENT,article_id INT NOT NULL,img_url TEXT NOT NULL,sequence_number INT,PRIMARY KEY (id))'
    cursor.execute(sql)
    db.close()
    print("����ͼƬ��ɹ���")

if __name__ == '__main__':

    print('1-�������ݿ�  |  2-�������±�  |  3-����ͼƬ��  |  0-�˳�')
    while 1:
        choose = input('��ѡ��')
        if choose == "0":
            break;
        elif choose == '1':
            create_databases()
        elif choose == "2":
            create_article_tables()
        elif choose == "3":
            create_img_tables()
        else:
            print("ѡ������")