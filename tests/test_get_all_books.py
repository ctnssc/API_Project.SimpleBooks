import unittest

from requests_books.simple_books_api import SimpleBooksRequests


class TestGetAllBooks(unittest.TestCase):

    def setUp(self):
        self.book_API = SimpleBooksRequests()

    def test_all_books_status_code_wo_filter(self):
        response = self.book_API.get_all_books()
        expected_response_code = 200
        actual_response_code = response.status_code

        self.assertEqual(expected_response_code, actual_response_code, "Error, unexpected status code")

    def test_get_all_books_number_of_results_wo_filter(self):
        response = self.book_API.get_all_books()
        expected_number_of_books = 6
        actual_numer_of_books = len(response.json())
        self.assertEqual(expected_number_of_books,actual_numer_of_books,"Error, unexpected number of books")

    def test_get_all_books_filter_by_valid_limit(self):
        response = self.book_API.get_all_books(limit=3)
        expected_number_of_results = 3
        actual_number_of_results = len(response.json())
        self.assertEqual(expected_number_of_results, actual_number_of_results, "Error, unexpected number of results")

    def test_get_all_books_filter_by_invalid_limit_greater_than_20(self):
        response = self.book_API.get_all_books(limit=21)
        expected_status_code = 400
        actual_code_response = response.status_code

        self.assertEqual(expected_status_code, actual_code_response, "Error, unexpected status code")
        expected_error_message = "Invalid value for query parameter 'limit'. Cannot be greater than 20."
        actual_errror_message = response.json()["error"]

        self.assertEqual(expected_error_message, actual_errror_message, "Error, unexpected error message")

    def test_get_all_books_filter_by_invalid_limit_negative_number(self):
        response = self.book_API.get_all_books(limit=-1)
        expected_status_code = 400
        actual_code_response = response.status_code
        self.assertEqual(expected_status_code, actual_code_response, "Error, unexpected status code")
        expected_error_message = "Invalid value for query parameter 'limit'. Must be greater than 0."
        actual_errror_message = response.json()["error"]

        self.assertEqual(expected_error_message, actual_errror_message, "Error, unexpected error message")

    def test_get_all_books_filter_by_type_fiction(self):
        response = self.book_API.get_all_books(book_type='fiction')
        expected_response_code = 200
        actual_response_code = response.status_code
        expected_type = 'fiction'
        self.assertEqual(expected_response_code, actual_response_code, "Error, unexpected status code")
        for i in range(len(response.json())):
            current_book = response.json()[i]
            current_book_type = current_book['type']

            self.assertEqual(expected_type,current_book_type, f"Unexpected type for book {current_book['name']}")


    def test_get_all_books_filter_by_type_nonfiction(self):
        response = self.book_API.get_all_books(book_type='non-fiction')
        expected_response_code = 200
        actual_response_code = response.status_code
        expected_type = 'non-fiction'
        self.assertEqual(expected_response_code, actual_response_code, "Error, unexpected status code")
        for i in range(len(response.json())):
            current_book = response.json()[i]
            current_book_type = current_book['type']
            self.assertEqual(expected_type,current_book_type, f"Unexpected type for book {current_book['name']}")


