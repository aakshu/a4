# import modules for testing
import unittest
from unittest.mock import MagicMock

# import function to test - get_book_titles()
from get_book_titles import get_book_titles

# import client class for live server tests only
from inventory_client import inventoryClient

# helper function to return a mock book when mock client calls get_book()
def get_book_for_isbn(isbn):
    # create a mock book
    mock_book = MagicMock()

    # create mock book with title based on the isbn input
    if isbn == "1000":
        mock_book.title = "Harry Potter 3"
    elif isbn  == "1001":
        mock_book.title =  "Percy Jackson"
    elif isbn == "1002":
        mock_book.title =  "Hunger Games"
    else:
        mock_book.title =  "Invalid ISBN"
    
    # return the mock book
    return mock_book

# testing class to run unittests
class TestGetBookTitles(unittest.TestCase):
    # test for get_book_titles() with mocks
    def test_mock_get_book_titles(self):
        # create a mock test client
        mock_test_client = MagicMock()
        # define behavior when get_book() function of mock client is called
        mock_test_client.get_book.side_effect = get_book_for_isbn

        # list of isbn to query
        list_of_isbn = ["1000", "1001"]
        # retrieve list of titles using mock client
        list_of_titles = get_book_titles(mock_test_client, list_of_isbn)

        # assert that the response is as expected
        self.assertEqual(list_of_titles, ["Harry Potter 3", "Percy Jackson"])

    # test for live server method for get_book_titles()
    # NOTE: this test will only work if the server is running
    def test_live_get_book_titles(self):
        # create an instance of client class
        test_client = inventoryClient("localhost:50051")
        
        # list of isbn to query
        list_of_isbn = ["1000", "1001"]
        # retrieve list of titles using real client object that queries live server
        list_of_titles = get_book_titles(test_client, list_of_isbn)

        # assert that the response is as expected
        self.assertEqual(list_of_titles, ["Harry Potter 3", "Percy Jackson"])

# if script is called, run all the unit tests defined
if __name__ == "__main__":
    unittest.main()