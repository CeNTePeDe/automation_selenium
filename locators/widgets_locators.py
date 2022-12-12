import random

from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_1 = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SECTION_2 = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECTION_3 = (By.CSS_SELECTOR, 'div[id="section3Heading"]')

    SECTION_1_CONTENT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECTION_2_CONTENT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    SECTION_3_CONTENT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompletePageocators:
    MULTI_COLOR_NAMES = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')

    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_COLOR_NAME = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')


class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"] ')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')


class SliderPageLocators:
    SLIDER_VALUE_RANGE = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')


class ProgressBarPageLocators:
    BUTTON_START = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')


class TabsPageLocators:
    WHAT_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    ORIGIN_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    USE_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')

    WHAT_TAB_TEXT = (By.XPATH, '//div[@id="demo-tabpane-what"]')
    ORIGIN_TAB_TEXT = (By.XPATH, '//div[@id="demo-tabpane-origin"] ')
    USE_TAB_TEXT = (By.XPATH, '//div[@id="demo-tabpane-use"] ')

class ToolTipPageLocatorts:

    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    BUTTON_TEXT = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    INPUT_FIELD = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    INPUT_FIELD_TEXT = (By.CSS_SELECTOR, 'button[aria-describedby="textFieldToolTip"]')

    LINK_CONTRARY = (By.XPATH, ' //*[.="Contrary"]')
    LINK_CONTRARY_TEXT = (By.CSS_SELECTOR,'button[aria-describedby="contraryTexToolTip"]' )

    LINK_SECTION = (By.XPATH, ' //*[.="1.10.32"] ')
    LINK_SECTION_TEXT = (By.CSS_SELECTOR,'button[aria-describedby="sectionToolTip"]' )

    TOOL_TIPS_INNER = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')


class MenuItemPageLocators:
    MENU_ITEM_1 = (By.CSS_SELECTOR, 'ul[id="nav"] li a')

