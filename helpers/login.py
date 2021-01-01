from time import sleep
from random import randint


def login(driver, config):
	# open Envato login page
	driver.get('https://elements.envato.com/sign-in')

	# some shut-eye :)
	sleep(randint(3, 5))

	# find username & password fields and set their input
	username = driver.find_element_by_name('username')
	username.send_keys(config['username'])
	password = driver.find_element_by_name('password')
	password.send_keys(config['password'])

	# get the login button & click
	submit = driver.find_element_by_css_selector('#app > div._2hNSIZS9 > main > div > div > div._2MG0CV8a > div > div > div > form > button')
	submit.click()