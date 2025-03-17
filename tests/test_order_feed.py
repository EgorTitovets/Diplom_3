import allure
from conftest import driver
from pages.main_page import MainPage
from pages.order_feeds_page import OrderFeedsPage
from pages.login_page import LoginPage
import data
import time
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

    @allure.description(
        'Тест проверяет, что заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_user_orders_are_displayed_in_order_feed(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedsPage(driver)

        # Авторизация пользователя
        main_page.click_to_login_to_account()
        login_page.input_email_in_form_authorization(data.USER_EMAIL)
        login_page.input_password_in_form_authorization(data.USER_PASSWORD)
        login_page.click_to_enter()

        # Создание заказа
        main_page.add_ingredient_in_basket(MainPageLocators.INGREDIENT_FLUORESCENT_BUN)
        main_page.click_to_place_order()
        time.sleep(5)
        # Получение номера заказа
        order_number = order_feed_page.get_order_number_from_order()
        print(f"Создан заказ: {order_number}")
        # Закрытие всплывающего окна
        main_page.click_to_cross_in_popup()
        # Переход в ленту заказов
        main_page.click_to_order_feed()
        # Проверка отображения заказа в ленте
        order_number_in_feed = order_feed_page.get_order_number_from_feed()
        print(f"Найден в ленте заказов: {order_number_in_feed}")
        assert f"#0{order_number}" in order_number_in_feed, "Заказа пользователя нет на странице 'Лента заказов'"

    @allure.description(
        'Тест проверяет, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_total_orders_counter_increases_on_new_order(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedsPage(driver)
        # Авторизация пользователя
        main_page.click_to_login_to_account()
        login_page.input_email_in_form_authorization(data.USER_EMAIL)
        login_page.input_password_in_form_authorization(data.USER_PASSWORD)
        login_page.click_to_enter()

        # Переход в ленту заказов
        main_page.click_to_order_feed()
        total_orders_before = order_feed_page.get_order_number_total()

        # делаем заказ
        main_page.click_to_constructor()
        main_page.add_ingredient_in_basket(MainPageLocators.INGREDIENT_FLUORESCENT_BUN)
        main_page.click_to_place_order()
        time.sleep(2)  # никак не получилось без sleep. Перепробовал 10000000 способов с wait
        main_page.click_to_cross_in_popup()

        # Переход в ленту заказов
        main_page.click_to_order_feed()
        total_orders_after = order_feed_page.get_order_number_total()

        assert total_orders_before < total_orders_after, f"{total_orders_before}, а {total_orders_after} получились такими."

    @allure.description(
        'Тест проверяет, что при создании нового заказа счётчик Выполнено за сегодня увеличивается.')
    def test_today_orders_counter_increases_on_new_order(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedsPage(driver)
        # Авторизация пользователя
        main_page.click_to_login_to_account()
        login_page.input_email_in_form_authorization(data.USER_EMAIL)
        login_page.input_password_in_form_authorization(data.USER_PASSWORD)
        login_page.click_to_enter()

        # Переход в ленту заказов
        main_page.click_to_order_feed()
        today_orders_before = order_feed_page.get_order_number_today()

        # делаем заказ
        main_page.click_to_constructor()
        main_page.add_ingredient_in_basket(MainPageLocators.INGREDIENT_FLUORESCENT_BUN)
        main_page.click_to_place_order()
        time.sleep(2)  # никак не получилось без sleep. Перепробовал 10000000 способов с wait
        main_page.click_to_cross_in_popup()

        # Переход в ленту заказов
        main_page.click_to_order_feed()
        time.sleep(2)
        today_orders_after = order_feed_page.get_order_number_today()
        assert today_orders_before < today_orders_after, f"{today_orders_before}, а {today_orders_after} получились такими."

    @allure.description(
        'Тест проверяет, что после оформления заказа его номер появляется в разделе В работе.')
    def test_order_appears_in_progress_after_creation(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed_page = OrderFeedsPage(driver)

        # Авторизация пользователя
        main_page.click_to_login_to_account()
        login_page.input_email_in_form_authorization(data.USER_EMAIL)
        login_page.input_password_in_form_authorization(data.USER_PASSWORD)
        login_page.click_to_enter()

        # Создание заказа
        main_page.add_ingredient_in_basket(MainPageLocators.INGREDIENT_FLUORESCENT_BUN)
        main_page.click_to_place_order()
        time.sleep(5)
        # Получение номера заказа
        order_number = order_feed_page.get_order_number_from_order()
        print(f"Создан заказ: {order_number}")
        # Закрытие всплывающего окна
        main_page.click_to_cross_in_popup()
        # Переход в ленту заказов
        main_page.click_to_order_feed()
        # Проверка отображения заказа в разделе В работе
        order_number_in_progress = order_feed_page.find_order_number_in_progress()
        print(f"Найден в ленте заказов: {order_number_in_progress}")
        assert f"0{order_number}" in order_number_in_progress, "Заказа пользователя нет в разделе 'В работе'"
