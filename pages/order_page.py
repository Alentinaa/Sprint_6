from datetime import date
from selenium.webdriver import Keys
import allure
import helpers
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Ввод имени')
    def enter_first_name(self, first_name: str):
        return self.find_element_with_wait(OrderPageLocators.ENTER_FIRST_NAME).send_keys(first_name)

    @allure.step('Ввод фамилии')
    def enter_last_name(self, last_name: str):
        return self.find_element_with_wait(OrderPageLocators.ENTER_LAST_NAME).send_keys(last_name)

    @allure.step('Ввод адреса')
    def enter_address(self, address: str):
        return self.find_element_with_wait(OrderPageLocators.ENTER_ADDRESS).send_keys(address)

    @allure.step('Выбор метро')
    def choose_subway(self, subway_name: str):
        self.find_element_with_wait(OrderPageLocators.SUBWAY_FIELD).click()
        return self.find_element_with_wait(helpers.SUBWAY_HINT_BUTTON(subway_name)).click()

    @allure.step('Ввод номера телефона')
    def enter_telephone_number(self, telephone_number: str):
        return self.find_element_with_wait(OrderPageLocators.ENTER_TELEPHONE_NUMBER).send_keys(telephone_number)

    @allure.step('Заполнить данные страницы Для кого самокат')
    def enter_user_data(self, data_set: dict):
        self.enter_first_name(data_set['first_name'])
        self.enter_last_name(data_set['last_name'])
        self.enter_address(data_set['address'])
        self.choose_subway(data_set['subway_name'])
        self.enter_telephone_number(data_set['telephone_number'])

    @allure.step('Клик по кнопке Далее для продолжения оформления заказа')
    def go_next_page(self):
        return self.find_element_with_wait(OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Ввод даты')
    def enter_date(self, date: str):
        element = self.find_element_with_wait(OrderPageLocators.ENTER_DATE)
        element.send_keys(date)
        element.send_keys(Keys.ENTER)
        return element

    @allure.step('Выбор периода аренды из выпадающего списка')
    def choose_rental_period(self):
        self.find_element_with_wait(OrderPageLocators.RENTAL_PERIOD_FIELD).click()
        return self.find_element_with_wait(OrderPageLocators.RENTAL_PERIOD_LIST).click()

    @allure.step('Выбор цвета самоката')
    def choose_color(self, option: int):
        return self.find_element_with_wait(OrderPageLocators.COLOR_CHECKBOXES).click()

    @allure.step('Комментарий для курьера')
    def enter_comment(self, comment_text):
        return self.find_element_with_wait(OrderPageLocators.ENTER_COMMENT_FOR_COURIER).send_keys(comment_text)

    @allure.step('Заполнить данные на странице Про аренду')
    def enter_rest_data(self, data_set: dict):
        self.enter_date(data_set['date'])
        self.choose_rental_period()
        for option in data_set['color']:
            self.choose_color(option)
        self.enter_comment(data_set['comment_for_courier'])

    @allure.step('Нажать "Заказать" после заполнения данных')
    def click_order_button(self):
        return self.find_element_with_wait(OrderPageLocators.ORDER_BUTTON).click()

    @allure.step('Подтвердить заказ')
    def click_accept_order(self):
        return self.find_element_with_wait(OrderPageLocators.ACCEPT_ORDER_BUTTON).click()