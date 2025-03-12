import allure
from conftest import driver
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.login_page import LoginPage
import data


@allure.suite('Тесты страницы Личного кабинета')
class TestPersonalAccountPage:

    @allure.title('Проверка раздела Личный кабинет')
    @allure.description('Тест проверяет переход по клику в «Личный кабинет»')
    def test_redirect_to_personal_account(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        main_page.click_to_login_to_account()
        login_page.input_email_in_form_authorization(data.USER_EMAIL)
        login_page.input_password_in_form_authorization(data.USER_PASSWORD)
        login_page.click_to_enter()
        main_page.click_to_personal_account()
        assert personal_account_page.is_profile_in_personal_account(), "Личный кабинет не открылся."

    @allure.description('Тест проверяет переход в раздел «История заказов»')
    def test_navigate_to_order_history(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        main_page.click_to_login_to_account()
        login_page.input_email_in_form_authorization(data.USER_EMAIL)
        login_page.input_password_in_form_authorization(data.USER_PASSWORD)
        login_page.click_to_enter()
        main_page.click_to_personal_account()
        personal_account_page.click_to_order_history()
        assert personal_account_page.is_order_history_opened(), "Раздел 'История заказов' не открылся"

    @allure.description('Тест проверяет выход из аккаунта')
    def test_logout_from_personal_account(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        main_page.click_to_login_to_account()
        login_page.input_email_in_form_authorization(data.USER_EMAIL)
        login_page.input_password_in_form_authorization(data.USER_PASSWORD)
        login_page.click_to_enter()
        main_page.click_to_personal_account()
        personal_account_page.click_to_exit()
        assert login_page.is_login_page_opened, "Выход из аккаунта не произошел."
