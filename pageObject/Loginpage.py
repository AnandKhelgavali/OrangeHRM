from selenium.common import NoSuchElementException,TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Login:
    Text_username_Name = (By.NAME, "username")
    Text_Password_Name = (By.NAME, "password")
    Click_Login_Xpath = (By.XPATH, "//button[@type='submit']")
    Click_Menu_button = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    click_logout_button = (By.XPATH, "//a[normalize-space()='Logout']")


    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def Enter_username(self, username):
        self.wait.until(expected_conditions.presence_of_all_elements_located(self.Text_username_Name))
        self.driver.find_element(*Login.Text_username_Name).send_keys(username)

    def Enter_password(self, password):
        self.driver.find_element(*Login.Text_Password_Name).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*Login.Click_Login_Xpath).click()

    def login_status(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.Click_Menu_button))
            self.driver.find_element(*Login.Click_Menu_button)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def click_menu_button(self):
        self.driver.find_element(*Login.Click_Menu_button).click()

    def click_logout(self):
        self.driver.find_element(*Login.click_logout_button).click()






