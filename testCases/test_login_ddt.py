import time
import openpyxl
import pytest

from pageObject.Loginpage import Login
from Utilitis.Readconfigfile import Readvalue
from Utilitis.Logger import LogGen
from Utilitis import Xlutils


class Test_ddt:

    url = Readvalue.get_url()
    path = "C:\\Users\\Anand\\PycharmProjects\\OrangeHRM\\TestData\\Login.xlsx"
    log = LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_ddt_login__003(self,setup):
        self.driver = setup
        self.log.info("Opening Browser")
        self.driver.get(self.url)
        self.log.info("Going To URL")
        self.lp = Login(self.driver)
        self.row= Xlutils.getrowCount(self.path, "Sheet1")
        print("Number of row are--->", +self.row)

        login_status = []

        for r in range(2, self.row+1):
            self.username = Xlutils.readData(self.path, "Sheet1", r, 1)
            self.password = Xlutils.readData(self.path, "Sheet1", r, 2)
            self.Exp_status = Xlutils.readData(self.path, "Sheet1", r, 3)

            self.lp.Enter_username(self.username)
            self.log.info("Enter UserName-->" + self.username)
            self.lp.Enter_password(self.password)
            self.log.info("Enter Password-->" + self.password)
            self.lp.click_login_button()
            self.log.info("Click on login button")

            if self.lp.login_status()==True:
                if self.Exp_status == "Pass":
                    login_status.append("Pass")
                    self.driver.save_screenshot("C:\\Users\\Anand\\PycharmProjects\\OrangeHRM\\Screenshots\\test_ddt_login__003_Pass.png")
                    self.lp.click_menu_button()
                    self.log.info("Click on Menu Button")
                    self.lp.click_logout()
                    self.log.info("Click on logout Button")
                    Xlutils.writeData(self.path, "Sheet1", r, 4, "Pass")
                elif self.Exp_status == "Fail":
                    login_status.append("Fail")
                    self.driver.save_screenshot("C:\\Users\\Anand\\PycharmProjects\\OrangeHRM\\Screenshots\\test_ddt_login__003_Fail.png")
                    self.lp.click_menu_button()
                    self.log.info("Click on Menu Button")
                    self.lp.click_logout()
                    self.log.info("Click on logout button")
                    Xlutils.writeData(self.path, "Sheet1", r, 4, "Fail")
            else:
                if self.Exp_status == "Fail":
                    login_status.append("Pass")
                    Xlutils.writeData(self.path, "Sheet1", r, 4, "Fail")
                elif self.Exp_status == "Pass":
                    login_status.append("Fail")
                    Xlutils.writeData(self.path, "Sheet1", r, 4, "Pass")

        if "Fail" not in login_status:
            self.log.info("test_login_params_003 is Passed")
            assert True
        else:
            self.log.info("test_login_params_003 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_login_params_003 is Completed")