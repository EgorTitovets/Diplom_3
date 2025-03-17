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

    SPICY_X_COUNTER_AFTER_ADD = [By.XPATH,
                                 "//*[@id='root']/div/main/section[1]/div[2]/ul[2]/a[1]/div[1]/p"]  # счетчик кол-ва ингредиента, в конструкторе

    PLACE_ORDER_BUTTON = [By.XPATH,
                          "//button[contains(@class, 'button_button') and text()='Оформить заказ']"]  # кнопка "Оформить заказ"

    ORDER_CONFIRMATION_POPUP = [By.XPATH,
                                "//p[text()='Ваш заказ начали готовить']"]  # popup об успешном оформлении заказа

    CROSS_IN_POPUP = [By.XPATH,
                      "//*[@id='root']/div/section[1]/div[1]/button"]  # крестик на всплывающем окне
