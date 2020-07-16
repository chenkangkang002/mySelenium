from selenium import webdriver
import time
'''
实现操控浏览器，进行百度搜索业务
'''

#实例化浏览器对象
driver = webdriver.Chrome()
#设置浏览器最大化
driver.maximize_window()
#设置等待时间5秒
time.sleep(5)
#设置浏览器的大小
driver.set_window_size(480, 800)

#打开浏览器并访问百度
driver.get('http://www.baidu.com')
#设置等待时间，等待页面加载完成5秒
time.sleep(5)

#定位输入框元素并设置搜索值,id
driver.find_element_by_id('kw').send_keys('python')
#定位搜索按钮并设置点击事件,id
driver.find_element_by_id('su').click()
#设置等待时间五秒
time.sleep(5)

#访问淘宝网站
driver.execute_script('window.open("http://www.taobao.com");')
# 切换du到新的窗口
handles = driver.window_handles
print(handles)
driver.switch_to.window(handles[1])
#设置等待时间，等待页面加载五秒
time.sleep(5)

#退回上一个页面
driver.back()
#设置等待时间2秒
time.sleep(2)

#访问京东网站
driver.get('http://www.jd.com')
#等待三秒
time.sleep(3)
#退回上一个页面
driver.back()
#等待两秒
time.sleep(2)
#刷新页面
driver.refresh()
#前进到下一个页面
driver.forward()
time.sleep(2)
#退回上一个页面
driver.back()
#等待三秒
time.sleep(3)

# 切换到原窗口的窗口
driver.switch_to.window(handles[0])

#进入搜索结果详情页面，完全匹配
driver.find_element_by_link_text('python与_从入门到精通')
#退回上一个页面
driver.back()
#等待五秒
time.sleep(5)

#进入搜索结果详情页面，模糊匹配
driver.find_element_by_partial_link_text('程序设计语言) - 百度百科')
#等待三秒
time.sleep(3)

#退回上一个页面
driver.back()
#清除当前输入框数据
driver.find_element_by_id('su').clear()
#设置输入框搜索数据，class
driver.find_element_by_class_name('s_ipt').send_keys('java')
#定位搜索按钮，并设置点击事件
driver.find_element_by_id('su').click()
#等待三秒
time.sleep(3)

#关闭当前页面，不关闭驱动
driver.close()
#关闭驱动
driver.quit()
