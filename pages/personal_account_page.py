import allure
from locators.personal_account_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    @allure.step('Клик на История заказов')
    def click_to_order_history(self):
        self.click_to_element(PersonalAccountPageLocators.ORDER_HISTORY)

    @allure.step('Клик на Личный кабинет')
    def click_to_personal_account(self):
        self.click_to_element(PersonalAccountPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Клик на Выход')
    def click_to_exit(self):
        self.click_to_element(PersonalAccountPageLocators.EXIT)

    @allure.step('Проверяем, что открылся Личный кабинет (Находим раздел Профиль)')
    def is_profile_in_personal_account(self):
        return self.find_element_with_wait(PersonalAccountPageLocators.PROFILE)

    @allure.step('Проверяем, что открылся раздел История Заказов (проверяем отображения списка заказов)')
    def is_order_history_opened(self):
        return self.find_element_with_wait(PersonalAccountPageLocators.LIST_OF_ORDERS)
