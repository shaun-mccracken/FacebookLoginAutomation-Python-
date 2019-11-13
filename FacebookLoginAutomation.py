from selenium import webdriver

username = 'Enter Username'
passowrd = 'Enter Password'

url = 'https://wwww.facebook.com/'

#Enter filepath of chromedriver.exe
driver = webdriver.Chrome("")

#Send url to the webdriver
driver.get(url)

#Locate username and password text fie lds by element id and input corresponding Strings
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(passowrd)

#Locate login submition field 
driver.find_element_by_id('loginbutton').click()