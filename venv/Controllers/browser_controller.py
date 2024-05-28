from fastapi import Form, HTTPException
from typing import Annotated
from Methods.browser_method import selenium_browser
from selenium.webdriver.common.by import By
from Interfaces.browser_interface import Alone
from selenium.common.exceptions import NoSuchElementException

class Browser_Controller:
    def find_atribute(self, browser: str, page: str, selector: str):
        browser_instance = selenium_browser(browser)
        browser_instance.get(page)


        try:
            element = browser_instance.find_element(By.CSS_SELECTOR, selector)
            browser_instance.quit()
            return Alone(
                text=element.text,
                id=element.get_attribute('id'),
                className=element.get_attribute('class')
            )
        except NoSuchElementException as e:
            browser_instance.quit()
            raise HTTPException(
                status_code=404,
                detail="no such element"
            )



    def all_tags(self, browser: str, page: str, tag: str):
        browser_instance = selenium_browser(browser)
        browser_instance.get(page)

        tags: Alone = list()

        try:
            elements = browser_instance.find_elements(By.TAG_NAME, 'p')

            for element in elements:
                tags.append(
                    Alone(
                    text="",
                    id="element.get_attribute('id')",
                    className="element.get_attribute('class')"
                    )
                )

            browser_instance.quit()

            return  ""

        except NoSuchElementException as e:
            browser_instance.quit()
            raise HTTPException(
                status_code=404,
                detail="no such element"
            )


