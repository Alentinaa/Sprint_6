from selenium.webdriver.common.by import By

@staticmethod
def SUBWAY_HINT_BUTTON(subway_name: str):
    return [By.XPATH, f".//div[text()='{subway_name}']/parent::button"]