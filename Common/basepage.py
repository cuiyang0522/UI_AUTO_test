from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    desired_caps = {}
    desired_caps["platformName"] = "Android"
    desired_caps["platformVersion"] = "7.0"
    desired_caps["deviceName"] = "VINLHMB7C0100846"
    desired_caps["appPackage"] = ""
    desired_caps["appActivity"] = ""

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 获取屏幕尺寸
    def get_size(self):
        return self.driver.get_window_size()
    # 向左滑动
    def swipe_left(self,size):
        self.driver.swipe(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1, size["height"]*0.5)
    # 向右滑动
    def swipe_right(self,size):
        self.driver.swipe(size["width"] * 0.1, size["height"] * 0.5, size["width"] * 0.9, size["height"]*0.5)
    # 向上滑动
    def swipe_up(self,size):
        self.driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5, size["height"] * 0.1)
    # 向下滑动
    def swipe_down(self,size):
        self.driver.swipe(size["width"] * 0.5, size["height"] * 0.1, size["width"] * 0.5, size["height"] * 0.9)

    # toast获取
    def get_toastMsg(self,str):
        # Xpath表达式，文本匹配
        loc = '//*[contains(@text,"{}")]'.format(str)
        try:
            WebDriverWait(self.driver,10,0.01).until(EC.presence_of_element_located(MobileBy.XPATH,loc))
            return self.driver.find_element_by_xpath(loc).text
        except:
            logging.exception("没有找到匹配的toast")
            raise

