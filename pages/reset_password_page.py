import allure
from locators.reset_password_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    # @allure.step('Вводим Email в поле email при восстановлении пароля')
    # def input_email_in_form_recovery_password(self, text):
    #     self.add_text_to_element(ForgotPasswordPageLocators.EMAIL_INPUT_FIELD_RECOVERY_FORM, text)