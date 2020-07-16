from selenium import webdriver
import time
'''
淘宝搜索
'''

#实例化浏览器对象
driver = webdriver.Chrome()
driver.set_window_size(1500, 800) #设置浏览器窗口大小
time.sleep(3) #等待三秒加载

#打开浏览器页面，访问淘宝
driver.get('http://www.taobao.com')
#等待5秒，页面加载
time.sleep(5)
#定位元素，并设置数据
# driver.find_element_by_xpath('//*[@id="q"]').send_keys('飞机')
# #定位搜索按钮，并设置点击事件
# # driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[1]/div[2]/form/div[1]/button').click()
# driver.find_element_by_xpath('//form[@id="J_TSearchForm"]/div[1]/button').click()
# driver.find_element_by_css_selector('div[class="search-combobox-input-wrap"] input').send_keys('老干妈')
text = driver.find_element_by_css_selector('div[class="search-hots-fline"] :nth-child(1)+a').text
if text == '' :
    print()
    driver.execute_script('alert(没有这个元素);')
else:
    newwindow = 'window.open(\'http://www.taobao.com\');'
    driver.execute_script(newwindow) # driver.execute_script('alert(没有这个元素);')
    text = driver.find_element_by_css_selector('div[class="search-hots-fline"] :nth-child(1)+a').click()
time.sleep(3)
# driver.find_element_by_css_selector('form[action*="search"] button').click()
#切换窗口到当前
handles = driver.window_handles
driver.switch_to.window(handles[1])
time.sleep(3)
#退出浏览器并关闭驱动
driver.quit()
