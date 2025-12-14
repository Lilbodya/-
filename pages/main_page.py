import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Locators:
    SEARCH_FIELD = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    TITLES = (By.CSS_SELECTOR, "div.product-card__content")
    POPUP_CLOSE = (By.CSS_SELECTOR, '[data-popmechanic-close]')
    CITY_CONFIRM = (
        By.CSS_SELECTOR,
        '.chg-app-button--primary.chg-app-button--block')
    FIRST_PRODUCT = (By.CSS_SELECTOR, "a.product-card__title")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h1")


class MainPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(url)

    def _wait_for_elements(self, locator, multiple=False, timeout=10):
        if multiple:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator))
        else:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))

    @allure.step("Выбор города")
    def close_popups(self):
        # Подтверждение города
        try:
            city_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(Locators.CITY_CONFIRM)
            )
            city_button.click()
        except TimeoutException:
            pass

        # Рекламный попап
        try:
            popup_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(Locators.POPUP_CLOSE)
            )
            popup_button.click()
        except TimeoutException:
            pass

    @allure.step("Проверка заголовка страницы")
    def check_page_title(self, expected_title):
        WebDriverWait(self.driver, 10).until(EC.title_is(expected_title))
        return True

    @allure.step("Поиск товара по фразе")
    def search_goods(self, phrase):
        search_field = self._wait_for_elements(
            Locators.SEARCH_FIELD, multiple=False)
        search_field.send_keys(phrase)
        search_button = self._wait_for_elements(
            Locators.SEARCH_BUTTON, multiple=False)
        search_button.click()

    @allure.step("Получаем количество элементов в результатах поиска")
    def get_search_results_count(self):
        elements = self._wait_for_elements(Locators.TITLES, multiple=True)
        return len(elements)

    @allure.step("Открытие первой книги из результатов поиска")
    def open_first_search_result(self):
        first_product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.FIRST_PRODUCT)
        )
        first_product.click()

    @allure.step("Проверка, что открылась страница книги")
    def is_product_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.PRODUCT_TITLE)
        ).is_displayed()
