from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
user_name = driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text

driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID,"username").send_keys(user_name)
driver.find_element(By.ID,"password").send_keys("learning")
driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()
