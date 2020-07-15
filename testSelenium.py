from selenium import webdriver
import time

#启动浏览器，实例化浏览器
driver = webdriver.Chrome()
#打开百度首页
driver.get('http://www.baidu.com')
#设置窗口大小
driver.set_window_size(480, 800)
#最大化浏览器
# driver.maximize_window()
# #刷新（F5）
driver.refresh()
driver.find_element_by_id('kw').send_keys('自动化怎么做？')
driver.find_element_by_id('su').click()
time.sleep(5)
driver.find_element_by_name('wd').send_keys('')
time.sleep(5)
driver.find_element_by_name('wd').send_keys('刘德华')
driver.find_element_by_id('su').click()

# #后退到上一个页面
# driver.back()
# # #前进到下一个页面
# driver.forward()
#退出
# driver.close()  #关闭当前窗口，不会关闭浏览器驱动
# driver.quit()   #退出所有窗口并关闭浏览器驱动

# title = driver.find_element_by_tag_name('title')
# print(title)