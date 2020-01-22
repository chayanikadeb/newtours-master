#http://newtours.demoaut.com/mercuryregister.php

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='chromedriver/chromedriver_for_79/chromedriver.exe')
driver.get("http://newtours.demoaut.com/mercuryregister.php")
#assert "Welcome: Mercury Tours" in driver.title, "Welcome: Mercury Tours not found"


def fillUpValue(elementName, value):
	element = driver.find_element_by_name(elementName)
	element.clear()
	element.send_keys(value)



fillUpValue("firstName", "Akshay")
fillUpValue("lastName", "Joshi")
fillUpValue("phone", "1234567899")
fillUpValue("userName", "akshay.joshi")
fillUpValue("address1", "Aishwaryam")
fillUpValue("address2", "Courtyard")
fillUpValue("city", "Pune")
fillUpValue("state", "Maharashtra")
fillUpValue("postalCode", "411062")
#fillUpValue("country", "92")
driver.find_element_by_xpath("//select[@name='country']/option[text()='INDIA ']").click()
fillUpValue("email", "akshay.joshi1@gmail.com")
fillUpValue("password", "C0ntinu3")
fillUpValue("confirmPassword", "C0ntinu3")

driver.find_element_by_name("register").click()

time.sleep(20)


#password.send_keys(Keys.RETURN)