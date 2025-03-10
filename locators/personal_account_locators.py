from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    ORDER_HISTORY = [By.XPATH,
                     "//a[contains(@class, 'Account_link') and text()='История заказов']"]  # "кнопка" история заказов в личном кабинете

    PERSONAL_ACCOUNT = [By.XPATH,
                        "//p[contains(@class, 'AppHeader_header') and text()='Личный Кабинет']"]  # "кнопка" личный кабинет

    EXIT = [By.XPATH,
            "//button[contains(@class, 'Account_button') and text()='Выход']"]  # "кнопка" выход
