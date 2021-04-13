from selenium.webdriver.common.by import By


class LoginPage:
    __url = "https://www.saucedemo.com/"
    __username = (By.CSS_SELECTOR, "input#user-name")
    __password = (By.CSS_SELECTOR, "input#password")
    __loginButton = (By.CSS_SELECTOR, "input#login-button")
    __errorButton = (By.CSS_SELECTOR, "button.error-button")

    def __init__(self, driver):
        self.driver = driver

    def goToLoginPage(self):
        self.driver.get(self.__url)

    def setUsername(self,username):
        e = self.driver.find_element(*self.__username)
        e.send_keys(" ")
        e.clear()
        self.driver.find_element(*self.__username).send_keys(username)

    def setPassword(self,password):
        e = self.driver.find_element(*self.__password)
        e.send_keys(" ")
        e.clear()
        self.driver.find_element(*self.__password).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(*self.__loginButton).click()







