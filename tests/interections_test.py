import random

from pages.interection_page import SortablePage, SelectablePage


class TestInteraction:
    class TestSortablePage:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before_list, order_after_list, order_before_grid, order_after_grid = sortable_page.change_order_item()
            assert order_before_list != order_after_list
            assert order_before_grid != order_after_grid

    class TestSelectablePage:
        def test_selectable_page(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, 'no elements were selected'
            assert len(item_grid) > 0, 'no elements were selected'
