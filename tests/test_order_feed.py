import time

import allure
from conftest import driver
from pages.main_page import MainPage
from pages.order_feeds_page import OrderFeedsPage
from pages.login_page import LoginPage
import data
from locators.main_page_locators import MainPageLocators


@allure.suite('Тесты Раздела «Лента заказов»')
class TestOrderFeedPage:

    @allure.title('Проверка Раздел «Лента заказов»')
    @allure.description('Тест проверяет, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_details_modal_opens_on_click(self, driver):
        order_feed_page = OrderFeedsPage(driver)
        main_page = MainPage(driver)
        main_page.click_to_order_feed()
        order_feed_page.click_to_first_order()
        assert order_feed_page.find_popup_window_with_details(), "Не открылось сплывающее окно с деталями"
