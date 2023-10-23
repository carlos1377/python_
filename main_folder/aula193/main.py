# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

from pathlib import Path
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=str(CHROME_DRIVER),)

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10
    options = ('--headless', )
    browser = make_chrome_browser(*options)

    browser.get('https://google.com.br')

    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    search_input.send_keys('bitcoin')
    search_input.send_keys(Keys.ENTER)

    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    bitcoin = results.find_element(By.CLASS_NAME, 'pclqee')

    print(bitcoin.text)

    sleep(TIME_TO_WAIT)
