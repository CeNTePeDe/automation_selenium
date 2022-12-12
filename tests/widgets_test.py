import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, ProgressBarPage, SliderPage, TabsPage, \
    ToolTipPage, MenuItemPage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title or missing text'
            assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title or missing text'
            assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title or missing text'

    class TestAutoCompletePage:

        def test_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            colors = auto_complete_page.fill_input_multi()
            colors_result = auto_complete_page.check_color_in_multi()
            assert colors == colors_result, 'the added colors are missing in the input'

        def test_remove_value_from_multi(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()
            assert count_value_before != count_value_after, 'value was not deleted'

        def test_fill_single(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color = auto_complete_page.fill_input_single()
            color_result = auto_complete_page.check_color_in_single()
            assert color == color_result, 'the added colors are missing in the input'

    class TestDatePicker:
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date_before, date_after = date_picker_page.select_date()
            assert date_before != date_after, 'The date and time has not been changed'

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date_before, date_after = date_picker_page.select_date_and_time()
            print(date_before)
            print(date_after)
            assert date_before != date_after, 'The date and time has not been changed'

    class TestSlider:
        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            values_before, values_after = slider_page.change_slider_value()
            assert values_before != values_after, 'Slider has not been changed'

    class TestProgressBar:
        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            value_before, value_after = progress_bar.change_progress_bar_value()
            print(value_before)
            print(value_after)
            assert value_before != value_after, 'Progress bar has not been changed'

    class TestTabs:
        def test_tabs(self, driver):
            tabs = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs.open()
            what_tab_text, origin_tab_text, use_tab_text = tabs.change_tabs()
            assert what_tab_text == 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
            assert origin_tab_text == 'Contrary to popular belief, Lorem Ipsum is not simply random text.'
            assert use_tab_text == 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.'

    class TestToolTip:
        def test_tool_tip(self, driver):
            tool_tab = ToolTipPage(driver, 'https://demoqa.com/tool-tips')
            tool_tab.open()
            tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section = tool_tab.check_tools()
            print(tool_tip_text_button) # == "You hovered over the Button", 'hover missing oe incorrect content'
            print(tool_tip_text_field) # == "You hovered over the text field", 'hover missing oe incorrect content'
            print(tool_tip_text_contrary) # == "You hovered over the Contrary", 'hover missing oe incorrect content'
            print(tool_tip_text_section) # == "You hovered over the 1.10.32", 'hover missing oe incorrect content'

    class TestMenuItem:
        def test_menu_item(self, driver):
            menu_item = MenuItemPage(driver, 'https://demoqa.com/menu')
            menu_item.open()
            data = menu_item.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3']
