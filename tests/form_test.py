from pages.form_page import FormPage
from conftest import driver


class TestFormPage:

    def test_form(self, driver):
        form_page = FormPage(driver, 'https://koshelek.ru/authorization/signup')
        form_page.open()
        form_page.fill_fields_and_submit()
        user_name_test, email_test, password_test = form_page.fill_fields_and_submit()
        result = form_page.form_result()
        assert f'{user_name_test}'==result[0]
        assert f'{email_test}'==result[1]
        assert f'{password_test}' == result[2]
