import time

import allure

from conftest import driver
from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


@allure.suite('Тесты страницы Восстановления пароля')
class TestRecoveryPasswordPage:

    @allure.title('Проверка раздела Восстановления пароля')
    @allure.description('Тест проверяет переход на страницу восстановления пароля по кнопке «Восстановить пароль')
    def test_forgot_password_redirect(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_password_page = ForgotPasswordPage(driver)
        main_page.click_to_personal_account()
        login_page.click_to_recovery_password()
        assert recovery_password_page.is_reset_page_opened(), "Страница восстановления пароля не открылась!"
