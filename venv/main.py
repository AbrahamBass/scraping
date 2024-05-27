from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Worl"}

def selenium_browser(browser: str):
    if(browser == "chrome"):
        return webdriver.Chrome()
    elif (browser == "edge"):
        service = Service(EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        return webdriver.Edge(service = service, options = options)
    elif (browser == "firefox"):
        return webdriver.Firefox()
    elif (browser == "safari"):
        return webdriver.Safari()
    else:
        return webdriver.Chrome()

@app.get("/scraping/")
async def scraping(browser: str = "chrome", url: str = ""):
    browser_instance = selenium_browser(browser)


    browser_instance.get(url)

    #p: str
    p_elements = browser_instance.find_elements(By.TAG_NAME, 'p')
    #print(p_elements.text)
    #p = p_elements.text


    for p_element in p_elements:
        print("Texto de un párrafo:", p_element.text)



    browser_instance.quit()
    return  ""