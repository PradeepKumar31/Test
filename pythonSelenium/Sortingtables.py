from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
BrowserSortedVeggies = []
#click on column header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

# collect all veggie names -> BrowserSortedveggieList (A,B,C)
VeggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")  # this list contains webElements not text
for ele in VeggieWebElements:
    BrowserSortedVeggies.append(ele.text)

originalBrowserSortedList = BrowserSortedVeggies.copy()

# sort this BrowserSortedveggieList -> newSortedList (A,B,C)
BrowserSortedVeggies.sort()

assert BrowserSortedVeggies == originalBrowserSortedList