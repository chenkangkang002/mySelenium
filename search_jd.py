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

#重新搜索新商品
driver.find_element(by.ID, 'key').clear()   #清除输入值
driver.find_element(by.ID, 'key').send_keys('小米')   #设置新的搜索值
driver.find_element(by.CSS_SELECTOR, 'div[class="form"] button').click()
time.sleep(3)

#获取第二个商品的价格
driver.find_element(by.CSS_SELECTOR, 'div[id="J_goodsList"] > ul > li:nth-child(2)').click()   #定位第二个商品并点金点击
handles = driver.window_handles #获取所有窗口的句柄
print(handles)
driver.switch_to.window(handles[-1]) #切换窗口到当前窗口
price = driver.find_element(by.XPATH, '//div[@class="dd"]/span/span[2]').text    #定位商品价格获取商品价格
print(price)    #打印商品价格

#加入购物车
driver.find_element(by.ID, 'InitCartUrl').click()
#等待3秒加载完成
time.sleep(5)

#登录
#选择账户登录
# driver.find_element(by.XPATH, '//div[@class="login-form"]/div[2]/a').click()
#driver.find_element(by.ID, 'loginDialogBody')

#查看商品详情
# driver.find_element(by.XPATH, '//div[@id="result"]/div/div/div[2]/div[3]/a[1]').click()
# time.sleep(3)

# #返回第一次进入窗口
# driver._switch_to.window(handles[0])
#
# #重新搜索新商品
# driver.find_element(by.ID, 'key').clear()   #清除输入值
# driver.find_element(by.ID, 'key').send_keys('Adidas')   #设置新的搜索值
# driver.find_element(by.CSS_SELECTOR, 'div[class="form"] button').click()
# time.sleep(3)

handles = driver.window_handles #获取所有窗口的句柄
print(handles)
#点击去购物车结算
driver.find_element(by.ID, 'GotoShoppingCart').click()
#点击去结算，弹出登录框//*[@id="cart-floatbar"]/div/div/div/div[2]/div[4]/div[1]/div/div[1]/a
driver.find_element(by.XPATH, '//a[@class="submit-btn"]').click()

#登录
#选择账户登录
driver.find_element(by.XPATH, '//div[@class="login-form"]/div[2]/a').click()

# driver.find_element(by.ID, 'loginDialogBody')
#关闭浏览器
time.sleep(5)
driver.quit()   #关闭浏览器及驱动
