from .settings import *

class ElementsTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path=WEBDRIVER_PATH)
        inst.driver.implicitly_wait(30)
        inst.driver.minimize_window()
        # navigate to the application home page
        inst.driver.get(WEBSITE_URL)
        inst.driver.title

    def test_logo_image(self):
        logo_bool = self.driver.find_element_by_xpath('//*[@id="hs-link-module_14891423382401005"]/img').is_displayed() # Checks xpath of logo
        self.assertTrue(logo_bool, msg="Logo is not displayed.")

    def menu_item_element_tester(self, text, depth):
        """
            Supplimentary function that will be used in sub tests in order to check is navbar items are there or not
            Algo:
            1. Finds all list items(navbar links) which has class and their depth.
            2. Iterates over the list and checks if items lowered text is the same what we search.
            3. Checks if the item that we are looking for is displayed or not, creates bool.
             3'. If not displayed fails the testcase.
        """
        menu_items = self.driver.find_elements_by_css_selector(f"li.hs-menu-item.hs-menu-depth-{depth} > a") # Finds all list items(navbar links) which has class and their depth (1 = menu items, 2=dropdown menu items).
        for element in menu_items:
            if element.text.lower() == text:
                flag = element.is_displayed()
                break
            else:
                flag = False
        self.assertTrue(flag, msg=f"{text} - menu item, is not here")
    
    def test_navElements(self):
        names = ["platform", "solutions", "about us", "contact us", "blog", "case studies"]
        for text in names: # Creates subTest for each item of menu, and checks if the item is displayed or not.
            with self.subTest(): 
                self.menu_item_element_tester(text, 1) # Using supplimentary menu_item_element_tester.

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
       unittest.main()