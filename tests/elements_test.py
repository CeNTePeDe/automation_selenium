import time
from pages.element_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            test_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            test_box_page.open()
            input_data = test_box_page.fill_all_fields()
            output_data = test_box_page.check_fieled_form()
            assert input_data == output_data

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_checkbox = check_box_page.get_output_result()
            assert input_checkbox == output_checkbox, 'checkboxes have not been selected'

    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()

            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()

            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()

            assert output_yes == 'Yes', "'yes' have not been seleted"
            assert output_no == 'No', "'no' have not been seleted"
            assert output_impressive == 'Impressive', "'impressive' have not been seleted"

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_person_page =  WebTablePage(driver, 'https://demoqa.com/webtables')
            web_person_page.open()
            new_person = web_person_page.add_new_person()
            table_result = web_person_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result




