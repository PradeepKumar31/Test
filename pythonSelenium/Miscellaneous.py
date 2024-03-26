from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("-- ignore-certificate-errors")  # in order to ignore your browser is not safe warnings and directly click on advanced and proceed anyway

service_obj = Service()
driver = webdriver.Chrome(service=service_obj,options=chrome_options)
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")
#driver.get_screenshot_as_file("/Users/pradeepkumar/Documents/screenshot.png")

