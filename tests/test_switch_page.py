import allure
from locators.main_page_locators import MainPageLocators
from locators.switch_page_locators import SwitchPageLocators
from pages.switch_page import SwitchPage
from urls import URLs

class TestSwitchPage:
    @allure.title('Клик по логотипу Яндекса')
    @allure.description('Клик по логотипу Яндекса на главной '
                        'странице ведет к открытию главной страницы Дзена.')
    def test_click_to_yandex_logo(self, driver):
        url = URLs.MAIN_PAGE
        switch_page = SwitchPage(driver)
        driver.get(url)
        switch_page.click_to_yandex_logo()
        switch_page.switch_window(-1)
        assert switch_page.find_element_with_wait(SwitchPageLocators.FIND_BUTTON_ON_DZEN_PAGE).is_displayed()

    @allure.title('Клик по логотипу Самоката')
    @allure.description('Клик по логотипу Самоката на странице оформления '
                        'заказа ведет к переходу на главную страницу сервиса Яндекс Самокат')

    def test_click_to_samokat_logo(self, driver):
        url = URLs.ORDER_PAGE
        switch_page = SwitchPage(driver)
        driver.get(url)
        switch_page.click_to_samokat_logo()
        assert switch_page.find_element_with_wait(MainPageLocators.HOME_HEADER).is_displayed()