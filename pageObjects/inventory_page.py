from selenium.webdriver.common.by import By



class Inventory:
    __burgerButton = (By.CSS_SELECTOR,"button#react-burger-menu-btn")
    __allItems = (By.CSS_SELECTOR, "a#inventory_sidebar_link")
    __about = (By.CSS_SELECTOR, "a#about_sidebar_link")
    __logout = (By.CSS_SELECTOR, "a#logout_sidebar_link")
    __resetAppState = (By.CSS_SELECTOR, "a#reset_sidebar_link")
    __close = (By.CSS_SELECTOR, "button#react-burger-cross-btn")
    __cartButtons = (By.CSS_SELECTOR,"button.btn.btn_primary.btn_small.btn_inventory")
    __cartLink = (By.CSS_SELECTOR,"a.shopping_cart_link")
    __items = (By.CSS_SELECTOR,"div.inventory_item")

    def __init__(self, driver):
        self.driver = driver

    def clickBurgerButton(self):
        self.driver.find_element(*self.__burgerButton).click()

    def clickAllItems(self):
        self.driver.find_element(*self.__allItems).click()

    def clickAbout(self):
        self.driver.find_element(*self.__about).click()

    def clickLogout(self):
        self.driver.find_element(*self.__logout).click()

    def clickResetAppState(self):
        self.driver.find_element(*self.__resetAppState).click()

    def clickCloseX(self):
        self.driver.find_element(*self.__close).click()

    def clickAllCartButtons(self):
        elements = self.driver.find_elements(*self.__cartButtons)
        for el in elements:
            el.click()
        return str(len(elements))

    def getCartCounter(self):
        el = self.driver.find_element(*self.__cartLink)
        return el.text

    def getItemLinks(self):
        elements = self.driver.find_elements(*self.__items)
        ids = [x.find_element(By.CSS_SELECTOR,"div.inventory_item_label > a").get_attribute("id").replace("_title_link","")\
               .replace("item_","id=") for x in elements]
        links = [f"https://www.saucedemo.com/inventory-item.html?{x}" for x in ids]
        return links
