import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from fixture.session import SessionHelper
from locators.gismeteo_locators import CountOfDays
from page.start_page import StartPage


class Application:

    def __init__(self):
        self.wd = WebDriver('../chromedriver')
        self.wd.set_window_size(1920, 1080)
        self.start_page = StartPage(self)
        self.session = SessionHelper(self)
        self.count = CountOfDays(self)

    def get_screenshot(self):
        with allure.step('Получаю скриншот'):
            allure.attach(
                self.wd.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )

    def destroy(self):
        self.wd.quit()
