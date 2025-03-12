from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    LOGIN_IN_PASSWORD_PASSWORD_RECOVERY_FORM = [By.XPATH,
                                                "//a[contains(@class , 'Auth_link') and text() = 'Войти']"]  # кнопка "Войти" в форме восстановления пароля
    EMAIL_INPUT_FIELD_RECOVERY_FORM = [By.XPATH,
                                       "//label[text()='Email']/following-sibling::input"]  # поле ввода email в восстановлении пароля

    RECOVERY_BUTTON = [By.XPATH,
                       "//button[contains(@class, 'button_button_type_primary') and text()='Восстановить']"]  # кнопка "Восстановить" в форме восстановления пароля

    # RESET_PAGE_HEADER = [By.XPATH,
    #                      "//h2[text()='Восстановление пароля']"]  # заголовок Восстановление пароля (дополнительный xpath)

    RESET_PAGE_HEADER = (
    By.XPATH, "//*[@id='root']/div/main/div/h2[text()='Восстановление пароля']")  # заголовок "Восстановление пароля"

    INPUT_RECOVERY_CODE = [By.XPATH,
                           "//label[contains(@class, 'input__placeholder') and text()='Введите код из письма']"]  # поле ввода кода из письма

    PASSWORD_VISIBILITY = [By.XPATH,
                           "//div[contains(@class, 'input__icon input__icon-action')]"]  # область показать/скрыть пароль

    INPUT_FIELD_ACTIVE = [By.XPATH,
                          "//div[contains(@class, 'input_status_active']"]
