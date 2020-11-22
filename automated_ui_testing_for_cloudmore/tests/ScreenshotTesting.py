from .settings import *

class DesktopSizeScreenshotTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path=WEBDRIVER_PATH)
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window() # for maximizing the browser size
        # navigate to the application home page
        inst.driver.get(WEBSITE_URL)
        inst.driver.title

    def consent_banner(self):
        """
            For closing EU consent banner if it will occur.
            1. Check if EU consent banner is there.
            2. Find admit button
            3. Click it
        """
        if self.driver.find_element_by_css_selector("a#hs-eu-confirmation-button"): 
            self.driver.find_element_by_css_selector("a#hs-eu-confirmation-button").click()
            self.driver.implicitly_wait(30)

    def test_search_hogset(self):
        search_key = "Högset" # What will be searched
        self.consent_banner() # For closing consent banner auto.
        self.driver.find_element_by_css_selector('span.search > i').click()
        search_box = self.driver.find_element_by_css_selector("input[type='search'].hs-input") # Finding search bar
        search_box.send_keys(search_key) # Typing the search_key to the search bar
        search_button = self.driver.find_element_by_css_selector("button[type='submit'].hs-button") 
        search_button.click() 
        self.driver.implicitly_wait(60)
        for i in range(2): # in order to go to the 3rd page of results, next page button should be clicked twice
            try: # Try catch is used in order to if it is only result page, then there will occur NoSuchElement exception. To handle the case and not to break script
                self.driver.find_element_by_css_selector("a.hs-search-results__next-page").click()
                self.driver.implicitly_wait(30)
            except:
                break
        self.driver.get_screenshot_as_file("./screenshots/screenshot_desktop.png")
        self.assertTrue(os.path.isfile('./screenshots/screenshot_desktop.png'), msg="Desktop size image is not found.") # Checking if screenshotfile is not there testcase will be failed
    
    

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

class MobileSizeScreenshotTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path=WEBDRIVER_PATH)
        inst.driver.implicitly_wait(30)
        inst.driver.set_window_size(375,812) # Setting Iphone X size to the browser, in order to get mobile view.
        # navigate to the application home page
        inst.driver.get(WEBSITE_URL)
        inst.driver.title

    def consent_banner(self):
        """
            For closing EU consent banner if it will occur.
        """
        if self.driver.find_element_by_css_selector("a#hs-eu-confirmation-button"):
            self.driver.find_element_by_css_selector("a#hs-eu-confirmation-button").click()
            self.driver.implicitly_wait(30)

    def test_search_hogset(self):
        search_key = "Högset"
        self.consent_banner()
        self.driver.find_element_by_css_selector('span.search > i').click()
        search_box = self.driver.find_element_by_css_selector("input[type='search'].hs-input")
        search_box.send_keys(search_key)
        search_button = self.driver.find_element_by_css_selector("button[type='submit'].hs-button")
        search_button.click()
        self.driver.implicitly_wait(60)
        for i in range(2): # in order to go to the 3rd page of results, next page button should be clicked twice
            try: # Try catch is used in order to if it is only result page, then there will occur NoSuchElement exception. To handle the case and not to break script
                self.driver.find_element_by_css_selector("a.hs-search-results__next-page").click()
                self.driver.implicitly_wait(30)
            except:
                break
        self.driver.get_screenshot_as_file("./screenshots/screenshot_mobile.png")
        self.assertTrue(os.path.isfile('./screenshots/screenshot_mobile.png'), msg="Desktop size image is not found.")
    
    

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()


if __name__ == "__main__":
    unittest.main()