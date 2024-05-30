from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from typing import Union

def add_option(options: Union[webdriver.ChromeOptions, webdriver.EdgeOptions]):
    pass
    options.add_argument('--headless')
    #options.add_argument('--disable-gpu')
    #options.add_argument('--no-sandbox')

def selenium_browser(browser: str = "chrome"):
    if(browser == "chrome"):
        chrome = Service(ChromeDriverManager().install())
        options_chrome = webdriver.ChromeOptions()
        add_option(options_chrome)
        return webdriver.Chrome(service=chrome, options=options_chrome)
    elif (browser == "edge"):
        #edge = Service(EdgeChromiumDriverManager().install())
        options_edge = webdriver.EdgeOptions()
        add_option(options_edge)
        return webdriver.Edge( options = options_edge)
    elif (browser == "firefox"):
        firefox = Service(GeckoDriverManager().install())
        options_firefox = webdriver.FirefoxOptions()
        add_option(options_chrome)
        return webdriver.Firefox(service=firefox, options=options_firefox)