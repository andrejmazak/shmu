from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
d = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=chrome_options)
d.get('http://www.shmu.sk/sk/?page=1')

### Chrome browser - maximized window
##options = webdriver.ChromeOptions()
##options.add_argument('--ignore-ssl-errors=yes')
##options.add_argument('--ignore-certificate-errors')
##options.add_argument("--start-maximized")
##
### newly added
##options.add_argument("--no-sandbox");
##options.add_argument("--disable-dev-shm-usage");
##
###driver = webdriver.Chrome('/usr/bin/chromedriver')
##driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
##driver = webdriver.Chrome(chrome_options=options)
##
### login to BHRx
##driver.get(('http://www.shmu.sk/sk/?page=1'))
##
### Close Webdriver and Chrome browser
##driver.close()
##sleep(2)
##os.system("pkill chromedriver")
##os.system("pkill chromium-browse")
