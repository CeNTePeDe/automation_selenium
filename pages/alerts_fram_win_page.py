import random
import time

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramePageLocator, \
    NestedFramePageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locator = BrowserWindowsPageLocators()

    def check_open_new_tab(self):
        self.element_is_visible(self.locator.NEW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locator.TEXT_PAGE).text
        return text_title , 'the new tab has not opened or an incorrecttab has opened'

    def check_opened_new_window(self):
        self.element_is_visible(self.locator.NEW_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locator.TEXT_PAGE).text
        return text_title, 'the new tab has not opened or an incorrecttab has opened'

class AlertsPage(BasePage):

    locator = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locator.ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locator.TIME_ALERT_BUTTON).click()
        time.sleep(5)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locator.CONFIRM_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locator.CONFIRM_RESULT).text
        return text_result

    def check_alert_promt_result(self):
        text = f'hello, world {random.randint(1,98)}'
        self.element_is_visible(self.locator.PROMT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_visible(self.locator.PROMT_RESULT).text
        return text, text_result

class FramePage(BasePage):
    locators = FramePageLocator()

    def check_frame(self, fram_num):
        if fram_num == "frame1":
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            heigh = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, heigh]

        if fram_num == "frame2":
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            heigh = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, heigh]

class NestedFramePage(BasePage):
    locators = NestedFramePageLocators()

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.FIRST_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.FIRST_FRAME_TEXT).text

        child_frame = self.element_is_present(self.locators.SECOND_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.SECOND_FRAME_TEXT).text

        return parent_text, child_text
