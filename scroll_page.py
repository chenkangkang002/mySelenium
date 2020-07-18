# #自动滚动
# def scroll_page(driver):
# x = 1
# height = 0
# while x:
#     js1 = 'window.scrollTo(0, %s)' % (height)
#     driver.execute_script(js1)
#     # time.sleep(1)
#     try:
#         ele = driver.find_element(by.XPATH, '//div[@id="J_feeds"]/div/div[1]/div/h3')
#         #elelj = driver.find_element(by.XPATH, '//div[@id="J_footer"]/div[3]/div/p[2]/a[2]')
#         # elelj = driver.find_element(by.XPATH, '//div[@id="J_coupon"]/div[1]/a/h3')
#     except:
#         height = height + 100
#     else:
#         x = False
#         print(ele.text)
#         print('height',height)
