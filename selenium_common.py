'''
初始化Chrome浏览器公共方法
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By as by

#实例化话浏览器Chrome
driver = webdriver.Chrome()
driver.maximize_window()
