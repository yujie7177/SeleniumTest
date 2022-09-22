import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def main():
    # executable_path = "/Users/yujie/Documents/Source/SeleniumTest/selenium_drivers/chromedriver"
    # driver = webdriver.Chrome(executable_path=executable_path)
    executable_path = "/Users/yujie/Documents/Source/SeleniumTest/selenium_drivers/geckodriver"
    driver = webdriver.Firefox(executable_path=executable_path)
    driver.get("https://humanbenchmark.com/tests/reactiontime")

    for i in range(20):
        driver.find_element(By.CSS_SELECTOR, "div.css-42wpoy.e19owgy79").click()

        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.view-go.e18o0sx0.css-saet2v.e19owgy77")))
        driver.find_element(By.CSS_SELECTOR, "div.css-42wpoy.e19owgy79").click()
        try:
            a = driver.find_element(By.CSS_SELECTOR, "div.css-1qvtbrk.e19owgy78 h1 div").text
        except Exception as e:
            a = driver.find_element(By.CSS_SELECTOR, "h1.css-0").text
            driver.find_element(By.CSS_SELECTOR, "button.secondary.css-qm6rs9.e19owgy710").click()
        print(a)

    time.sleep(20)


if __name__ == "__main__":
    main()
