from selenium.webdriver.common.by import By

from page.base_app import BasePage


class GismeteoLocators:
    GISMETEO_SEARCH_FIELD = (By.CSS_SELECTOR, '.input')
    CITIES_TITLE = (By.CSS_SELECTOR, 'div.city-title')
    PAGE_TITLE = (By.CSS_SELECTOR, '.page-title')
    POPULAR_CITIES = (By.CSS_SELECTOR, 'div.cities-popular  div.list div a')
    SOFT_PAGE = (By.XPATH, '//a[@href="/soft/"]')
    SOFT_TV_PAGE = (By.XPATH, '//a[@href="/soft-tv/"]')
    GET_SOFT_HEADER_TEXT = (By.CSS_SELECTOR, 'div.soft-header')
    CITY_LINK = (By.CSS_SELECTOR, 'a.city-link.link')
    COUNT_OF_DAYS = (By.CSS_SELECTOR, 'div.widget-row.widget-row-days-date')
    DAYS = (By.CSS_SELECTOR, 'a')


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(GismeteoLocators.GISMETEO_SEARCH_FIELD)
        search_field.send_keys(word)


class CountOfDays(BasePage):

    def count_of_days(self):
        widgets = self.find_elements(GismeteoLocators.COUNT_OF_DAYS)
        for widget in widgets:
            days = widget.find_elements_by_css_selector('a')
        return len(days)
