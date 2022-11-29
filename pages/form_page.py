import os

from selenium.webdriver import Keys


from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.FIRST_NAME)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.LAST_NAME)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.EMAIL)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.MOBILE)
        self.element_is_visible(self.locators.SUBJECT).send_keys('Maths')
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.CURRENT_ADDRESS)

        self.go_to_element(self.element_is_present(self.locators.SELECT_STATE))
        self.element_is_visible(self.locators.SELECT_STATE).send_keys(Keys.RETURN)

        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_SITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)

        self.element_is_visible(self.locators.SUBMIT).click()
        return person