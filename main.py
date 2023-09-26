from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def brownser(url):
    driver = webdriver.Chrome()

    driver.get(url)

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"
    time.sleep(40)

    # driver.quit()

if __name__ == "__main__":
    url = 'https://www.selenium.dev/selenium/web/web-form.html'
    brownser(url)