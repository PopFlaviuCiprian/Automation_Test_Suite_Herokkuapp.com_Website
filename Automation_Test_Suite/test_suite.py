import unittest
import HtmlTestRunner
from formy_tests_autocomplete import Autocomplete
from buttons_page import ButtonsPage
from checkboxes_page import CheckboxPage


class TestSuiteFormy(unittest.TestCase):

    def test_suite(self):
        running_tests = unittest.TestSuite()
        running_tests.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Autocomplete),
            unittest.defaultTestLoader.loadTestsFromTestCase(ButtonsPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(CheckboxPage)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports = True,
            report_title = "Test_suite_report",
            report_name = "Reports_formy_project"
        )

        runner.run(running_tests)