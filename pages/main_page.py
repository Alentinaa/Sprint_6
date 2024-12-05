import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Получить текст ответа в блоке Вопросы о важном')
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER, num)
        self.scroll_to_element(MainPageLocators.LAST_QUESTION_FOR_SCROLL)
        self.find_element_with_wait(MainPageLocators.LAST_QUESTION_FOR_SCROLL)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Принять куки')
    def click_accept_cookie_button(self):
        self.click_to_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Нажать на кнопку Заказать, переданную в локаторе')
    def click_order_button(self, locator):
        self.find_element_with_wait(locator).click()

