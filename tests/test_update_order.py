import unittest

from requests_books.simple_books_api import SimpleBooksRequests


class TestUpdateOrder(unittest.TestCase):
    access_token = ""

    def setUp(self):
        self.books_API = SimpleBooksRequests()

        if self.access_token == "":
            self.access_token = self.books_API.generate_token()

    def test_for_update_order_status_code(self):

        new_customer_name = "John1"
        book_id = 3
        customer_name = "John"

        submit_response = self.books_API.submit_order(self.access_token, book_id, customer_name)
        order_Id = submit_response.json()["orderId"]

        response_update = self.books_API.update_order(self.access_token, order_Id, new_customer_name)
        expected_status_code = 204
        actual_status_code = response_update.status_code

        self.assertEqual(expected_status_code, actual_status_code, "Unexpected status code.")

        response_get = self.books_API.get_order_byId(self.access_token,order_Id)
        expected_customer_name = new_customer_name
        actual_customer_name = response_get.json()['customerName']
        self.assertEqual(expected_customer_name, actual_customer_name, "Unexpected customer name.")