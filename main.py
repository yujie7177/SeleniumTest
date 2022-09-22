from selenium import webdriver
from selenium.webdriver.common.by import By
import time

executable_path = "/Users/yujie/Documents/Source/SeleniumTest/selenium_drivers/chromedriver"
driver = webdriver.Chrome(executable_path=executable_path)

driver.get("https://time.ibm.com/")

time.sleep(5)

driver.quit()
