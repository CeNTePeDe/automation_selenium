from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    NEW_WINDOW_MESSAGE = (By.CSS_SELECTOR, 'button[id="messageWindowButton"]')

    TEXT_PAGE = (By.CSS_SELECTOR, 'h1[id = "sampleHeading"]')


class AlertsPageLocators:
    ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    TIME_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    PROMT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')

    CONFIRM_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMT_RESULT = (By.CSS_SELECTOR, 'span[id = "promptResult"]')


class FramePageLocator:
    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame2"]')

    TITLE_FRAME = (By.CSS_SELECTOR, 'h1[id = "sampleHeading"]')


class NestedFramePageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    FIRST_FRAME_TEXT = (By.CSS_SELECTOR, 'body')

    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    SECOND_FRAME_TEXT = (By.CSS_SELECTOR, 'p')

class ModalDialogPageLocators:
    SMALL_MODAL = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    SMALL_MODAL_TEXT = (By.CSS_SELECTOR, 'div[class = "modal-body"]')
    CLOSE_SMALL_BUTTON = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')

    LARGE_MODAL = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    LARGE_MODAL_TEXT = (By.CSS_SELECTOR, 'p[class]')
    CLOSE_LARGE_BUTTON = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')

