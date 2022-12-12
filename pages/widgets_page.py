import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_locators import AccordianPageLocators, AutoCompletePageocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipPageLocatorts, MenuItemPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first': {'title': self.locators.SECTION_1,
                               'content': self.locators.SECTION_1_CONTENT},
                     'second': {'title': self.locators.SECTION_2,
                                'content': self.locators.SECTION_2_CONTENT},
                     'third': {'title': self.locators.SECTION_3,
                               'content': self.locators.SECTION_3_CONTENT}
                     }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return section_title.text, len(section_content)


class AutoCompletePage(BasePage):
    locators = AutoCompletePageocators()

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 4))
        for color in colors:
            input_multi = self.element_is_visible(self.locators.MULTI_COLOR_NAMES)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.RETURN)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_presents(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_COLOR_NAME)
        input_single.send_keys(color)
        input_single.send_keys(Keys.RETURN)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute("value")
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute("value")
        return value_date_before, value_date_after

    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute("value")
        input_date.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
        value_date_after = input_date.get_attribute("value")
        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_presents(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_VALUE_RANGE)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(0, 100), 0)

        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        progress_bar = self.element_is_clickable(self.locators.BUTTON_START)
        progress_bar.click()
        time.sleep(random.randint(2, 5))
        progress_bar.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def change_tabs(self):
        what_tab_text = self.element_is_visible(self.locators.WHAT_TAB_TEXT).text[:74]
        origin_tab = self.element_is_clickable(self.locators.ORIGIN_TAB).click()
        origin_tab_taxt = self.element_is_visible(self.locators.ORIGIN_TAB_TEXT).text[:66]
        use_tab = self.element_is_clickable(self.locators.USE_TAB).click()
        use_tab_text = self.element_is_visible(self.locators.USE_TAB_TEXT).text[:124]
        return what_tab_text, origin_tab_taxt, use_tab_text


class ToolTipPage(BasePage):
    locators = ToolTipPageLocatorts()

    def get_text_from_tool_tips(self, hover_elem, wait_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        #self.element_is_visible(wait_elem)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNER)
        text = tool_tip_text.text
        return text

    def check_tools(self):
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.BUTTON, self.locators.BUTTON_TEXT)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.INPUT_FIELD, self.locators.INPUT_FIELD_TEXT)
        tool_tip_text_contrary = self.get_text_from_tool_tips(self.locators.LINK_CONTRARY,
                                                              self.locators.LINK_CONTRARY_TEXT)
        tool_tip_text_section = self.get_text_from_tool_tips(self.locators.LINK_SECTION,
                                                             self.locators.LINK_SECTION_TEXT)

        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section


class MenuItemPage(BasePage):
    locators = MenuItemPageLocators()

    def check_menu(self):
        menu_item_list = self.elements_are_presents(self.locators.MENU_ITEM_1)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data
