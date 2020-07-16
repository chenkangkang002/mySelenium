'''
自动化-ecshop后台添加会员
'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.select import Select as select
import get_name_email as gne

#实例化浏览器对象
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)

#参数
user = 'chenkang'
pwd = 'chenkang123'

username = gne.getUsername()
email = gne.getEmail()

upwd = username
ucpwd = username
msn = '123456@hotmail.com'
qq = '411052590'
call1 = '2558888888'
call2 = '255999999'
phone = '15885537820'

url = 'http://localhost/upload/admin/privilege.php?act=login'

#进入后台登录页面
driver.get(url = url)
time.sleep(2)

#登录后台
driver.find_element(by.NAME, 'username').send_keys(user)#输入用户名
driver.find_element(by.NAME, 'password').send_keys(pwd)    #输入密码
driver.find_element(by.CLASS_NAME, 'button').click()   #点击【进入管理中心】

#跳出frame
# driver.switch_to.parent_frame() #跳到上一层
driver.switch_to.default_content()  #跳回主文档，最外层
#进入frame
driver.switch_to.frame('menu-frame')

#点击【会员管理】//*[@id="menu-ul"]/li[7]
driver.find_element(by.XPATH, '//ul[@id="menu-ul"]/li[7]').click()
time.sleep(1)
#点击【添加会员】
driver.find_element(by.XPATH, '//ul[@id="menu-ul"]/li[7]/ul/li[2]/a').click()

#切换frame
driver.switch_to.default_content()  #跳回主文档，最外层
driver.switch_to.frame('main-frame')

#注册会员
driver.find_element(by.NAME, 'username').send_keys(username)#输入用户名
driver.find_element(by.NAME, 'email').send_keys(email)#输入email
driver.find_element(by.NAME, 'password').send_keys(upwd)#输入密码
driver.find_element(by.NAME, 'confirm_password').send_keys(ucpwd)#输入确认密码
driver.find_element(by.XPATH, '/html/body/div[1]/form/table/tbody/tr[14]/td/input[1]').click()#点击【确定】
time.sleep(5)

#编辑会员信息//*[@id="listDiv"]/table/tbody/tr[3]/td[10]/a[1]/img
driver.find_element(by.XPATH, '//div[@id="listDiv"]/table/tbody/tr[3]/td[10]/a[1]/img').click()#点击【编辑】

#获取新的email
newemail = gne.getEmail()

#修改email
driver.find_element(by.NAME, 'email').clear()#清除原信息
driver.find_element(by.NAME, 'email').send_keys(newemail)
driver.find_element(by.XPATH, '/html/body/div[1]/form/table/tbody/tr[18]/td/input[1]').click()#点击【确定】
time.sleep(5)

#查看收货地址
driver.find_element(by.XPATH, '//div[@id="listDiv"]/table/tbody/tr[3]/td[10]/a[2]/img').click()#点击【查看收货地址】
time.sleep(1)
driver.back()
time.sleep(5)

#切换frame
driver.switch_to.default_content()  #跳回主文档，最外层
driver.switch_to.frame('main-frame')

#查看订单//*[@id="listDiv"]/table/tbody/tr[3]/td[10]/a[3]/img
driver.find_element(by.XPATH, '//div[@id="listDiv"]/table/tbody/tr[3]/td[10]/a[3]/img').click()#点击【查看订单】
time.sleep(3)
driver.back()
time.sleep(5)

#切换frame
driver.switch_to.default_content()  #跳回主文档，最外层
driver.switch_to.frame('main-frame')

# #查看账目明细
driver.find_element(by.XPATH, '//div[@id="listDiv"]/table/tbody/tr[3]/td[10]/a[4]/img').click()#点击【查看账目明细】
time.sleep(3)
driver.back()
time.sleep(5)

#切换frame
driver.switch_to.default_content()  #跳回主文档，最外层
driver.switch_to.frame('main-frame')

#移除会员
driver.find_element(by.XPATH, '//div[@id="listDiv"]/table/tbody/tr[3]/td[10]/a[5]/img').click()#点击【移除会员】
#接受accept或取消dismiss，text：返回alert/confirm/prompt中的文字信息
#send_keys(keysToSend)：发送文本至警告框。 keysToSend：将文本发送至警告框。
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)


#关闭页面并退出驱动
time.sleep(3)
driver.quit()