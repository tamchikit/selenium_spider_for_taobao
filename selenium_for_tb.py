#!usr/bin/env python
#-*-coding:utf-8-*-

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq

browser = webdriver.Firefox()
URL = 'https://s.taobao.com/search?q='
wait = WebDriverWait(browser, 15)
Keyword = input('Please input your keyword: \n')
Maxpage = 10

def getpage(page):
    print('正在爬取第 '+str(page)+' 页\n')
    try:
        url = URL + quote(Keyword)
        browser.get(url)
        print (browser)
        if page>1:
            input = wait.until(Ec.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form > input')))
            button = wait.until(Ec.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            button.click()
        wait.until(Ec.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(Ec.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        getpage(page)

def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)

def main():
    for i in range(1, Maxpage+1):
        getpage(i)
    browser.close()

if __name__ == '__main__':
    main()