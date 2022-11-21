from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL =(By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS =(By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMAMENT_ADDRESS =(By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT =(By.CSS_SELECTOR, "button[id='submit']")

    # created forms
    CREATED_FULL_NAME =(By.XPATH, "//p[@id='name']")
    CREATED_EMAIL =(By.XPATH, "//p[@id='email'] ")
    CREATED_CURRENT_ADDRESS =(By.XPATH, "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS =(By.XPATH, "//p[@id='permanentAddress']")


class CheckBoxPageLocators:
    EXPEND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHACEKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")