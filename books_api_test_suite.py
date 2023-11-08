import unittest

import HtmlTestRunner

from tests.test_api_status import TestApiStatus
from tests.test_get_all_books import TestGetAllBooks
from tests.test_submit_order import TestSubmitOrder


class TestSuite(unittest.TestCase):

    def test_suite(self):
        suita_teste = unittest.TestSuite()
        suita_teste.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(TestApiStatus),
                             unittest.defaultTestLoader.loadTestsFromTestCase(TestGetAllBooks),
                              unittest.defaultTestLoader.loadTestsFromTestCase(TestSubmitOrder)])

        #pip install html-testRunner
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="API Test Report",
            report_name="Books API Test Results"
        )

        runner.run(suita_teste)