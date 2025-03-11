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

    @allure.step('Клик на ингредиент')
    def click_to_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT_FLUORESCENT_BUN)

    @allure.step("Проверяем всплывающее окно с деталями ингредиента")
    def check_popup_with_the_details_of_the_ingredient(self):
        element = self.find_element_with_wait(MainPageLocators.INGREDIENT_DETAILS_BUN)
        return element.is_displayed()

    @allure.step('Клик на "Крестик", всплывающего окна с деталями ингредиента')
    def click_to_cross_in_popup_with_the_details_of_the_ingredient(self):
        self.click_to_element(MainPageLocators.CROSS_IN_POPUP_WITH_THE_DETAILS_OF_THE_INGREDIENT)

    @allure.step('Добавить ингредиент в корзину')
    def add_ingredient_in_basket(self):
        actions = ActionChains(self.driver)
        # Найти элементы
        ingredient = self.find_element_with_wait(MainPageLocators.INGREDIENT_SAUCE_SPICY_X)
        cart = self.find_element_with_wait(MainPageLocators.BASKET_ORDER)
        actions.drag_and_drop(ingredient, cart).perform()
        #actions.click_and_hold(ingredient).move_to_element(cart).release().perform()  - это альтернативный вариант
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(MainPageLocators.INGREDIENT_SAUCE_SPICY_X)
        ) # это вместо sleep, возможно можно это убрать и сделать time.sleep (для отладки)
        #time.sleep(2)

