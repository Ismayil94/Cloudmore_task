from .settings import *

class SearchNoResultTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path=WEBDRIVER_PATH)
        inst.driver.implicitly_wait(30)
        inst.driver.minimize_window()
        # navigate to the application home page
        inst.driver.get(WEBSITE_URL)
        inst.driver.title

    
    @unittest.expectedFailure
    def test_search_Ismayil(self):
        search_key = "Ismayil"
        self.driver.find_element_by_css_selector('span.search > i').click()
        search_box = self.driver.find_element_by_css_selector("input[type='search'].hs-input")
        search_box.send_keys(search_key)
        search_button = self.driver.find_element_by_css_selector("button[type='submit'].hs-button")
        search_button.click()
        results = self.driver.find_elements_by_css_selector('ul.hs-search-results__listing > li') # Get the list of results
        if len(results) > 0: # If the length og results array is 0, then there is no results for the search query.
            flag = True
        else:
            flag = False
        self.assertTrue(flag, msg=f"No Results for {search_key}") # if flag is False - no results, testcase will Fail.
    

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

class SearchResultsTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path=WEBDRIVER_PATH)
        inst.driver.implicitly_wait(30)
        inst.driver.minimize_window()
        # navigate to the application home page
        inst.driver.get(WEBSITE_URL)
        inst.driver.title

    def test_search_hogset(self):
        search_key = "Högset"
        self.driver.find_element_by_css_selector('span.search > i').click()
        search_box = self.driver.find_element_by_css_selector("input[type='search'].hs-input")
        search_box.send_keys(search_key)
        search_button = self.driver.find_element_by_css_selector("button[type='submit'].hs-button")
        search_button.click()
        self.driver.implicitly_wait(30)
        results = self.driver.find_elements_by_css_selector('ul.hs-search-results__listing > li')
        if len(results) > 0:
            flag = True
        else:
            flag = False
        self.assertTrue(flag, msg=f"No Results for {search_key}")
    
    
    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == "__main__":
    unittest.main()