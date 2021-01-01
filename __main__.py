from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from helpers import reader, downloader, login
from time import sleep
from random import randint
import os


if __name__ == '__main__':
	# read config.json file
	config = reader()

	options = Options()

	pathname = os.path.expanduser(config['download_location'])
	if not os.path.exists(pathname):
		os.makedirs(pathname)

	options.add_experimental_option('prefs', {
		'download.default_directory': pathname
	})

	# open a new browser
	global driver
	driver = Chrome(options=options)

	# sets a sticky timeout to implicitly wait for an element to be found
	driver.implicitly_wait(30)

	# login into Envato
	login(driver, config)

	# sleep to prevent issues with the server
	sleep(randint(3, 5))

	# start downloading freebies items
	downloader(driver)

	# closes all browser windows and ends driver's session.
	driver.quit()