import allure

from helpers.config import base_url


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        with allure.step(f"Открываю {base_url}"):
            wd.get(base_url)
