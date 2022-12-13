from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST_TABS = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    ITEM_LIST_TABS = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')
    GRID_TABS = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_TABS_LIST = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')
