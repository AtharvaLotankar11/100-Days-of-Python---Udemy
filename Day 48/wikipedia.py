from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

#Navigate to Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#Hone in on anchor tag using CSS Selectors
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()

#Find Elements by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

#Find the "Search" <input by Name
search = driver.find_element(By.NAME, value="search")

#Sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER)

