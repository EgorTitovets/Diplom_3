import allure
from conftest import driver
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.login_page import LoginPage
import data


@allure.suite('Тесты на Проверку основного функционала')
class TestMainFunctionalPage:

    @allure.title('Проверка основного функционала')
    @allure.description('Тест проверяет переход по клику на "Конструктор"')
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_login_to_account()
        main_page.click_to_constructor()
        assert main_page.is_constructor_main_page_opened(), "Не открылась главная страница Конструктора"

    @allure.description('Тест проверяет переход по клику на "Лента заказов"')
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_order_feed()
        assert main_page.is_order_feed_opened(), "Не открылась страница Лента заказов"
