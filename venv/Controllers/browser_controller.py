from fastapi import Form, HTTPException
from fastapi.responses import FileResponse
from typing import Annotated
from Methods.browser_method import selenium_browser
from selenium.webdriver.common.by import By
from Interfaces.browser_interface import Alone
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import os
import uuid

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
        try:
            browser_instance.get(page)
        except:
            print("error")

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

    async def capture_screenshots(self, browser: str, page: str):
        browser_instance = selenium_browser(browser)
        try:
            browser_instance.get(page)
        except WebDriverException as e:
            raise HTTPException(status_code=400, detail="Please enter the complete and correctly formatted URL. The URL you provided seems to be invalid.")
        except:
            raise HTTPException(status_code=400, detail="An unexpected error occurred. Please try again later.")

        screenshot_folder = "Screenshots"

        for filename in os.listdir(screenshot_folder):
            file_path = os.path.join(screenshot_folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to delete {file_path}.")


        screenshot_filename = f"{uuid.uuid4()}.png"
        screenshot_path = os.path.join(screenshot_folder, screenshot_filename)

        try:
            browser_instance.save_screenshot(screenshot_path)

            if not os.path.exists(screenshot_path):
                raise HTTPException(status_code=500, detail="Failed to capture screenshot")

            return FileResponse(screenshot_path)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail="no such element"
            )
        finally:
            browser_instance.quit()
