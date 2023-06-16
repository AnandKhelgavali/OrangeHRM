import pytest

from pageObject.Loginpage import Login
from Utilitis.Readconfigfile import Readvalue
from Utilitis.Logger import LogGen

class Test_login_param_004:
    url = Readvalue.get_url()
    log = LogGen.loggen()

    @pytest.mark.regression
    def test_login_param_004(self,setup,getDataForLogin):
        self.log.info("Opening Browser")
        self.driver = setup
        self.driver.get(self.url)
        self.log.info("Geting url")
        self.lp = Login(self.driver)
        self.lp.Enter_username(getDataForLogin[0])
        self.log.info("Enter Username -->" + (getDataForLogin[0]))
        self.lp.Enter_password(getDataForLogin[1])
        self.log.info("enter Password --->" + (getDataForLogin[1]))
        self.lp.click_login_button()
        self.log.info("Click On Login button")
        login_status=[]
        if self.lp.login_status()==True:
            if getDataForLogin[2] == "Pass":
                login_status.append("Pass")
                self.driver.save_screenshot("C:\\Users\Anand\\PycharmProjects\\OrangeHRM\\Screenshots\\test_login_params_004_pass.png")
                self.lp.click_menu_button()
                self.log.info("Clik on menu Button")
                self.lp.click_logout()
                self.log.info("Click on LogOut Button")
            elif getDataForLogin[2] == "Fail":
                login_status.append("Fail")
                self.driver.save_screenshot("C:\\Users\Anand\\PycharmProjects\\OrangeHRM\\Screenshots\\test_login_params_004_Fail.png")
                self.lp.click_menu_button()
                self.log.info("Click On Menu button")
                self.lp.click_logout()
                self.log.info("click on Logout Button")

        else:
            if getDataForLogin[2] == "Fail":
                login_status.append("Pass")
                self.driver.save_screenshot("C:\\Users\Anand\\PycharmProjects\\OrangeHRM\\Screenshots\\test_login_params_004_pass.png")
            elif getDataForLogin[2] == "pass":
                login_status.append("Fail")
                self.driver.save_screenshot("C:\\Users\Anand\\PycharmProjects\\OrangeHRM\\Screenshots\\test_login_params_004_pass.png")
            print(login_status)

        if "Fail" not in login_status:
            self.log.info("test_login_params_003 is Passed")
            assert True
        else:
            self.log.info("test_login_params_003 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_login_params_003 is Completed")