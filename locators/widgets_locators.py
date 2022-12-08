from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_1 = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SECTION_2 = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECTION_3 = (By.CSS_SELECTOR, 'div[id="section3Heading"]')

    SECTION_1_CONTENT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECTION_2_CONTENT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    SECTION_3_CONTENT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')

class AutoCompletePageocators:
    MULTI_COLOR_NAMES =(By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')

    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_COLOR_NAME = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
