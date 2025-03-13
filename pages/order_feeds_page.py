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

    @allure.step('Находим номер заказа на странице "Лента заказов"')
    def get_order_number_from_feed(self):
        order_number_element = self.find_element_with_wait(OrderFeedsPageLocators.ORDER_NUMBER_IN_ORDER_FEEDS)
        order_number_text = order_number_element.text.strip()
        return order_number_text

    @allure.step('Находим номер заказа на popup после успешного оформления заказа')
    def get_order_number_from_order(self):
        order_number_element = self.find_element_with_wait(OrderFeedsPageLocators.ORDER_NUMBER)
        order_number = order_number_element.text.strip()
        return order_number

    @allure.step('Находим количество заказов за все время')
    def get_order_number_total(self):
        total_orders = self.find_element_with_wait(OrderFeedsPageLocators.TOTAL_ORDERS_COUNT)
        total_orders_number = total_orders.text.strip()
        return total_orders_number

    @allure.step('Находим количество заказов за сегодня')
    def get_order_number_today(self):
        today_orders = self.find_element_with_wait(OrderFeedsPageLocators.TODAY_ORDERS_COUNT)
        today_orders = today_orders.text.strip()
        return today_orders

    @allure.step('Находим номер заказа в разделе "В работе')
    def find_order_number_in_progress(self):
        order_number_element = self.find_element_with_wait(OrderFeedsPageLocators.ORDER_NUMBER_IN_PROGRESS)
        order_number_text = order_number_element.text.strip()
        return order_number_text
