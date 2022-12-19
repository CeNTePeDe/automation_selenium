import random

from pages.interection_page import SortablePage, SelectablePage, ResizeblePage, DropablePage, DraggablePage


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

    class TestResizeblePage:
        def test_resizeble_page(self, driver):
            resizeble_page = ResizeblePage(driver, 'https://demoqa.com/resizable')
            resizeble_page.open()
            max_box, min_box = resizeble_page.change_size_resible_box()
            max_resize, min_resize = resizeble_page.change_size_resible()
            assert ('500px', '300px') == max_box, "maximum size not equal to '500px', '300px'"
            assert ('150px', '150px') == min_box, "maximum size not equal to '150px', '150px'"
            assert min_resize != max_resize, "resizeble has not been changed"

    class TestDropablePage:
        def test_dropable_page(self, driver):
            dropable_page = DropablePage(driver, 'https://demoqa.com/droppable')
            dropable_page.open()
            text = dropable_page.drop_simple()
            assert text == 'Dropped!', 'the element has not been dropped'

        def test_accept_droppable(self, driver):
            dropable_page = DropablePage(driver, 'https://demoqa.com/droppable')
            dropable_page.open()
            accept, not_accept = dropable_page.accept_droppable()
            assert accept == "Dropped!", 'the dropped element has not been accepted'
            assert not_accept == "Drop here", 'the dropped element has been accepted'

        def test_prevent_propogation_dropable(self, driver):
            dropable_page = DropablePage(driver, 'https://demoqa.com/droppable')
            dropable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = dropable_page.drop_prevent_propogation()
            assert not_greedy == 'Dropped!', 'the elements has not been changed'
            assert not_greedy_inner == 'Dropped!', 'the elements has not been changed'
            assert greedy == 'Outer droppable', 'the elements has been changed'
            assert greedy_inner == 'Dropped!', 'the elements has not been changed'

        def test_revert_draggable_droppable(self, driver):
            droppable_page = DropablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will')
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will')
            assert will_after_move != will_after_revert, 'the element has not reverted'
            assert not_will_after_move == not_will_after_revert, 'the element has reverted'

    class TestDraggablePage:

        def test_drag_me(self, driver):
            dragable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            dragable_page.open()
            drag_before, drag_after = dragable_page.drag_me()
            assert drag_before != drag_after, "the position of the box has not been changed"

        def test_change_coordinate(self, driver):
            dragable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            dragable_page.open()
            top_x, left_x =dragable_page.axis_restricted_x()
            top_y, left_y =dragable_page.axis_restricted_y()
            assert top_x[0][0] == top_x[1][0] and int(
                top_x[1][0]) == 0, 'box position has not changed has been a shift in the y-axis'
            assert left_x[0][0] != left_x[1][0] and int(
                left_x[1][0]) != 0, 'box position has not changed has been a shift in the y-axis'
            assert top_y[0][0] != top_y[1][0] and int(
                top_y[1][0]) != 0, 'box position has not changed has been a shift in the x-axis'
            assert left_y[0][0] == left_y[1][0] and int(
                left_y[1][0]) == 0, 'box position has not changed has been a shift in the x-axis'









