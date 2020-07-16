from selenium import webdriver
import time
from selenium.webdriver.common.by import By as  by
'''
自动化—京东搜索
'''

#实例化浏览器对象
driver = webdriver.Chrome()
driver.maximize_window()    #窗口最大化
time.sleep(5)   #设置等待加载时间

#打开页面并访问京东
driver.get('http://www.jd.com')
time.sleep(3)

#实现搜索业务
driver.find_element(by.ID, 'key').send_keys('鞋子')   #定位输入框并设置值
driver.find_element(by.XPATH, '//div[@id="search"]/div/div[2]/button').click()  #定位搜索按钮并点击
time.sleep(3)   #等待加载页面完成

url = driver.current_url    #获取当前页面的url
print(url)  #打印到控制台

#关闭浏览器
time.sleep(5)
driver.quit()   #关闭浏览器及驱动