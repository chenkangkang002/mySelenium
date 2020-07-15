from selenium import webdriver
import time
'''
实现搜索
'''

driver = webdriver.Chrome()     #实例化浏览器对象
driver.maximize_window()        #浏览器窗口最大化
time.sleep(3)                   #设置等待时间

#实现搜索业务
driver.get('http://www.baidu.com')  #访问百度
time.sleep(3)

# driver.find_element_by_link_text('地图').click()  #选择链接地址
driver.find_element_by_id('kw').send_keys('selenium')    #定位输入框，#输入搜索的数据
time.sleep(3)

driver.set_window_size(488,800)     #设置窗口大小
driver.find_element_by_id('su').click()
time.sleep(3)

# driver.find_element_by_name('wd').click()
# time.sleep(3)

# driver.find_element_by_class_name('s_btn').click()
driver.find_element_by_partial_link_text('(WEB自动化工具)_百度百科').click()

time.sleep(5)
driver.quit()   #关闭所有页面并结束webdriver
