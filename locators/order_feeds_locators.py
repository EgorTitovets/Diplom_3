from selenium.webdriver.common.by import By


class OrderFeedsPageLocators:
    ORDER_1 = [By.XPATH,
               "//*[@id='root']/div/main/div/div/ul/li[1]"]  # Первый заказ в списке заказов

    POPUP_WINDOW_WITH_DETAILS = [By.XPATH,
                                 "//p[text()='Cостав']"]  # всплывающее окно с деталями "Состав"

    ORDER_NUMBER_IN_ORDER_FEEDS = [By.XPATH,
                                   "//p[contains(@class, 'text_type_digits-default')]"]  # номер заказа в Ленте заказов

    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")  # popup с идентификатором номера заказа

    TOTAL_ORDERS_COUNT = [By.XPATH,
                          "//p[contains(@class, 'OrderFeed_number') and contains(@class, 'text_type_digits-large')]"]  # кол-во заказов за все время

    TODAY_ORDERS_COUNT = (
        By.XPATH,
        "(//p[contains(@class, 'OrderFeed_number') and contains(@class, 'text_type_digits-large')])[2]")  # кол-во заказов за сегодня

    ORDER_NUMBER_IN_PROGRESS = (By.XPATH, '//li[@class="text text_type_digits-default mb-2"]')  # номер заказа в работе
