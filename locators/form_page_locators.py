import random

from selenium.webdriver.common.by import By


class FormPageLocators:
    FIRST_NAME = (By.XPATH, '//input[@placeholder="First Name"]')
    LAST_NAME = (By.XPATH, '//input[@placeholder="Last Name"]')
    EMAIL = (By.XPATH, '//input[@placeholder="name@example.com"]')
    GENDER = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']")
    MOBILE = (By.XPATH, '//input[@placeholder="Mobile Number"]')
    DATE_OF_BIRTH = (By.XPATH, '//input[@id="dateOfBirthInput"]')
    SUBJECT = (By.XPATH, '//input[@id="subjectsInput"]')
    HOBBIES = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='hobbies-checkbox-{random.randint(1, 3)}']")
    FILE_INPUT = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
    CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_SITY = (By.CSS_SELECTOR, 'div[id="city"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')

    # result
    # RESULT_TABLE=
