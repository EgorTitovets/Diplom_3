import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Клик на Восстановить пароль')
    def click_to_recovery_password(self):
        self.click_to_element(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Вводим пароль - в поле пароль в форме авторизации')
    def input_password_in_form_authorization(self, text):
        self.add_text_to_element(LoginPageLocators.PASSWORD_INPUT_FIELD_AUTHORIZATION_FORM, text)

    @allure.step('Вводим Email - в поле enail в форме авторизации')
    def input_email_in_form_authorization(self, text):
        self.add_text_to_element(LoginPageLocators.EMAIL_INPUT_FIELD_AUTHORIZATION_FORM, text)

    @allure.step('Клик на кнопку Войти')
    def click_to_enter(self):
        self.click_to_element(LoginPageLocators.LOGIN_FINISH_BUTTON)
