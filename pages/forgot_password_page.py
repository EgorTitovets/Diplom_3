import allure
from locators.forgot_password_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Вводим Email в поле email при восстановлении пароля')
    def input_email_in_form_recovery_password(self, text):
        self.add_text_to_element(ForgotPasswordPageLocators.EMAIL_INPUT_FIELD_RECOVERY_FORM, text)

    @allure.step('Клик на Восстановить в форме восстановления пароля')
    def click_to_recovery_button(self):
        self.click_to_element(ForgotPasswordPageLocators.RECOVERY_BUTTON)
