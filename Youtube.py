from selenium import webdriver 
from pynput.keyboard import Key, Controller
import time

video = str(input("What do u like to watch:"))
url = 'https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin' 
browser = webdriver.Chrome()
browser.get(url)
keyboard = Controller()
email = 'Your email'
password = 'Your password'
#email log in
browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email)
browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
#search for video
time.sleep(2)
browser.find_element_by_xpath('//*[@id="search"]').send_keys(video)
browser.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
time.sleep(1)
browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a').click()
#auto fullscreen
time.sleep(1)
keyboard.press('f')
keyboard.release('f')
