import unittest

from requests_books.simple_books_api import SimpleBooksRequests


class TestDeleteOrder(unittest.TestCase):
    access_token = ""
    def setUp(self):
        self.books_API = SimpleBooksRequests()

        if self.access_token == "":
            self.access_token = self.books_API.generate_token()

    def test_delete_order_byId(self):
        book_id = 3
        customer_name = "John"

        submit_response = self.books_API.submit_order(self.access_token, book_id, customer_name)
        order_Id = submit_response.json()["orderId"]

        response_delete = self.books_API.delete_order_byId(self.access_token, order_Id)
        expected_status_code = 204
        actual_status_code = response_delete.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code.")

        response_get = self.books_API.get_order_byId(self.access_token, order_Id)
        new_expected_status_code = 404
        new_actual_status_code = response_get.status_code

        self.assertEqual(new_expected_status_code, new_actual_status_code, "Unexpected status code.")

