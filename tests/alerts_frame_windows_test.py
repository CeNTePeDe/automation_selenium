import time

from pages.alerts_fram_win_page import BrowserWindowsPage, AlertsPage, FramePage, NestedFramePage, ModalDialogPage


class TestAlertsFrameWindow:
    class TestBrowserWindows:

        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_open_new_tab()
            assert text_result == 'This is a sample page'

        def test_new_window(self, driver):
            new_window = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_window.open()
            text_result = new_window.check_opened_new_window()
            assert text_result == 'This is a sample page'

    class TestAlertPage:

        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text = alert_page.check_see_alert()
            assert text == 'You clicked a button'

        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text = alert_page.check_alert_appear_5_sec()
            assert text == 'This alert appeared after 5 seconds'

        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text = alert_page.check_confirm_alert()
            assert text == 'You selected Ok'

        def test_alert_promt_result(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, text_result = alert_page.check_alert_promt_result()
            assert text_result == f'You entered {text}'
            assert text in text_result

    class TestFramePage:
        def test_frames(self, driver):
            frame_page = FramePage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result1 = frame_page.check_frame('frame1')
            result2 = frame_page.check_frame('frame2')
            assert result1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
            assert result2 == ['This is a sample page', '100px', '100px'], 'The frame does not exist'

    class TestNestedFramePage:
        def test_nested_frame(self, driver):
            nested_frame_page = NestedFramePage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent frame', 'Nested frame does not exist'
            assert child_text == 'Child Iframe', 'Nested frame does not exist'

    class TestModalDialog:
        def test_modal_dialog(self, driver):
            modal_dialog_page = ModalDialogPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog_page.open()
            text_small_modal_dialog, text_large_modal_dialog = modal_dialog_page.check_modal_dialog_button()

            assert text_large_modal_dialog[
                   :74] == "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
            assert text_small_modal_dialog == "This is a small modal. It has very less content"
