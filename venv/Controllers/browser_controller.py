from fastapi import Form, HTTPException
from typing import Annotated
from Methods.browser_method import selenium_browser
from selenium.webdriver.common.by import By
from Interfaces.browser_interface import Alone
from selenium.common.exceptions import NoSuchElementException

class Browser_Controller:
    async def find_atribute(self, browser: Annotated[str, Form()], page: Annotated[str, Form()], selector: Annotated[str, Form()]):
        browser_instance = selenium_browser(browser)
        browser_instance.get(page)

        try:
            element = browser_instance.find_element(By.CSS_SELECTOR, selector)
            return Alone(
                text=element.text,
                id=element.get_attribute('id'),
                className=element.get_attribute('class')
            )
        except NoSuchElementException as e:
            raise HTTPException(
                status_code=404,
                detail="no such element"
            )
        finally:
            browser_instance.quit()


    async def all_tags(self, browser: str, page: str, tag: str):
        browser_instance = selenium_browser(browser)
        browser_instance.get(page)

        tags = list()

        try:
            elements = browser_instance.find_elements(By.TAG_NAME, tag)

            for element in elements:
                append = Alone(
                    text=element.text,
                    id=element.get_attribute('id'),
                    className=element.get_attribute('class')
                )
                tags.append(append)

            return  tags

        except NoSuchElementException as e:
            raise HTTPException(
                status_code=404,
                detail="no such element"
            )
        finally:
            browser_instance.quit()

    async def find_title(self, browser: str, page: str, title: str):
        browser_instance = selenium_browser(browser)
        browser_instance.get(page)

        try:
            element = browser_instance.find_element(By.XPATH, f"//*[contains(text(), '{title}')]")
            return  Alone(
                text=element.text,
                id=element.get_attribute('id'),
                className=element.get_attribute('class')
            )

        except NoSuchElementException as e:
            raise HTTPException(
                status_code=404,
                detail="no such element"
            )
        finally:
            browser_instance.quit()