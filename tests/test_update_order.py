import unittest

from requests_books.simple_books_api import SimpleBooksRequests


class TestUpdateOrder(unittest.TestCase):
    access_token = ""

    def setUp(self):
        self.books_API = SimpleBooksRequests()

        if self.access_token == "":
            self.access_token = self.books_API.generate_token()

    def test_for_update_order_status_code(self):
        order_Id = "oq_bTELRd7QTW9C22bWBk"
        new_customer_name = "John"

        response = self.books_API.update_order(self.access_token, order_Id, new_customer_name)
        expected_status_code = 201
        actual_status_code = response.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code.")
