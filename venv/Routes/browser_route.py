from fastapi import APIRouter, Form
from typing import Annotated
from Controllers.browser_controller import Browser_Controller

router = APIRouter()

browser_controller = Browser_Controller()

@router.get("/scraping/atribute/")
async def scraping_atribute(browser: Annotated[str, Form()], page: Annotated[str, Form()], selector: Annotated[str, Form()]):
    browser_controller.find_atribute(browser, page, selector)

@router.get("/scraping/all/tags/")
async def scraping_tangs(browser: Annotated[str, Form()], page: Annotated[str, Form()], tag: Annotated[str, Form()]):
    browser_controller.all_tags(browser, page, tag)