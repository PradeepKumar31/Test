from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chrome driver - chrome browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()

#service_obj = Service('/Users/pradeepkumar/Documents/chromedriver')
#driver = webdriver.Chrome(service=service_obj)
#driver.get("https://rahulshettyacademy.com")
