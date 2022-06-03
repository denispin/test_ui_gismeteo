import logging

import allure
import time

from selenium.webdriver.chrome.webdriver import WebDriver

base_url = "https://www.gismeteo.ru/"


class Application:

    def __init__(self):
        self.wd = WebDriver('../chromedriver')
        self.wd.set_window_size(1920, 1080)

    def open_home_page(self):
        wd = self.wd
        with allure.step(f"Открываю {base_url}"):
            wd.get(base_url)

    def popular_cities(self):
        wd = self.wd

        popular_cities_list = []
        for city in wd.find_elements_by_css_selector('div.cities-popular  div.list div a'):
            popular_cities_list.append(city.text)
        return popular_cities_list

    def city_search(self, city_name):
        wd = self.wd
        wd.find_element_by_css_selector('.input').send_keys(city_name)
        time.sleep(1)
        cities_title = wd.find_elements_by_css_selector('div.city-title')
        for el in cities_title:
            if el.text == city_name:
                el.click()
                break

    def get_page_title(self):
        wd = self.wd
        return wd.find_element_by_css_selector('.page-title').text

    def open_soft_page(self):
        wd = self.wd
        wd.find_element_by_xpath('//a[@href="/soft/"]').click()

    def open_soft_tv_page(self):
        wd = self.wd
        wd.find_element_by_xpath('//a[@href="/soft-tv/"]').click()

    def get_soft_header_text(self):
        wd = self.wd
        return wd.find_element_by_css_selector('div.soft-header').text

    def open_10days_weather(self, city_code):
        wd = self.wd
        wd.find_element_by_xpath(f"//a[@href='/weather-{city_code}/10-days/']").click()

    def get_city_link(self):
        wd = self.wd
        link = wd.find_element_by_css_selector('a.city-link.link').get_attribute('href')
        city_id = link.split('/')[3].split('-')[1:]
        return link, "-".join(city_id)

    def get_page_url(self):
        wd = self.wd
        return wd.current_url

    def count_of_days(self):
        wd = self.wd
        widgets = wd.find_elements_by_css_selector('div.widget-row.widget-row-days-date')
        for widget in widgets:
            days = widget.find_elements_by_css_selector('a')
        return len(days)

    def destroy(self):
        self.wd.quit()
