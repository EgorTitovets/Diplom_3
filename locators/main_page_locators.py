from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_MAIN_PAGE = [By.XPATH,
                       "//button[contains(@class, 'button_button_type_primary') and text()='Войти в аккаунт']"]  # кнопка "Войти в аккаунт" на главной
    LOGIN_PERSONAL_ACCOUNT = [By.XPATH,
                              "//p[contains(@class, 'AppHeader_header') and text()='Личный Кабинет']"]  # кнопка "Личный кабинет" на главной

    CONSTRUCTOR_BUTTON = [By.XPATH,
                          "//p[contains(@class, 'AppHeader_header') and text()='Конструктор']"]  # "Конструктор" в хэдере

    ORDER_FEED = [By.XPATH,
                  "//p[contains(@class, 'AppHeader_header') and text()='Лента Заказов']"]  # "Лента Заказов" в хэдере

    INGREDIENT_FLUORESCENT_BUN = [By.XPATH,
                                  "//img[contains(@alt, 'Флюоресцентная булка')]"]  # ингредиент Флюоресцентная булка
    INGREDIENT_DETAILS_BUN = [By.XPATH,
                              "//h2[contains(@class, 'Modal_modal__title') and text()='Детали ингредиента']"]  # всплывающее окно с деталями ингредиента
    CROSS_IN_POPUP_WITH_THE_DETAILS_OF_THE_INGREDIENT = [By.XPATH,
                                                         "//*[@id='root']/div/section[1]/div[1]/button"]  # крестик на всплывающем окне с деталями ингредиента

    INGREDIENT_SAUCE_SPICY_X = [By.XPATH,
                                "//img[contains(@alt, 'Соус Spicy-X')]"]  # ингредиент Соус SPICY_X

    BASKET_ORDER = [By.XPATH,
                    "//ul[contains(@class, 'BurgerConstructor_basket')]"]  # корзина заказа

    CONSTRUCTOR_GENERAL_FORM = [By.XPATH,
                                "//h1[contains(@class, 'text_type_main-large') and text()='Соберите бургер']"]  # Общая/главная страница Конструктора с информингом "Соберите бургер"

    ORDER_FEED_PAGE_HEADER = [By.XPATH,
                              "//h1[text()='Лента заказов']"]  # заголовок раздела Лента Заказов

    class TestLocators:
        LOGIN_IN_REGISTRATION_FORM = [By.XPATH,
                                      "//a[contains(@class , 'Auth_link') and text() = 'Войти']"]  # кнопка "Войти" в форме регистрации

        LOGOUT_BUTTON = [By.XPATH, "//button[@type='button' and text()='Выход']"]  # кнопка "Выйти"

        REGISTRATION_START_BUTTON = [By.XPATH,
                                     "//a[@href='/register' and text()='Зарегистрироваться']"]  # кнопка "Зарегистрироваться" в разделе авторизации (для открытия формы регистрации)
        REGISTRATION_FINISH_BUTTON = [By.XPATH,
                                      "//button[text()='Зарегистрироваться']"]  # кнопка "Зарегистрироваться" в форме регистрации

        NAME_INPUT_FIELD_REGISTRATION = [By.XPATH,
                                         "//label[text()='Имя']/following-sibling::input"]  # поле ввода Имя в регистрации
        EMAIL_INPUT_FIELD_REGISTRATION = [By.XPATH,
                                          "//label[text()='Email']/following-sibling::input"]  # поле ввода email в регистрации
        PASSWORD_INPUT_FIELD_REGISTRATION = [By.XPATH,
                                             "//input[@type='password' and @name='Пароль']"]  # поле вода пароля в регистрации

        EMAIL_INPUT_FIELD_AUTHORIZATION = [By.XPATH,
                                           "//label[text()='Email']/following-sibling::input"]  # поле ввода email в авторизации
        PASSWORD_INPUT_FIELD_AUTHORIZATION = [By.XPATH,
                                              "//input[@type='password' and @name='Пароль']"]  # поле ввода email в авторизации

        PLACE_ORDER_BUTTON = [By.XPATH,
                              "//*[text()='Оформить заказ']"]  # кнопка "Оформить заказ" у авторизованного пользователя

        STELLAR_BURGERS_BUTTON = [By.XPATH, "//a/*[name()='svg']"]  # логотип Stellar Burgers

        SAUCES_IN_CONSTRUCTOR = [By.XPATH,
                                 "//*[@class='text text_type_main-default' and text()='Соусы']"]  # раздел Соусы в конструкторе
        SAUCES_HEADER_SECTION = [By.XPATH,
                                 "//*[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']"]  # Хэдер секции Соусы в конструкторе
        BUNS_IN_CONSTRUCTOR = [By.XPATH,
                               "//*[@class='text text_type_main-default' and text()='Булки']"]  # раздел Булки в конструкторе
        BUNS_HEADER_SECTION = [By.XPATH,
                               "//*[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']"]  # Хэдер секции Соусы в конструкторе
        FILLINGS_IN_CONSTRUCTOR = [By.XPATH,
                                   "//*[@class='text text_type_main-default' and text()='Начинки']"]  # раздел Начинки в конструкторе
        FILLINGS_HEADER_SECTION = [By.XPATH,
                                   "//*[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"]  # Хэдер секции Соусы в конструкторе

        INVALID_PASSWORD = [By.XPATH,
                            "//*[@class='input__error text_type_main-default' and text()='Некорректный пароль']"]
