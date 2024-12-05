import allure
from pages.switch_page import SwitchPage
from urls import URLs

class TestSwitchPage:
    @allure.title('Клик по логотипу Яндекса')
    @allure.description('Клик по логотипу Яндекса на главной '
                        'странице ведет к открытию главной страницы Дзена.')
    def test_click_to_yandex_logo(self, driver):
        url = URLs.MAIN_PAGE
        switch_page = SwitchPage(driver)
        switch_page.go_to_url(url)
        switch_page.click_to_yandex_logo()
        switch_page.switch_window(-1)
        assert switch_page.is_on_dzen_page()

    @allure.title('Клик по логотипу Самоката')
    @allure.description('Клик по логотипу Самоката на странице оформления '
                        'заказа ведет к переходу на главную страницу сервиса Яндекс Самокат')

    def test_click_to_samokat_logo(self, driver):
        url = URLs.ORDER_PAGE
        switch_page = SwitchPage(driver)
        switch_page.go_to_url(url)
        switch_page.click_to_samokat_logo()
        assert switch_page.is_on_main_page()