import allure
from locators.main_page_locators import MainPageLocators
from locators.switch_page_locators import SwitchPageLocators
from pages.base_page import BasePage

class SwitchPage(BasePage):
    @allure.step('Переключиться на новое окно через редирект браузера')
    def switch_window(self, window_num: int = -1):
        window_handles = self.get_window_handles()
        self.switch_to_window(window_handles[window_num])

    @allure.step('Перейти на главную страницу Дзена')
    def click_to_yandex_logo(self):
        return self.find_element_with_wait(SwitchPageLocators.YANDEX_LOGO).click()

    @allure.step('Перейти на главную страницу Самоката')
    def click_to_samokat_logo(self):
        return self.find_element_with_wait(SwitchPageLocators.SAMOKAT_LOGO).click()

    @allure.step('Проверка, что кнопка Найти видна на странице Дзена')
    def is_on_dzen_page(self):
        element = self.find_element_with_wait(SwitchPageLocators.FIND_BUTTON_ON_DZEN_PAGE)
        return element.is_displayed()

    @allure.step('Проверка, что виден заголовок главной страницы Яндекс.Самокат')
    def is_on_main_page(self):
        element = self.find_element_with_wait(MainPageLocators.HOME_HEADER)
        return element.is_displayed()