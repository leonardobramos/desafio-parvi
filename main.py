# -*- coding: iso-8859-1 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


driver = webdriver.Chrome()

driver.get('https://gizmodo.uol.com.br/')

post_elements = driver.find_elements(By.CLASS_NAME, 'list-item')

titles = []
dates = []
summaries = []



for post_element in post_elements[:10]:
    title_element = post_element.find_element(By.CLASS_NAME, 'postHeader')
    date_element = post_element.find_element(By.CSS_SELECTOR, 'span.metaText.metaDate')
    summary_element = post_element.find_element(By.CLASS_NAME, 'postSummary')
    date_text = driver.execute_script("return arguments[0].textContent;", date_element)
    summary_text = driver.execute_script("return arguments[0].textContent;", summary_element)
    titles.append(title_element.text)
    dates.append(date_text.strip())
    summaries.append(summary_text.strip())

driver.quit()

data_dict = {
    'Title: ': titles,
    'Date: ': dates,
    'Summary: ': summaries,
}

df = pd.DataFrame(data_dict)

df.to_csv('data_site.csv', index=False)