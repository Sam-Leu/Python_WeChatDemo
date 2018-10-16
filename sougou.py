from selenium import webdriver
from pyquery import PyQuery as pq
import time
driver_sougou = webdriver.Chrome()
#driver_change = webdriver.Chrome()

#driver_sougou.get("http://weixin.sogou.com/")
#driver_sougou.find_element_by_xpath('//*[@id="loginBtn"]').click()
base_url = 'https://mp.weixin.qq.com/'


def get_url_list():
    """获取公众号推文url列表"""
    #account1 = input("请输入公众号名称：")
    account = "差评"
    #driver_sougou.find_element_by_xpath('//*[@id="query"]').send_keys("%s" % account)       #输入公众号
    #driver_sougou.find_element_by_xpath('//*[@id="searchForm"]/div/input[4]').click()       #模拟点击搜索公众号

    driver_sougou.get("https://weixin.sogou.com/weixin?type=1&query="+account)
    time.sleep(1)
    link = driver_sougou.find_element_by_xpath('//*[@class="news-box"]/ul/li[1]/div/div[2]/p/a')      #获取公众号详情页面
    init_url = link.get_attribute('href')
    driver_sougou.get(init_url)     #get公众号详情页面

    print(driver_sougou.current_url)
    print(driver_sougou.page_source)
    html = driver_sougou.page_source
    doc = pq(html)
    items = doc('#weui_msg_card_list .weui_msg_card_bd .weui_media_box appmsg').items()


    for item in items:
        print('2')
        temp_url = item.find('.weui_media_title').attr('hrefs')
        url_list = {
            'url':base_url + temp_url
        }
        print(url_list)

    time.sleep(3)
    driver_sougou.close()





if __name__ == '__main__':
    get_url_list()
