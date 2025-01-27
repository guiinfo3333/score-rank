from selenium import webdriver
import drivers
from selenium.webdriver.chrome.options import Options

class Scrapy:
    def __init__(self):
        self.chrome_options = Options()
        # self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument('--disable-dev-shm-usage')

        drivers.install()
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.set_window_size(1080, 878)