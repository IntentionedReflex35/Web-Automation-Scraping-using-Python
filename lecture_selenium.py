from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # This keeps the browser open

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.wikipedia.org")

search_bar = driver.find_element(by=By.ID, value='searchInput')

search_bar.send_keys("Bayern Munich")

search_btn = driver.find_element(by=By.XPATH, value='//*[@id="search-form"]/fieldset/button/i')

search_btn.click()
