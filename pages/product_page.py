from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def should_be_added_to_basket(self):
        self.should_be_add_button()
        self.should_be_clicked_add_button()        
        self.should_be_equal_title(self.get_element_text(*ProductPageLocators.PRODUCT_TITLE))
        self.should_be_equal_price(self.get_element_text(*ProductPageLocators.PRODUCT_PRICE))

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button not exist"

    def should_be_clicked_add_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def should_be_equal_title(self, value):
        message_title = self.get_element_text(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_TITLE)
        assert message_title == value, f"Added product title {message_title} not the same as product title {value}"

    def should_be_equal_price(self, value):
        basket_summ = self.get_element_text(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_PRICE)
        assert basket_summ == value, f"Basket summ {basket_summ} not the same as product price {value}"



