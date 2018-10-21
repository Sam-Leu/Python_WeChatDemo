#encoding=utf-8
import jieba
import pymysql


def cut_word(word):
    '''
    利用jieba库的搜索引擎模式分词
    :param word:
    :return: 分词列表
    '''

    # 搜索引擎模式分词
    seg_list = list(jieba.cut_for_search(word))
    new_list = []

    # 提取大于等于两个词的词语
    for lists in seg_list:
        if len(lists) >= 2:
            new_list.append(lists)

    return new_list


def search_infos(key_words):
    '''
    根据分词查询数据
    :param words:
    :return: 数据列表
    '''
    words = cut_word(key_words)     # 调用分词函数
    infos = []                      # 外层列表，存储检索到的每条推文信息的子列表
    for word in words:
        sql = "SELECT id, article_title FROM wechat_article WHERE article_title LIKE '%" + word + "%'"
        cursor.execute(sql)
        datas = cursor.fetchall()       # 查找所有符合条件的数据

        if len(datas) > 0:

            for data in datas:
                temp_word = '<strong>' + word + '</strong>'         # 添加html标签
                new_data = []                                       # 每条推文信息的子列表
                new_data.append(data[0])                            # 主键id
                new_data.append(data[1].replace(word, temp_word))   # 标题
                infos.append(new_data)                              # 添加数据到外层列表

    for info in infos:
        print(info)
    return infos

if __name__ == '__main__':

    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='spider')
    cursor = db.cursor()
    words = 'goole杀了500个官宣GitHub苹果爬虫程序员脚本祭天！'
    search_infos(words)
    db.close()