from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage:
    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(locator)
        )
        return self.driver.find_element(*locator)

    @allure.step('Скролл к элементу')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()

    @allure.step('Получить текст с элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step('Форматирование локаторов в блоке Вопросы о важном')
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator