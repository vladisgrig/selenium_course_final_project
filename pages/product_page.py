from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def should_be_added_to_basket(self):
        self.should_be_add_button()
        self.should_be_clicked_add_button()
        self.should_be_basket_summ_equal_product_price()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button not exist"

    def should_be_clicked_add_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        added_product_title = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_TITLE).text
        assert title == added_product_title, "Added product have not the same title"

    def should_be_basket_summ_equal_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_summ = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_PRICE).text
        assert price == basket_summ, "Basket summ not equal price of added product"



