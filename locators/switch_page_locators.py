from selenium.webdriver.common.by import By

class SwitchPageLocators:
    # Локатор логотипа Яндекс
    YANDEX_LOGO = [By.XPATH, ".//img[@alt='Yandex']/parent::a"]

    # Локатор кнопки Найти на странице Дзен
    FIND_BUTTON_ON_DZEN_PAGE = [By.XPATH, '//button[text() = "Найти"]']

    # Локатор логотипа Самокат
    SAMOKAT_LOGO = [By.XPATH, ".//img[@alt='Scooter']/parent::a"]
