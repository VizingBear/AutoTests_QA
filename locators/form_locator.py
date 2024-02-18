from selenium.webdriver.common.by import By


class FormPageLocator():
    user_name = (By.CSS_SELECTOR, '#input-3537')
    email = (By.CSS_SELECTOR, '#username')
    password = (By.CSS_SELECTOR, '#new-password')
    referal = (By.CSS_SELECTOR, '#input-563')
    polit_assert = (By.CSS_SELECTOR, '#input-575')
    submit = (By.CSS_SELECTOR, '.v-btn v-btn--block v-btn--has-bg v-btn--rounded v-btn--tile theme--light elevation-0 v-size--x-large')  # input-575

