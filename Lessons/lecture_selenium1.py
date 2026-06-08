# Saving Browser Sessions As Cookies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pickle  # <-- the library for dumping or saving cookies

service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://practicetestautomation.com/practice-test-login/")

username_field = driver.find_element(by=By.NAME, value="username")
password_field = driver.find_element(by=By.ID, value="password")
submit_button = driver.find_element(by=By.ID, value="submit")

username_field.send_keys("student")
password_field.send_keys("Password123")
submit_button.click()

# Dumping the cookies / Saving
pickle.dump(driver.get_cookies(), open("../cookies.pkl", "wb"))
