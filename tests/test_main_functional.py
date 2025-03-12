import allure
from conftest import driver
from pages.main_page import MainPage
from pages.login_page import LoginPage
import data
from locators.main_page_locators import MainPageLocators


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

    @allure.description('Тест проверяет, что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_ingredient_modal_opens_on_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_ingredient()
        assert main_page.check_popup_with_the_details_of_the_ingredient(), "Не открылась всплывающее окно с деталями"

    @allure.description('Тест проверяет, что всплывающее окно закрывается кликом по крестику')
    def test_ingredient_modal_closes_on_cross_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_ingredient()
        main_page.click_to_cross_in_popup_with_the_details_of_the_ingredient()
        assert main_page.is_constructor_main_page_opened(), "Всплывающее окно не закрылось кликом по крестику"

    @allure.description(
        'Тест проверяет, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_ingredient_counter_increases_on_addition(self, driver):
        main_page = MainPage(driver)
        main_page.add_ingredient_spicy_x_in_basket()
        (main_page.add_ingredient_spicy_x_in_basket())
        counter_value = main_page.get_ingredient_counter_value()
        expected_value = 2
        assert counter_value == expected_value, f"Ожидалось {expected_value}, но получили {counter_value}"

    @allure.description(
        'Тест проверяет, что залогиненный пользователь может оформить заказ.')
    def test_logged_in_user_can_place_order(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.click_to_login_to_account()
        login_page.input_email_in_form_authorization(data.USER_EMAIL)
        login_page.input_password_in_form_authorization(data.USER_PASSWORD)
        login_page.click_to_enter()
        main_page.add_ingredient_in_basket(MainPageLocators.INGREDIENT_FLUORESCENT_BUN)
        main_page.click_to_place_order()
        assert main_page.is_order_confirmation_popup_displayed(), "Не получилось создать заказ"
