import time
import random

from pages.base_page import BasePage
from locators.form_locator import FormPageLocator as Locators


class FormPage(BasePage):

    def fill_fields_and_submit(self):
        user_name_test = ['zdgg', '0gzd', '0025', 'vvvvbvvvvvbvvvvvbvvvvvbvvvvvbvvvvvbv',
                          '2vvvbvvvvvbvvvvvbvvvvvbvvvvvbvvvvvbv', '000000000000000000000000000000000',
                          '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', '!!!!']
        email_test = ['somebody@gmail.com', '745754775', 'somebody@mail.ru']
        password_test = ['1234567', '!!!!!', '@@@@hhdhd', 'jjjj_  _']
        referal_test = ['  ', '735737', 'jjfgjfgjfrdjetrjterj', 'jj', '!!!!!!']
        self.element_is_visible(Locators.user_name).send_keys(random.choice(user_name_test))
        self.element_is_visible(Locators.email).send_keys(random.choice(email_test))
        self.element_is_visible(Locators.password).send_keys(random.choice(password_test))
        self.element_is_visible(Locators.referal).send_keys(random.choice(referal_test))
        self.element_is_visible(Locators.polit_assert).click()
        self.element_is_visible(Locators.submit).click()
        time.sleep(5)
        return user_name_test, email_test, password_test

    def form_result(self):
        result_list = self.element_is_visible()
        result_text = [i.text for i in result_list]
        return result_text
