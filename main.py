# -*- coding: iso-8859-1 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://gizmodo.uol.com.br/')

post_elements = driver.find_elements(By.CLASS_NAME, 'postHeader')

titles = []
dates = []
summaries = []

for post_element in post_elements[:10]:
    # title_element = post_element.find_element(By.CLASS_NAME, 'postTitle')
    date_element = post_element.find_element(By.CLASS_NAME, 'published updated')
    # summary_element = post_element.find_element(By.CLASS_NAME, 'postSummary entry-content')
    # titles.append(title_element.text)
    dates.append(date_element)
    # summaries.append(summary_element)

for _ in range(10):
    print('Title, Date, Resumo.')
    print(titles[_],dates[_],summaries[_])