from selenium.webdriver.common.by import By


class OrderFeedsPageLocators:
    ORDER_1 = [By.XPATH,
               "//*[@id='root']/div/main/div/div/ul/li[1]"]  # Первый заказ в списке заказов

    POPUP_WINDOW_WITH_DETAILS = [By.XPATH,
                                 "//p[text()='Cостав']"]  # всплывающее окно с деталями "Состав"
