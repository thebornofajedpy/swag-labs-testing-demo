from selenium.webdriver.common.by import By
from pageObjects.login_page import LoginPage
from pageObjects.inventory_page import Inventory
import pytest


@pytest.mark.usefixtures("setup", "logger")
class TestScenario:

    def test_invalid_login(self, invalid_login_data):
        login_page = LoginPage(self.driver)
        login_page.setUsername(invalid_login_data[0])
        login_page.setPassword(invalid_login_data[1])
        login_page.clickLoginButton()

        if self.driver.current_url != "https://www.saucedemo.com/inventory.html":
            self.log.info(f":{self.test_invalid_login.__name__}: {[*invalid_login_data]} :: TEST PASSED")
            assert True
        else:
            self.log.info(f":{self.test_invalid_login.__name__}: {[*invalid_login_data]} :: TEST FAILED")
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

    def test_inventory_menu_about(self, standard_user_cred):
        login_page = LoginPage(self.driver)
        if self.driver.current_url != "https://www.saucedemo.com/":
            login_page.goToLoginPage()
        login_page.setUsername(standard_user_cred[0])
        login_page.setPassword((standard_user_cred[1]))
        login_page.clickLoginButton()

        inventory = Inventory(self.driver)
        inventory.clickBurgerButton()
        inventory.clickAbout()

        if self.driver.current_url == "https://saucelabs.com/":
            self.log.info(
                f":{self.__class__.test_inventory_menu_about.__name__}: {[*standard_user_cred]} :: TEST PASSED")
            self.driver.back()
            assert True
        else:
            self.log.info(
                f":{self.__class__.test_inventory_menu_about.__name__}: {[*standard_user_cred]} :: TEST FAILED")
            assert False

    def test_inventory_menu_logout(self, standard_user_cred):
        login_page = LoginPage(self.driver)
        if self.driver.current_url == "https://www.saucedemo.com/":
            login_page.setUsername(standard_user_cred[0])
            login_page.setPassword((standard_user_cred[1]))
            login_page.clickLoginButton()

        inventory = Inventory(self.driver)
        inventory.clickBurgerButton()
        inventory.clickLogout()

        if self.driver.current_url == "https://www.saucedemo.com/":
            self.log.info(
                f":{self.__class__.test_inventory_menu_logout.__name__}: {[*standard_user_cred]} :: TEST PASSED")
            assert True
        else:
            self.log.info(
                f":{self.__class__.test_inventory_menu_logout.__name__}: {[*standard_user_cred]} :: TEST FAILED")
            assert False

    def test_inventory_menu_x(self, standard_user_cred):
        login_page = LoginPage(self.driver)
        if self.driver.current_url == "https://www.saucedemo.com/":
            login_page.setUsername(standard_user_cred[0])
            login_page.setPassword((standard_user_cred[1]))
            login_page.clickLoginButton()

        inventory = Inventory(self.driver)
        inventory.clickBurgerButton()
        inventory.clickCloseX()

        if self.driver.find_element(By.CSS_SELECTOR, "div.bm-menu-wrap").get_attribute("aria-hidden") == "true":
            self.log.info(
                f":{self.__class__.test_inventory_menu_x.__name__}: {[*standard_user_cred]} :: TEST PASSED")
            assert True
        else:
            self.log.info(
                f":{self.__class__.test_inventory_menu_x.__name__}: {[*standard_user_cred]} :: TEST FAILED")
            assert False

    def test_inventory_cart_counter(self, standard_user_cred):
        login_page = LoginPage(self.driver)
        inventory = Inventory(self.driver)
        curl = self.driver.current_url

        if curl == "https://www.saucedemo.com/":
            login_page.setUsername(standard_user_cred[0])
            login_page.setPassword((standard_user_cred[1]))
            login_page.clickLoginButton()
        elif curl != "https://www.saucedemo.com/inventory.html":
            inventory.clickBurgerButton()
            inventory.clickAllItems()

        counter = inventory.clickAllCartButtons()
        cart_counter = inventory.getCartCounter()

        if counter == cart_counter:
            self.log.info(
                f":{self.__class__.test_inventory_cart_counter.__name__}: {[*standard_user_cred]} :: TEST PASSED")
            assert True
        else:
            self.log.info(
                f":{self.__class__.test_inventory_cart_counter.__name__}: {[*standard_user_cred]} :: TEST FAILED")
            assert False

    def test_inventory_item_links(self, standard_user_cred):
        login_page = LoginPage(self.driver)
        inventory = Inventory(self.driver)
        curl = self.driver.current_url

        if curl == "https://www.saucedemo.com/":
            login_page.setUsername(standard_user_cred[0])
            login_page.setPassword((standard_user_cred[1]))
            login_page.clickLoginButton()
        elif curl != "https://www.saucedemo.com/inventory.html":
            inventory.clickBurgerButton()
            inventory.clickAllItems()

        links = inventory.getItemLinks()

        for i in range(len(links)):
            els = self.driver.find_elements(By.CSS_SELECTOR,"div.inventory_item > div.inventory_item_description > div.inventory_item_label > a")
            els[i].click()
            if links[i] == self.driver.current_url:
                self.log.info(
                    f":{self.__class__.test_inventory_item_links.__name__}: {[*standard_user_cred]} :: TEST PASSED")
                self.driver.back()
                assert True
            else:
                self.log.info(
                    f":{self.__class__.test_inventory_item_links.__name__}: {[*standard_user_cred]} :: TEST FAILED")
                self.driver.back()
                assert False



