import pytest
import allure
from data import HomePageFAQ
from pages.main_page import MainPage
from urls import URLs

class TestMainPage:
    @allure.title('При нажатии на вопрос с 1 по 8 раскрывается ответ')
    @allure.description('Проверяется, что при нажатии на вопрос блока '
                        'Вопросы о важном, открывается соответствующий текст')
    @pytest.mark.parametrize(
        "num, result",
        [
            (0, HomePageFAQ.answer1),
            (1, HomePageFAQ.answer2),
            (2, HomePageFAQ.answer3),
            (3, HomePageFAQ.answer4),
            (4, HomePageFAQ.answer5),
            (5, HomePageFAQ.answer6),
            (6, HomePageFAQ.answer7),
            (7, HomePageFAQ.answer8),
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        url = URLs.MAIN_PAGE
        main_page = MainPage(driver)
        driver.get(url)
        main_page.click_accept_cookie_button()
        assert main_page.get_answer_text(num) == result

