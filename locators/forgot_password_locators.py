from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    LOGIN_IN_PASSWORD_PASSWORD_RECOVERY_FORM = [By.XPATH,
                                                "//a[contains(@class , 'Auth_link') and text() = 'Войти']"]  # кнопка "Войти" в форме восстановления пароля
    EMAIL_INPUT_FIELD_RECOVERY_FORM = [By.XPATH,
                                      "//label[text()='Email']/following-sibling::input"]  # поле ввода email в восстановлении пароля

    RECOVERY_BUTTON = [By.XPATH,
                       "//button[contains(@class, 'button_button_type_primary') and text()='Восстановить']"] # кнопка "Восстановить" в форме восстановления пароля
