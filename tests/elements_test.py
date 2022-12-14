import random
import time
from pages.element_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadDownloadPage, DinamicPropertiesPage


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

            assert output_yes == 'Yes', "'yes' have not been seleсted"
            assert output_no == 'No', "'no' have not been seleсted"
            assert output_impressive == 'Impressive', "'impressive' have not been seleсted"

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_seach_person()
            print(key_word)
            print(table_result)
            assert key_word in table_result, "the person was not found in the table"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_seach_person()
            assert age in row, "the person card has not been changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == 'No rows found'

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], "The numbers of rows in the table has not " \
                                                      "been changed or has chenged incorrectly"

    class TestButtonPage:

        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            print(double)
            print(right)
            print(click)
            assert double == "You have done a double click", "The double click button was not press"
            assert right == "You have done a right click", "The right click button was not press"
            assert click == "You have done a dynamic click", "The dynamic click button was not press"

    class TestLinksPage:

        def test_check_link(self, driver):
            link_page = LinksPage(driver, 'https://demoqa.com/links')
            link_page.open()
            href_link, current_url = link_page.check_new_simple_link()
            assert href_link == current_url, 'the link is broken or url is incorrect'

        def test_broken_link(self, driver):
            link_page = LinksPage(driver, 'https://demoqa.com/links')
            link_page.open()
            response_code = link_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, 'the link is broken or url is incorrect'

    class TestUploadAndDownload:

        def test_upload(self, driver):
            upload_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_page.open()
            file_name, result = upload_page.upload_file()

            assert file_name == result, 'the file has not been uploaded'

        def test_download(self, driver):
            download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            download_page.open()
            check = download_page.download_file()
            assert check is True, 'the file has not been downloaded'

    class TestDynamicPropities:

        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DinamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            before, after = dynamic_properties_page.check_changed_of_color()
            dynamic_properties_page.check_appear_button()
            assert before != after, "colors have not been changed"

        def test_appear_button(self, driver):
            appear_button = DinamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            appear_button.open()
            appear = appear_button.check_appear_button()
            assert appear is True, "button did not appear after 5 second"

        def test_enable_button(self, driver):
            enable_button = DinamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            enable_button.open()
            enable = enable_button.check_enable_button()
            assert enable is True, "button did not open"
