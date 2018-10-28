# -*- coding: gb2312 -*-

import pymysql

db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='spider2')
cursor = db.cursor()

sql = 'INSERT INTO wechat_article(publish_date,article_title,wechat_id,article_url,cover_img,article_content,article_html,img_counts) values(%s, %s, %s, %s, %s, %s, %s, %s)'
sql1 = 'SELECT id FROM wechat_article ORDER BY id DESC LIMIT 1'
sql2 = 'SELECT count(*) FROM wechat_article'

sql4 = 'CREATE TABLE IF NOT EXISTS wechat_article(id INT UNSIGNED AUTO_INCREMENT,publish_date VARCHAR(20) NOT NULL,article_title VARCHAR(200) NOT NULL,wechat_id VARCHAR(20) NOT NULL,article_url TEXT NOT NULL,cover_img TEXT NOT NULL,article_content TEXT,article_html MEDIUMTEXT NOT NULL,img_counts INT,PRIMARY KEY (id))'


date = '2018-10-15'
title = 'title'
wechat_id = 'wechat'
article_url = "http://mp.weixin.qq.com/s?timestamp=1540454749&src=3&ver=1&signature=1TUTYKR7Letc77bXj9VGaYZesLXThbZ*eadyeUHKabW-t9LG9XihqVBiFfrreddUUE6kfRAYii3c31JmdBPcwEqENmPv-*IFREYS0ArB0CqSjzz0ATOT7ADfc1X2vyXGTxVrCKPwhArB2S7wfnaCTf6KOD7VY0mSHtebSq382fc="
pic = "http://mp.weixin.qq.com/s?timestamp=1540454749&src=3&ver=1&signature=1TUTYKR7Letc77bXj9VGaYZesLXThbZ*eadyeUHKabW-t9LG9XihqVBiFfrreddUUE6kfRAYii3c31JmdBPcwEqENmPv-*IFREYS0ArB0CqSjzz0ATOT7ADfc1X2vyXGTxVrCKPwhArB2S7wfnaCTf6KOD7VY0mSHtebSq382fc="
content = "点击空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 天饿和和 56和 53 和 5和也 天你 天你  儿童你 你 那样太阳能 叶檀 太阳能 一头牛也你 天你天你天你退一步天你一头牛也你 你 一头牛天一年饿你额头一年 饿你饿天你饿天那样饿太阳能 儿童一年 饿一年 饿一年  一年 你  你太阳能 儿童也能 一头牛 额头一年儿童天也 天你嗯呢 你 你你你嗯讨厌也你一年饿也你你那天 你你那样那样那样你那天那样那样你你也那样"
html = "点击空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 点击妇女空高开乖乖热个人个人提供任天堂如火如荼 图图图  天 给5天 还和和 人挺好人和让他和和 "
img_counts = 3

article_id = 2
img_url = 'http://mp.weixin.qq.com/s?timestamp=1540454749&src=3&ver=1&signature=1TUTYKR7Letc77bXj9VGaYZesLXThbZ*eadyeUHKabW-t9LG9XihqVBiFfrreddUUE6kfRAYii3c31JmdBPcwEqENmPv-*IFREYS0ArB0CqSjzz0ATOT7ADfc1X2vyXGTxVrCKPwhArB2S7wfnaCTf6KOD7VY0mSHtebSq382fc='
seq = 3


sql5 = 'INSERT INTO wechat_img(article_id,img_url,sequence_number) values(%s, %s,%s)'

cursor.execute(sql1)
exist_count = cursor.fetchone()
if cursor.fetchone() == None:
    new_id = 3
else:
    cursor.execute(sql2)
    data = cursor.fetchone()
    new_id = data[0] +1   # 新爬取文章的id

# try:
#     cursor.execute(sql5, (article_id, img_url, seq))
#     db.commit()
#     print(u'文章入库成功')
# except:
#     db.rollback()
#     print(u'文章入库不成功')

try:
    cursor.execute(sql, (date, title, wechat_id, article_url, pic, content, html, img_counts))
    db.commit()
    print(u'文章入库成功')
except:
    db.rollback()
    print(u'文章入库不成功')

#cursor.execute(sql)
# print(new_id)
# print(new_id)

db.close()