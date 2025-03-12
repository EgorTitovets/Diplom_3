import allure
from conftest import driver
from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
import data


@allure.suite('Тесты страницы Восстановления пароля')
class TestRecoveryPasswordPage:

    @allure.title('Проверка раздела Восстановления пароля')
    @allure.description('Тест проверяет переход на страницу восстановления пароля по кнопке «Восстановить пароль')
    def test_recovery_button_redirects_to_password_reset(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_password_page = ForgotPasswordPage(driver)
        main_page.click_to_personal_account()
        login_page.click_to_recovery_password()
        assert recovery_password_page.is_reset_page_opened(), "Страница восстановления пароля не открылась!"

    @allure.description('Тест проверяет ввод почты и клик по кнопке «Восстановить»')
    def test_password_recovery_by_email(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_password_page = ForgotPasswordPage(driver)
        main_page.click_to_personal_account()
        login_page.click_to_recovery_password()
        recovery_password_page.input_email_in_form_recovery_password(data.EMAIL_PASSWORD_RECOVERY)
        recovery_password_page.click_to_recovery_button()
        assert recovery_password_page.is_recovery_code_field_displayed(), "Ввод почты и клик по кнопке 'Восстановить' - не получился"

    @allure.description('Тест проверяет, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_password_field_highlighted(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_password_page = ForgotPasswordPage(driver)
        main_page.click_to_personal_account()
        login_page.click_to_recovery_password()
        recovery_password_page.input_email_in_form_recovery_password(data.EMAIL_PASSWORD_RECOVERY)
        recovery_password_page.click_to_recovery_button()
        recovery_password_page.click_to_password_visibility()
        assert recovery_password_page.is_password_field_active, "Поле не стало подсвечено после клика"
