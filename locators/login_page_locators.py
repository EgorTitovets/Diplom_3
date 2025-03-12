from selenium.webdriver.common.by import By


class LoginPageLocators:
    PASSWORD_RECOVERY_BUTTON = [By.XPATH,
                                "//a[text()='Восстановить пароль']"]  # "Восстановить пароль" в форме авторизации
    EMAIL_INPUT_FIELD_AUTHORIZATION_FORM = [By.XPATH,
                                            "//label[text()='Email']/following-sibling::input"]  # поле ввода email в авторизации
    PASSWORD_INPUT_FIELD_AUTHORIZATION_FORM = [By.XPATH,
                                               "//label[text()='Пароль']/following-sibling::input"]  # поле ввода пароль в авторизации
    LOGIN_FINISH_BUTTON = [By.XPATH,
                           "//button[contains(@class, 'button_button_type_primary') and text()='Войти']"]  # кнопка "Войти" в форме авторизации (при вводе Email и Пароль)

    LOGIN_PAGE_HEADER = [By.XPATH,
                         "//h2[text()='Вход']"]  # заголовой страаницы аавторизации (логина) на котором написано Вход
