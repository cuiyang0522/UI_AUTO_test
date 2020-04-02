
import time
import os

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
desired_caps = {}
# 支持X5内核应用自动化配置
desired_caps["recreateChromeDriverSessions"] = True
# 平台类型
desired_caps["platformName"] = "Android"
# 平台版本
desired_caps["platformVersion"] = "7.0"
# 设备名称
desired_caps["deviceName"] = "VINLHMB7C0100846"
# app包名
desired_caps["appPackage"] = "com.tencent.mm"
# app入口acitivity
desired_caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
# 重置与否
desired_caps["noReset"] = True

desired_caps["chromeOptions"] = {"androidProcess":"com.tencent.mm.toolsmp"}
desired_caps["browserName"] = ""
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

time.sleep(5)

driver.find_element_by_android_uiautomator('new UiSelector().text(\"发现\")').click()

driver.find_element_by_android_uiautomator('new UiSelector().text(\"搜一搜\")').click()

WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.tencent.mm:id/bfl")))
driver.find_element_by_id("com.tencent.mm:id/bfl").click()

time.sleep(5)

# os.system("adb shell input tap 180 500")
#
# time.sleep(5)

driver.find_element_by_android_uiautomator('new UiSelector().text(\"柠檬班软件测试\")').click()

time.sleep(14)

cons = driver.contexts
print(cons)

driver.switch_to.context("WEBVIEW_com.tencent.mm:toolsmp")

hs = driver.window_handles

print("当前所有窗口：",hs)

