import re
import json
import urllib.request
from urllib.request import urlopen
from urllib import request
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from selenium import webdriver
import socket
import time
def get_driver_url_content(url, encoding='utf-8', timeout=3):
    '''
    使用浏览器获取动态内容
    :param url:         网页url
    :param encoding:    网页编码
    :param timeout:     设置超时
    :return:
    '''
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(timeout)
    bsObj = BeautifulSoup(driver.page_source, 'html.parser', from_encoding=encoding)
    driver.close()
    return bsObj
'''
只能够爬取静态页面
def getPage(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    req = urllib.request.Request(url, headers=header)
    return urllib.request.urlopen(req).read().decode('utf-8')
'''
def parsePage(s):
    com = re.compile(
        '<li class="rank-item.*?">.*?<i.*?>(?P<rank_num>\d+)</i>.*?<a.*?/BV(?P<BV_num>.*?)" target="_blank" title="(?P<title>.*?)播放'
        , re.S)
    ret = com.finditer(str(s))
    for i in ret:
        yield {
            "排行": i.group("rank_num"),
            "BV号": i.group("BV_num"),
            "标题": i.group("title"),
        }
 
def main(channel,zone):
    url = 'https://www.bilibili.com/v/%s/%s#/' % (channel,zone)
    response_html = get_driver_url_content(url)
    print(response_html)
    ret = parsePage(response_html)
    print(ret)
    f = open("%s_%s_rank" % (channel,zone), "w", encoding="utf8")

    for obj in ret:
        print(obj)
        data = str(obj)
        f.write(data + "\n")

channel = input('请输入频道:')
zone = input('请输入分区:')

if __name__ == '__main__':
    main(channel,zone)