from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Локатор поля Имя
    ENTER_FIRST_NAME = [By.XPATH, ".//input[contains(@placeholder,'* Имя')]"]

    # Локатор поля Фамилия
    ENTER_LAST_NAME = [By.XPATH, ".//input[contains(@placeholder,'* Фамилия')]"]

    # Локатор поля Адрес:куда привезти заказ
    ENTER_ADDRESS = [By.XPATH, ".//input[contains(@placeholder,'* Адрес: куда привезти заказ')]"]

    # Локатор поля Станция метро
    SUBWAY_FIELD = [By.XPATH, ".//input[contains(@placeholder,'* Станция метро')]"]

    # Локатор поля Телефон: на него позвонит курьер
    ENTER_TELEPHONE_NUMBER = [By.XPATH, ".//input[contains(@placeholder,'* Телефон: на него позвонит курьер')]"]

    # Локатор кнопки Далее
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]

    # Локатор поля Когда привезти самокат
    ENTER_DATE = [By.XPATH, ".//input[contains(@placeholder,'* Когда привезти самокат')]"]

    # Локатор поля Срок аренды
    RENTAL_PERIOD_FIELD = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    # Локатор выпадающего списка
    RENTAL_PERIOD_LIST = [By.XPATH, "// div[text() = 'двое суток']"]

    # Локатор поля Цвет самоката чёрный жемчуг
    COLOR_CHECKBOXES = [By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input"]

    # Локатор поля Комментарий для курьера
    ENTER_COMMENT_FOR_COURIER = [By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]"]

    # Локатор кнопки Заказать
    ORDER_BUTTON = [By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"]

    # Локатор кнопки Да во всплывающем окне Хотите оформить заказ?
    ACCEPT_ORDER_BUTTON = [By.XPATH, ".//button[text()='Да']"]

    # Локатор кнопки Посмотреть статус в окне Заказ оформлен
    SHOW_STATUS_BUTTON = [By.XPATH, ".//button[text()='Посмотреть статус']"]