import allure
from locators.switch_page_locators import SwitchPageLocators
from pages.base_page import BasePage

class SwitchPage(BasePage):
    @allure.step('Переключиться на новое окно через редирект браузера')
    def switch_window(self, window_num: int = -1):
        return self.driver.switch_to.window(self.driver.window_handles[window_num])

    @allure.step('Перейти на главную страницу Дзена')
    def click_to_yandex_logo(self):
        return self.find_element_with_wait(SwitchPageLocators.YANDEX_LOGO).click()

    @allure.step('Перейти на главную страницу Самоката')
    def click_to_samokat_logo(self):
        return self.find_element_with_wait(SwitchPageLocators.SAMOKAT_LOGO).click()