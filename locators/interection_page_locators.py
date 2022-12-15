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

class ResizeblePageLocators:
    RESIZEBLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZEBLE_BOX_HANDLE = (By.CSS_SELECTOR,
        'div[id= "resizableBoxWithRestriction"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZEBLE_HANDLE = (By.CSS_SELECTOR,
         'div[id= "resizable"] [class="react-resizable-handle react-resizable-handle-se"]')
    HANDLE = (By.CSS_SELECTOR, 'div[id= "resizable"] ')

class DropablePageLocators:
    #TABS:
    SIMPLE_TABS = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    ACCEPT_TABS = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    PREVENT_TABS = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    REVERT_DRAGGABLE_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-revertable"]')

    #simple tabs
    DRAG_ME = (By.CSS_SELECTOR, 'div[id="draggable"]')
    DROPED = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')

    #accept tabs
    ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    DROP_HER = (By.CSS_SELECTOR, '#acceptDropContainer #droppable')

    #prevent propogation
    NOT_GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p:nth-child(1)')
    NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p:nth-child(1)')
    GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, '#ppDropContainer #dragBox')

    #revert dragable
    WILL_REVERT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVERT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    DROP_HERE_REVERT = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')