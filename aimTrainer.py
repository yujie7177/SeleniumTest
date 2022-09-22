from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

executable_path = "/Users/yujie/Documents/Source/SeleniumTest/selenium_drivers/chromedriver"
driver = webdriver.Chrome(executable_path=executable_path)
driver.get("https://humanbenchmark.com/tests/aim")




for i in range(31):

    mylabel = driver.find_element(By.CSS_SELECTOR, "div.css-1k4dpwl.e6yfngs0 div")
    ActionChains(driver).move_to_element_with_offset(mylabel,0,0).click().perform()


time.sleep(10)