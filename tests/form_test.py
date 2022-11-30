import time

from pages.form_page import FormPage


class TestForm:
    class TestFormPage:
        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()

            p = form_page.fill_form_fields()
            result = form_page.form_result()
            assert [result[0], result[1]] == [p.FIRST_NAME + ' ' + p.LAST_NAME, p.EMAIL], "the form has not been filled"
