import allure
from locators.order_feeds_locators import OrderFeedsPageLocators
from pages.base_page import BasePage


class OrderFeedsPage(BasePage):

    @allure.step('Клик на Первый (верхний) заказ в ленте заказов')
    def click_to_first_order(self):
        self.click_to_element(OrderFeedsPageLocators.ORDER_1)

    @allure.step('Находим всплывающее окно с деталями заказа')
    def find_popup_window_with_details(self):
        return self.find_element_with_wait(OrderFeedsPageLocators.POPUP_WINDOW_WITH_DETAILS)

