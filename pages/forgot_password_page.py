import allure
from locators.forgot_password_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Вводим Email в поле email при восстановлении пароля')
    def input_email_in_form_recovery_password(self, text):
        self.add_text_to_element(ForgotPasswordPageLocators.EMAIL_INPUT_FIELD_RECOVERY_FORM, text)

    @allure.step('Клик на кнопку Восстановить в форме восстановления пароля')
    def click_to_recovery_button(self):
        self.click_to_element(ForgotPasswordPageLocators.RECOVERY_BUTTON)

    @allure.step('Проверяем, что заголовок "Восстановление пароля" отображается.')
    def is_reset_page_opened(self):
        return self.find_element_with_wait(ForgotPasswordPageLocators.RESET_PAGE_HEADER)

    @allure.step('Проверяем, что отображается "поле ввода кода из письма".')
    def is_recovery_code_field_displayed(self):
        return self.find_element_with_wait(ForgotPasswordPageLocators.INPUT_RECOVERY_CODE)

    @allure.step('Клик по кнопке показать/скрыть пароль')
    def click_to_password_visibility(self):
        self.click_to_element(ForgotPasswordPageLocators.PASSWORD_VISIBILITY)

    @allure.step('Проверяем, что поле пароля подсвечено')
    def is_password_field_active(self):
        return self.find_element_with_wait(ForgotPasswordPageLocators.INPUT_FIELD_ACTIVE)
