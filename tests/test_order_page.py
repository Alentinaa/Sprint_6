import pytest
import allure
from data import OrderPageData
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import URLs

class TestOrder:
    @allure.title('Оформление заказа')
    @allure.description('Корректное заполнение формы заказа и появление '
                        'всплывающего окна с сообщением об успешном создании заказа.')
    @pytest.mark.parametrize(
        "entry_button_locator, customer_data",
        [
            (MainPageLocators.ORDER_BUTTON_IN_MAIN_PAGE_HEADER, OrderPageData.data_sets['data_set1']),
            (MainPageLocators.ORDER_BUTTON_IN_HOW_IN_WORKS_PAGE, OrderPageData.data_sets['data_set2']),
        ]
    )
    def test_create_order_is_successful(self, driver, entry_button_locator, customer_data):
        url = URLs.MAIN_PAGE
        main_page = MainPage(driver)
        driver.get(url)
        main_page.click_accept_cookie_button()
        main_page.click_order_button(entry_button_locator)
        order_page = OrderPage(driver)
        order_page.enter_user_data(customer_data)
        order_page.go_next_page()
        order_page.enter_rest_data(customer_data)
        order_page.click_order_button()
        order_page.click_accept_order()
        assert order_page.find_element_with_wait(OrderPageLocators.SHOW_STATUS_BUTTON).is_displayed()

