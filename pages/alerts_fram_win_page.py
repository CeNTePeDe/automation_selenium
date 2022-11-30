from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators
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
