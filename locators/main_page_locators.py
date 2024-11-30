from selenium.webdriver.common.by import By

class MainPageLocators:
    # Локатор кнопки куки
    COOKIE_BUTTON = [By.XPATH, ".//button[text()='да все привыкли']"]

    # Локаторы вопросов и ответов
    QUESTION = [By.XPATH, '//*[@id="accordion__heading-{}"]']
    ANSWER = [By.XPATH, '//*[@id="accordion__panel-{}"]']
    LAST_QUESTION_FOR_SCROLL = [By.XPATH, '//*[@id="accordion__heading-7"]']

    # Локатор заголовка Самокат на пару дней
    HOME_HEADER = [By.XPATH, '//*[contains(@class, Home_Header)]']

    # Локаторы 2-х кнопок Заказать
    ORDER_BUTTON_IN_MAIN_PAGE_HEADER = [By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"]
    ORDER_BUTTON_IN_HOW_IN_WORKS_PAGE = [By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"]