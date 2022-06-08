import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, app):
        self.app = app

    def find_element(self, locator, time=3):
        return WebDriverWait(self.app.wd, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=3):
        return WebDriverWait(self.app.wd, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def cur_url(self):
        a = self.app.wd.current_url
        return a
