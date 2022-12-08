from locators.widgets_locators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):

    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':{'title': self.locators.SECTION_1,
                              'content': self.locators.SECTION_1_CONTENT},
                     'second':{'title': self.locators.SECTION_2,
                              'content': self.locators.SECTION_2_CONTENT},
                     'third':{'title': self.locators.SECTION_3,
                              'content': self.locators.SECTION_3_CONTENT}
                     }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return section_title.text, len(section_content)