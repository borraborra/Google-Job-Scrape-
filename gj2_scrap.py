from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from parsel import Selector

driver = webdriver.Chrome(r"C:\Users\borra\Desktop\ChromeDriver\chromedriver")

driver.get('https://www.google.com/')

search_query = driver.find_element_by_name('q')

search_query.send_keys('software engineer Pittsburgh')

search_query.send_keys(Keys.RETURN)

link_jobs = driver.find_element_by_link_text('100+ more jobs')

link_jobs.click()

search_jp = driver.find_elements_by_xpath('//*[@id="immersive_desktop_root"]/div/div[3]/div[1]/div[1]') #worked! but all print together

for value in search_jp:
    print(value.text)
    print()
