import random
import re
import time

from locators.interection_page_locators import SortablePageLocators, SelectablePageLocators, ResizeblePageLocators, \
    DropablePageLocators, TestDropablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable(self, element):
        item_list = self.elements_are_visible(element)
        return [item.text for item in item_list]

    def change_order(self, locator_tab, locator_item):
        self.element_is_visible(locator_tab).click()
        order_before = self.get_sortable(locator_item)
        item_list = random.sample(self.elements_are_visible(locator_item), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable(locator_item)
        return order_before, order_after

    def change_order_item(self):
        order_before_list, order_after_list = self.change_order(self.locators.LIST_TABS, self.locators.ITEM_LIST_TABS)
        order_before_grid, order_after_grid = self.change_order(self.locators.GRID_TABS, self.locators.GRID_TABS_LIST)
        return order_before_list, order_after_list, order_before_grid, order_after_grid


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self):
        self.element_is_visible(self.locators.LIST_TAB).click()
        self.click_selectable_item(self.locators.LIST_TAB_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_TAB_ITEM_ACTIVE)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        self.click_selectable_item(self.locators.GRID_TAB_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_TAB_ITEM_ACTIVE)
        return active_element.text


class ResizeblePage(BasePage):
    locators = ResizeblePageLocators()

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        heigh = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, heigh

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resible_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZEBLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZEBLE_BOX))

        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZEBLE_BOX_HANDLE), -400, -200)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZEBLE_BOX))
        return max_size, min_size

    def change_size_resible(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZEBLE_HANDLE),
                                            random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.HANDLE))

        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZEBLE_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.HANDLE))
        return max_size, min_size


class DropablePage(BasePage):
    locators = DropablePageLocators()

    def drop_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TABS)
        drag_div = self.element_is_visible(self.locators.DRAG_ME)
        drop_div = self.element_is_visible(self.locators.DROPED)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def accept_droppable(self):
        self.element_is_clickable(self.locators.ACCEPT_TABS).click()
        acceptable_div = self.element_is_visible(self.locators.ACCEPTABLE)
        not_acceptable_div = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HER)
        self.action_drag_and_drop_to_element(not_acceptable_div, drop_div)
        drop_text_not_accept = drop_div.text
        self.action_drag_and_drop_to_element(acceptable_div, drop_div)
        drop_text_accept = drop_div.text
        return drop_text_accept, drop_text_not_accept

    def drop_prevent_propogation(self):
        self.element_is_clickable(self.locators.PREVENT_TABS).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedy_inner_box = self.element_is_visible(self.locators.NOT_GREEDY_INNER_BOX)
        greedy_inner_box = self.element_is_visible(self.locators.GREEDY_INNER_BOX)
        self.action_drag_and_drop_to_element(drag_div, not_greedy_inner_box)
        text_not_greedy_box = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX_TEXT).text
        text_not_greedy_inner_box = not_greedy_inner_box.text
        self.action_drag_and_drop_to_element(drag_div, greedy_inner_box)
        text_greedy_box = self.element_is_visible(self.locators.GREEDY_DROP_BOX_TEXT).text
        text_greedy_inner_box = not_greedy_inner_box.text
        return text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box

    def drop_revert_draggable(self, type_drag):
        drags = {'will':
                     {'revert': self.locators.WILL_REVERT},
                 'not_will':
                     {'revert': self.locators.NOT_REVERT}
                 }
        self.element_is_visible(self.locators.REVERT_DRAGGABLE_TAB).click()
        revert = self.element_is_visible(drags[type_drag]['revert'])
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(revert, drop_div)
        position_after_move = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_after_revert, position_after_move


class DraggablePage(BasePage):
    locators = TestDropablePageLocators()

    def drag_me(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()

        drag = self.element_is_visible(self.locators.DRAG_ME)
        self.action_drag_and_drop_by_offset(drag, random.randint(0, 200), random.randint(0, 200))
        drag_before = drag.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag, random.randint(0, 200), random.randint(0, 200))
        drag_after = drag.get_attribute('style')
        return drag_before, drag_after

    def get_before_and_after_position(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 100), random.randint(0, 100))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 100), random.randint(0, 100))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    def get_top_position(self, position):
        return re.findall(r'\d[0-9]|\d', position.split(';')[2])

    def get_left_position(self, position):
        return re.findall(r'\d[0-9]|\d', position.split(';')[1])

    def axis_restricted_x(self):
        self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).click()
        only_x = self.element_is_visible(self.locators.ONLY_X)
        position_x = self.get_before_and_after_position(only_x)

        top_x_before = self.get_top_position(position_x[0])
        top_x_after = self.get_top_position(position_x[1])
        left_x_before = self.get_left_position(position_x[0])
        left_x_after = self.get_left_position(position_x[1])
        return [top_x_before, top_x_after], [left_x_before, left_x_after]

    def axis_restricted_y(self):
        self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).click()
        only_y = self.element_is_visible(self.locators.ONLY_Y)
        position_y = self.get_before_and_after_position(only_y)

        top_y_before = self.get_top_position(position_y[0])
        top_y_after = self.get_top_position(position_y[1])
        left_y_before = self.get_left_position(position_y[0])
        left_y_after = self.get_left_position(position_y[1])
        return [top_y_before, top_y_after], [left_y_before, left_y_after]

