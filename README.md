# WeChatDemo
### Debug 2.0

在spider.py的基础上更新了如下内容,并保存为spider2.0.py：  

1.html代码中所有的data-src替换为src  

	temp_html = requests.get(article_url)  
	temp_html.encoding = 'utf-8'  
	data = temp_html.text  
	html = re.sub(pattern='data-src', repl='src', string=data)  

2.增加了保存html代码到本地的代码，文件名为标题前10个字，处于注释状态，需要使用可删除注释。

	f = open('HTML/'+title[:10]+'.html', 'a+')
	f.write(html)
	f.close()

3.提取正文代码添加了异常处理  

	try:  
	    ps = content.find_all('p')  
	    for i in ps:  
	    	x = i.get_text()  
	    	# if '分享一篇文章' in x:       # 判断文章是否为分享其他文章的类型  
        	# return 'null'  
        	p_list.append(x)  

	    main_content = '\n'.join(p_list)
	except:  
	    return "null"                   #异常则返回null  

4.Test文件夹的文件为测试代码

### Debug 2.1

在spider2.0.py的基础上更新了如下内容，保存文件不变：   
1.增加了重复数据不插入数据库的代码，采用的方法是在原数据库的基础上关于publish_date,article_title建立唯一索引，建立了唯一索引后数据入库时会自动判断是否有重复数据：  

	def create_index():  
	    '''  
	    创建唯一索引  
	    :return:  
	    '''  
	    db = pymysql.connect(host='localhost', user='root', password='12345678', port=3306, db='spider')  
	    cursor = db.cursor()  
	    sql = 'CREATE UNIQUE INDEX unique_index ON wechat_article (publish_date,article_title)'  
	    cursor.execute(sql)  
	    db.close()  
	    log('unique_index索引已创建好')  
	    
2.优化了数据库操作的部分代码  
3.将老版本移至Older Version文件夹管理
