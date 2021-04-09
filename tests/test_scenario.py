from pageObjects.login_page import LoginPage
import pytest


@pytest.mark.usefixtures("setup", "logger")
class TestUserLogin:

    def test_invalid_login(self, invalid_login_data):
        login_page = LoginPage(self.driver)
        login_page.setUsername(invalid_login_data[0])
        login_page.setPassword(invalid_login_data[1])
        login_page.clickLoginButton()

        if self.driver.current_url != "https://www.saucedemo.com/inventory.html":
            self.log.info(f":{self.__class__.test_invalid_login.__name__}: {[*invalid_login_data]} :: TEST PASSED")
            assert True
        else:
            self.log.info(f":{self.__class__.test_invalid_login.__name__}: {[*invalid_login_data]} :: TEST FAILED")
            self.driver.back()
            assert False

    def test_valid_login(self, valid_login_data):
        login_page = LoginPage(self.driver)
        login_page.setUsername(valid_login_data[0])
        login_page.setPassword(valid_login_data[1])
        login_page.clickLoginButton()

        if self.driver.current_url == "https://www.saucedemo.com/inventory.html":
            self.log.info(f":{self.__class__.test_valid_login.__name__}: {[*valid_login_data]} :: TEST PASSED")
            self.driver.back()
            assert True
        else:
            self.log.info(f":{self.__class__.test_valid_login.__name__}: {[*valid_login_data]} :: TEST FAILED")

            assert False
