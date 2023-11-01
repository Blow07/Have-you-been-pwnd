from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

account = input("Enter a valid e-mail: ")
service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://haveibeenpwned.com/')

search_bar = driver.find_element("id", "Account")
search_bar.send_keys(account)

search_button = driver.find_element("id", "searchPwnage")
search_button.click()
sleep(3)

try:
    wait = WebDriverWait(driver, 5)  # Attendre jusqu'à 5 secondes
    data = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "pwnedCompanyTitle")))

    description = data.find_element(By.XPATH, "./following-sibling::*")
    compromised = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dataClasses")))

    print("Oh no — pwned!")
    print(description.text)
    print(compromised.text)

except TimeoutException as t:
    print(t)
    print("Good news — no pwnage found!")
except Exception as e:
    print(e)
