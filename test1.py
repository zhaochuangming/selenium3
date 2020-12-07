#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
cc = webdriver.Chrome()
cc.get("http://www.baidu.com")
print(WebDriverWait(cc,10).until(EC.title_is("百度一下，你就知道")))
