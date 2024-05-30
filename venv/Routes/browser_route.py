from fastapi import APIRouter, Form
from typing import Annotated
from Controllers.browser_controller import Browser_Controller

router = APIRouter()

controller = Browser_Controller()

@router.get("/scraping/atribute/")
async def get_atribute(browser: str, page: str, selector: str):
    return await controller.find_atribute(browser, page, selector)

@router.get("/scraping/all/tags/")
async def get_all_by_tags(browser: str, page: str, tag: str):
    return await controller.all_tags(browser, page, tag)

@router.get("/scraping/title/")
async def find_title(browser: str, page: str, title: str):
    return await controller.find_title(browser, page, title)

@router.get("/scraping/screenshots/")
async def save_screenshots(browser: str, page: str):
    return await controller.capture_screenshots(browser, page)