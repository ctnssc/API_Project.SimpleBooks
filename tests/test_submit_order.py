import unittest

from requests_books.simple_books_api import SimpleBooksRequests


class TestSubmitOrder(unittest.TestCase):
    access_token = ""

    def setUp(self):
        self.books_API = SimpleBooksRequests()

        if self.access_token == "":
            self.access_token = self.books_API.generate_token()

    def test_submit_order_status_code(self):
        book_id = 3
        customer_name = "John"

        response = self.books_API.submit_order(self.access_token, book_id, customer_name)
        expected_status_code = 201
        actual_status_code = response.status_code


        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code.")
        expected_created_message = True
        actual_created_message = response.json()['created']
        self.assertEqual(expected_created_message, actual_created_message, "Unexpected created message.")
        self.order_id = response.json()["orderId"]

    def test_submit_order_invalid_bookid(self):
        invalid_book_id = 21
        customer_name = "John"

        response = self.books_API.submit_order(self.access_token, invalid_book_id, customer_name)
        expected_status_code = 400
        actual_status_code = response.status_code
        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code.")

        expected_error_message = 'Invalid or missing bookId.'
        actual_error_message = response.json()['error']
        self.assertEqual(expected_error_message, actual_error_message, "Unexpected error message.")

