import random

from locators.interection_page_locators import SortablePageLocators, SelectablePageLocators, ResizeblePageLocators
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
        width = value_of_size.split(';')[0].split(':')[1].replace(' ','')
        heigh = value_of_size.split(';')[1].split(':')[1].replace(' ','')
        return width, heigh

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resible_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZEBLE_BOX_HANDLE), 400,200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZEBLE_BOX))

        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZEBLE_BOX_HANDLE),-400,-200)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZEBLE_BOX))
        return max_size, min_size

    def change_size_resible(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZEBLE_HANDLE),
                                            random.randint(1,300), random.randint(1,300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.HANDLE))

        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZEBLE_HANDLE),
                                            random.randint(-200,-1), random.randint(-200,-1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.HANDLE))
        return max_size, min_size