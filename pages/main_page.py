import allure
from selenium.webdriver.common.action_chains import ActionChains

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    @allure.step('Клик на Личный кабинет')
    def click_to_personal_account(self):
        self.click_to_element(MainPageLocators.LOGIN_PERSONAL_ACCOUNT)

    @allure.step('Клик на Войти в аккаунт')
    def click_to_login_to_account(self):
        self.click_to_element(MainPageLocators.LOGIN_MAIN_PAGE)

    @allure.step('Клик на Конструктор')
    def click_to_constructor(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик на Лента заказов')
    def click_to_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED)

    @allure.step('Клик на ингредиент - Флюоресцентная булка')
    def click_to_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT_FLUORESCENT_BUN)

    @allure.step("Проверяем всплывающее окно с деталями ингредиента")
    def check_popup_with_the_details_of_the_ingredient(self):
        element = self.find_element_with_wait(MainPageLocators.INGREDIENT_DETAILS_BUN)
        return element.is_displayed()

    @allure.step('Клик на "Крестик", всплывающего окна с деталями ингредиента')
    def click_to_cross_in_popup_with_the_details_of_the_ingredient(self):
        self.click_to_element(MainPageLocators.CROSS_IN_POPUP_WITH_THE_DETAILS_OF_THE_INGREDIENT)

    @allure.step("Проверяем, что находимся на Общей/главной странице Конструктора с информингом 'Соберите бургер'")
    def is_constructor_main_page_opened(self):
        element = self.find_element_with_wait(MainPageLocators.CONSTRUCTOR_GENERAL_FORM)
        return element.is_displayed()

    @allure.step("Проверяем, что находимся в разделе Лента Заказов")
    def is_order_feed_opened(self):
        element = self.find_element_with_wait(MainPageLocators.ORDER_FEED_PAGE_HEADER)
        return element.is_displayed()

    @allure.step('Добавить ингредиент SPICY_X в корзину')
    def add_ingredient_spicy_x_in_basket(self):
        actions = ActionChains(self.driver)
        ingredient = self.find_element_with_wait(MainPageLocators.INGREDIENT_SAUCE_SPICY_X)
        cart = self.find_element_with_wait(MainPageLocators.BASKET_ORDER)
        actions.drag_and_drop(ingredient, cart).perform()
        WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located(MainPageLocators.INGREDIENT_SAUCE_SPICY_X)
        )

    @allure.step('Добавить любой ингредиент в корзину')
    def add_ingredient_in_basket(self, ingredient_locator):
        actions = ActionChains(self.driver)
        ingredient = self.find_element_with_wait(ingredient_locator)
        cart = self.find_element_with_wait(MainPageLocators.BASKET_ORDER)
        actions.drag_and_drop(ingredient, cart).perform()
        WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located(ingredient_locator)
        )

    @allure.step("Получаем значение счетчика ингредиента (Возвращает числовое значение счетчика у ингредиента)")
    def get_ingredient_counter_value(self):
        counter_element = self.find_element_with_wait(MainPageLocators.SPICY_X_COUNTER_AFTER_ADD)
        return int(counter_element.text)

    @allure.step('Клик на Оформить заказ')
    def click_to_place_order(self):
        self.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Проверяем, что появился popup об успешном оформлении заказа")
    def is_order_confirmation_popup_displayed(self):
        element = self.find_element_with_wait(MainPageLocators.ORDER_CONFIRMATION_POPUP)
        return element.is_displayed()