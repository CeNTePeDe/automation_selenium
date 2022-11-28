from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMAMENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created forms
    CREATED_FULL_NAME = (By.XPATH, "//p[@id='name']")
    CREATED_EMAIL = (By.XPATH, "//p[@id='email'] ")
    CREATED_CURRENT_ADDRESS = (By.XPATH, "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.XPATH, "//p[@id='permanentAddress']")


class CheckBoxPageLocators:
    EXPEND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    NO_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")


class WebTablesPageLocators:
    # локаторы, для добовления человека
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id ="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id ="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id ="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id ="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id ="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id ="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id ="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # tables
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    # seach
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')
    # delete
    DELETE_TEXT = (By.CSS_SELECTOR, 'div[class="rt-noData"]')

    COUNT = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')


class ButtonsPageLocators:
    DOUBLE_BUTTON_CLICK = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By.XPATH, '//div[3]/button')
    # result
    SUCCESS_DOUBLE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    SUCCESS_RIGHT = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    SUCCESS_CLICK_ME = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')


class LinkPageLocators:
    HOME_LINK = (By.XPATH, "//a[@id='simpleLink']")
    HOME_LINK_ZAYQD = (By.XPATH, "//a[@id='dynamicLink']")

    CREATED = (By.XPATH, "//a[@id='created']")
    NO_CONTENT = (By.XPATH, "//a[@id='no-content']")
    MOVED = (By.XPATH, "//a[@id='moved']")
    BAD_REQUEST = (By.XPATH, "//a[@id='bad-request']")
    UNAUTHORIZED = (By.XPATH, "//a[@id='unauthorized']")
    FORBITTEN = (By.XPATH, "//a[@id='forbidden']")
    NOT_FOUND = (By.XPATH, "invalid-url")
