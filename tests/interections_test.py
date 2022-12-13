import random

from pages.interection_page import SortablePage


class TestInteraction:
    class TestSortablePage:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before_list, order_after_list, order_before_grid, order_after_grid = sortable_page.change_order_item()
            assert order_before_list != order_after_list
            assert order_before_grid != order_after_grid


