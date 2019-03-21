from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver  = webdriver.Chrome()
driver.get('http://206.189.215.73:9999/')
 
# Find the element by id
driver.find_element_by_id('name').send_keys('Test Name')
driver.find_element_by_id('email').send_keys('TestName@gmail.com')

# Find hidden elemt and change the value
hidden = driver.find_element_by_id('hidden')
driver.execute_script("arguments[0].setAttribute('value','hidden value')", hidden)

driver.find_element_by_id('sbut').click();
