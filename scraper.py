from selenium import webdriver

from getpass import getpass

from selenium.webdriver.common.action_chains import ActionChains

username=input("Enter the username")

password=getpass("Enter the password")

driver=webdriver.Chrome()

driver.get("https://www.amazon.in")

SignIn_button = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')
SignIn_button.click()

username_textbox = driver.find_element_by_id("ap_email")

username_textbox.send_keys(username)

Continue_button = driver.find_element_by_id("continue")

Continue_button.submit()

password_textbox = driver.find_element_by_id("ap_password")

password_textbox.send_keys(password)

SignIn_button = driver.find_element_by_id("auth-signin-button-announce")

SignIn_button.submit()
