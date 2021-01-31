from selenium import webdriver 
import time

video = str(input("What do u like to watch:"))
url = 'https://www.youtube.com/' 
browser = webdriver.Chrome()
browser.get(url)
email = 'Your email'
password = 'Your password'

browser.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a').click()
browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email)
browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()

time.sleep(2)
browser.find_element_by_xpath('//*[@id="search"]').send_keys(video)
browser.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
time.sleep(2)
browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a').click()

