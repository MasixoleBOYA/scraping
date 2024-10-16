import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


#keep window open
options = Options()
options.add_experimental_option("detach", True)

#driver instance
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager(url="https://pypi.python.org/simple/").install()))


# main_url = 'https://tools.sars.gov.za/tradestatsportal/data_download.aspx'


# driver.get("https://www.neuralnine.com/")
# driver.get(main_url)


