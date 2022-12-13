from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST_TABS = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    ITEM_LIST_TABS = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')
    GRID_TABS = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_TABS_LIST = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')

class SelectablePageLocators:
    LIST_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_TAB_ITEM = (By.CSS_SELECTOR, 'li[class = "mt-2 list-group-item list-group-item-action"]')
    LIST_TAB_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class = "mt-2 list-group-item active list-group-item-action"]')

    GRID_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_TAB_ITEM = (By.CSS_SELECTOR, 'li[class = "list-group-item list-group-item-action"]')
    GRID_TAB_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class = "list-group-item active list-group-item-action"]')

