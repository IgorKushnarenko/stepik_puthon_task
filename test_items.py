import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_visibility_of_button_for_adding_to_basket(browser):
    browser.get(link)
    button_for_adding_to_basket = browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(button_for_adding_to_basket) == 1, 'There is no button for adding to basket on page or selector doesn"t unique'