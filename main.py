from selenium import webdriver
from selenium.webdriver.common.by import By



def open_site():
    driver = webdriver.Chrome()

    driver.get("https://gizmodo.uol.com.br/")


open_site()