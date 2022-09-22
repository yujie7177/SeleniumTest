import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    executable_path = "/Users/yujie/Documents/Source/SeleniumTest/selenium_drivers/chromedriver"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get("https://humanbenchmark.com/tests/typing")

    words = driver.find_elements(By.CSS_SELECTOR, "div.letters.notranslate span")
    for i in range(len(words)):
        word = words[i].text
        if word == '':
            word = ' '
        driver.find_element(By.CSS_SELECTOR, "div.letters.notranslate").send_keys(word)
    time.sleep(10)


if __name__ == "__main__":
    main()
