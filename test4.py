from selenium import webdriver
from config.find_element import FindElement

class RegisterFunction(object):
    def __init__(self,url):
        self.cc=self.get_cc(url)
    #获取cc并且打开
    def get_cc(self,url):
        cc =webdriver.Chrome()
        cc.get(url)
        cc.maximize_window()
        cc.implicitly_wait(10)
        cc.switch_to.frame(1)
        return cc


    #定位用户信息，获取element
    def get_user_element(self,key):
        find_element = FindElement(self.cc)
        user_element = find_element.get_element(key)
        return user_element

    #运行主程序
    def run_main(self):
        self.get_user_element("u")
        self.cc.implicitly_wait(10)
        self.get_user_element("p")
        self.cc.implicitly_wait(10)
        self.get_user_element("login_button").click()

if __name__ == '__main__':
    register_function=RegisterFunction("https://mail.qq.com/")
    register_function.run_main()