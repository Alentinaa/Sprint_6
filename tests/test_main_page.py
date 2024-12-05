import pytest
import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from urls import URLs

class TestOrderButton:
    @allure.title('Нажатие на кнопку Заказать')
    @allure.description('Проверяется, что при клике по кнопке Заказать, '
                        'открывается страница Оформления заказа')
    @pytest.mark.parametrize(
        "order_button_locator",
        [
            (MainPageLocators.ORDER_BUTTON_IN_MAIN_PAGE_HEADER),
            (MainPageLocators.ORDER_BUTTON_IN_HOW_IN_WORKS_PAGE),
        ]
    )

    def test_click_order_button(self, driver, order_button_locator):
        url = URLs.MAIN_PAGE
        main_page = MainPage(driver)
        main_page.go_to_url(url)
        main_page.click_accept_cookie_button()
        main_page.click_order_button(order_button_locator)
        assert URLs.ORDER_PAGE in main_page.get_current_url()

