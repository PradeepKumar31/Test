import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# chrome driver - chrome browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

Alist = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

count = len(results)
assert count > 0
Namelist = []
for result in results:
    Namelist.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

assert Alist == Namelist

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

amounts = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
total = 0
for amount in amounts:
    total = int(amount.text) + total
print(total)

Total_Sum = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert total == Total_Sum

discount_price = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)

assert Total_Sum > discount_price






