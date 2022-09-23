import imp
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


executable_path = "/Users/yujie/Documents/Source/SeleniumTest/selenium_drivers/chromedriver"
driver = webdriver.Chrome(executable_path=executable_path)

driver.get("https://humanbenchmark.com/tests/verbal-memory")

driver.find_element(By.CSS_SELECTOR, "button.css-de05nr.e19owgy710").click()
wordList = []

while True:
    word = driver.find_element(By.CSS_SELECTOR, "div.word").text
    time.sleep(1)
    if word in wordList:
        driver.find_element(By.XPATH, "//div[@class='css-1qvtbrk e19owgy78']/button[1]").click()
    else:
        driver.find_element(By.XPATH, "//div[@class='css-1qvtbrk e19owgy78']/button[2]").click()
        wordList.append(word)


