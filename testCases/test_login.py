import time

import pytest

from pageObject.Loginpage import Login
from Utilitis.Readconfigfile import Readvalue
from Utilitis.Logger import LogGen


class Test_Login:
    username = Readvalue.getusername()
    password = Readvalue.getpassword()
    url = Readvalue.get_url()
    log = LogGen.loggen()

    @pytest.mark.sanity
    def test_url_001(self, setup):
        self.log.info("Opening Browser")
        self.driver = setup
        self.driver.get(self.url)
        self.log.info("Going to url")
        time.sleep(2)
        self.log.info("checking Page title")
        if self.driver.title == "OrangeHRM":
            self.log.info("Test_url_001 passed")
            self.driver.save_screenshot("C:\\Users\\Anand\\PycharmProjects\\OrangeHRM\\Screenshots\\Tes_url_001_Pass.png")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\Anand\\PycharmProjects\\OrangeHRM\\Screenshots\\Tes_url_001_Failed.png")
            self.log.info("Test_url_001 failed")
            assert False

        self.driver.close()
        self.log.info("Url login Close")
        self.log.info("Test_Url_001_Completed")

    @pytest.mark.sanity
    def test_logout_002(self, setup):
        self.log.info("Opening Browser")
        self.driver = setup
        self.driver.get(self.url)
        self.log.info("going To URL")
        self.lp = Login(self.driver)
        time.sleep(2)
        self.log.info("Entering Username")
        self.lp.Enter_username(self.username)
        self.log.info("Entering Password")
        self.lp.Enter_password(self.password)
        self.log.info("Login success")
        self.lp.click_login_button()

        time.sleep(3)
        if self.lp.login_status() == True:
            self.driver.save_screenshot("C:\\Users\\Anand\\PycharmProjects\\OrangeHRM\\Screenshots\\Tes_url_002_Pass.png")
            self.log.info("Test_002_Passed")
            self.lp.click_menu_button()
            self.log.info("Click on menu Button")
            self.lp.click_logout()
            self.log.info("Click on Logout button")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\Anand\\PycharmProjects\\OrangeHRM\\Screenshots\\Tes_url_002_Failed.png")
            assert False
        self.driver.close()
        self.log.info("Test_login_002 completed")