from time import sleep
from random import randint
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def downloader(driver):
	# open freebies page
	driver.get('https://elements.envato.com/free')

	# get all freebies items
	freebies = driver.find_elements_by_css_selector('#app > div:nth-child(1) > div > div._11VygIw6 > div.UFvD2nhw > div > div._3DtYNzm-')

	# open each item in new tab
	action = ActionChains(driver)
	
	for item in freebies:
		action.key_down(Keys.CONTROL).click(item).key_up(Keys.CONTROL)
		
	action.perform()

	# close current tab -> https://elements.envato.com/free
	driver.close()

	# switch between tabs & download items
	tabs = driver.window_handles

	for tab in reversed(tabs):
		driver.switch_to.window(tab)

		# wait for the `Download for Free` button to be clickable & click on it
		button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
			(By.CSS_SELECTOR, '#app > div.TAgl8_az > main > div > div > div._3xSb5jIU > div > div.hNdEXw7_ > button')
		))
		button.click()
	
		# accept terms
		checkbox = driver.find_element_by_css_selector('body > div:nth-child(23) > div > div > div > form > div > div > label > span._3ACMmCBk')
		checkbox.click()

		# find `Download` button & click on it
		download = driver.find_element_by_css_selector('body > div:nth-child(23) > div > div > div > form > div > button')
		download.click()
	
		# some shut-eye :)
		sleep(randint(3, 5))

	# waiting for a download process to complete
	def downloads_done(driver):
		if not driver.current_url.startswith("chrome://downloads"):
			driver.get("chrome://downloads")
		return driver.execute_script("""
				return document.querySelector('downloads-manager')
				.shadowRoot.querySelector('#downloadsList')
				.items.filter(item => item.state === 'COMPLETE')
				.map(item => item.filePath || item.file_path || item.fileUrl || item.file_url);
			""")

	WebDriverWait(driver, 120, 1).until(downloads_done)