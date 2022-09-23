import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# executable_path = "/Users/yujie/Documents/Source/SeleniumTest/selenium_drivers/geckodriver"
# driver = webdriver.Firefox(executable_path=executable_path)
executable_path = "/Users/yujie/Documents/Source/SeleniumTest/selenium_drivers/chromedriver"
driver = webdriver.Chrome(executable_path=executable_path)
driver.get("https://humanbenchmark.com/tests/chimp")

driver.find_element(By.CSS_SELECTOR, "button.css-de05nr.e19owgy710").click()

while True:
    rows = driver.find_elements(By.XPATH, "//div[@class='css-gmuwbf']/div/div")
    b = []
    for y in range(len(rows)):
        squares = driver.find_elements(By.XPATH, "//div[@class='css-gmuwbf']/div/div[{}]/div".format(y+1))
        for x in range(len(squares)):
            a = driver.find_element(By.XPATH, "//div[@class='css-gmuwbf']/div/div[{}]/div[{}]".format(y+1, x+1)).get_attribute("data-cellnumber")
            if a:
                b.append([int(a), y, x])
    b.sort()
    for i in b:
        driver.find_element(By.XPATH, "//div[@class='css-gmuwbf']/div/div[{}]/div[{}]".format(i[1]+1, i[2]+1)).click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button.css-de05nr.e19owgy710").click()

time.sleep(20)
