__author__ = "Ismayil Aliyev"

from tests.settings import *
from tests import utils
from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
import tests.ElementsTesting
import tests.MenuItemTesting
import tests.ScreenshotTesting
import tests.SearchTesting

# example_tests = TestLoader().loadTestsFromTestCase(ExampleTests)
# example2_tests = TestLoader().loadTestsFromTestCase(Example2Test)

ElementTest = TestLoader().loadTestsFromTestCase(tests.ElementsTesting.ElementsTesting)
MenuAboutUsTest = TestLoader().loadTestsFromTestCase(tests.MenuItemTesting.AboutUsTesting)
MenuBlogTest = TestLoader().loadTestsFromTestCase(tests.MenuItemTesting.BlogTesting)
MenuCaseStudiesTest = TestLoader().loadTestsFromTestCase(tests.MenuItemTesting.CaseStudiesTesting)
MenuContactUsTest = TestLoader().loadTestsFromTestCase(tests.MenuItemTesting.ContactUsTesting)
MenuPlatformTest = TestLoader().loadTestsFromTestCase(tests.MenuItemTesting.PlatformTesting)
MenuSolutionTest = TestLoader().loadTestsFromTestCase(tests.MenuItemTesting.SolutionsTesting)
ScreenshotDesktopTest = TestLoader().loadTestsFromTestCase(tests.ScreenshotTesting.DesktopSizeScreenshotTesting)
ScreenshotMobileTest = TestLoader().loadTestsFromTestCase(tests.ScreenshotTesting.MobileSizeScreenshotTesting)
SearchResultsTest = TestLoader().loadTestsFromTestCase(tests.SearchTesting.SearchResultsTesting)
SearchNoResultsTest = TestLoader().loadTestsFromTestCase(tests.SearchTesting.SearchNoResultTesting)

suite1 = TestSuite([ElementTest,])
suite2 = TestSuite([MenuAboutUsTest,])
suite3 = TestSuite([MenuBlogTest,])
suite4 = TestSuite([MenuCaseStudiesTest,])
suite5 = TestSuite([MenuContactUsTest,])
suite6 = TestSuite([MenuPlatformTest,])
suite7 = TestSuite([MenuSolutionTest,])
suite8 = TestSuite([SearchResultsTest,])
suite9 = TestSuite([SearchNoResultsTest,])
suite10 = TestSuite([ScreenshotMobileTest,])
suite11 = TestSuite([ScreenshotDesktopTest,])

kwargs = {
    "output": ".",
    "failfast": True
}
runner = HTMLTestRunner(report_name="ElementTest",**kwargs)
runner.run(suite1)
runner = HTMLTestRunner(report_name="MenuAboutUsTest",**kwargs)
runner.run(suite2)
runner = HTMLTestRunner(report_name="MenuBlogTest",**kwargs)
runner.run(suite3)
runner = HTMLTestRunner(report_name="MenuCaseStudiesTest",**kwargs)
runner.run(suite4)
runner = HTMLTestRunner(report_name="MenuContactUsTest",**kwargs)
runner.run(suite5)
runner = HTMLTestRunner(report_name="MenuPlatformTest",**kwargs)
runner.run(suite6)
runner = HTMLTestRunner(report_name="MenuSolutionTest",**kwargs)
runner.run(suite7)
runner = HTMLTestRunner(report_name="SearchResultsTest",**kwargs)
runner.run(suite8)
runner = HTMLTestRunner(report_name="SearchNoResultsTest",**kwargs)
runner.run(suite9)
runner = HTMLTestRunner(report_name="ScreenshotMobileTest",**kwargs)
runner.run(suite10)
runner = HTMLTestRunner(report_name="ScreenshotDesktopTest",**kwargs)
runner.run(suite11)