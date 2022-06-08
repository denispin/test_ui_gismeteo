import time

from locators.gismeteo_locators import GismeteoLocators
from page.base_app import BasePage


class StartPage(BasePage):

    def get_popular_cities_list(self):
        popular_cities_list = []
        for city in self.find_elements(GismeteoLocators.POPULAR_CITIES):
            popular_cities_list.append(city.text)
        return popular_cities_list

    def city_search(self, city_name):
        self.find_element(GismeteoLocators.GISMETEO_SEARCH_FIELD).send_keys(city_name)
        time.sleep(1)
        cities_title = self.find_elements(GismeteoLocators.CITIES_TITLE)
        for el in cities_title:
            if el.text == city_name:
                el.click()
                break

    def get_page_title(self):
        return self.find_element(GismeteoLocators.PAGE_TITLE).text

    def open_soft_page(self):
        self.find_element(GismeteoLocators.SOFT_PAGE).click()

    def open_soft_tv_page(self):
        self.find_element(GismeteoLocators.SOFT_TV_PAGE).click()

    def get_soft_header_text(self):
        return self.find_element(GismeteoLocators.GET_SOFT_HEADER_TEXT).text

    def open_10days_weather(self, city_code):
        self.app.wd.find_element_by_xpath(f"//a[@href='/weather-{city_code}/10-days/']").click()

    def get_city_link(self):
        link = self.find_element(GismeteoLocators.CITY_LINK).get_attribute('href')
        city_id = link.split('/')[3].split('-')[1:]
        return link, "-".join(city_id)

    def get_page_url(self):
        return self.cur_url()
