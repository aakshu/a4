# Add project directory to system path so python can find imports
from os.path import dirname, realpath
import sys
sys.path.append(dirname(dirname(realpath(__file__))))

# import modules to run client
import grpc
from service import library_pb2
from service import library_pb2_grpc

# import Genre to validate input
from service.library_pb2 import Genre

# Class that encapsulates Client API
class inventoryClient:

    # constructor to take technical details and instantiate client object
    def __init__(self, port=None) -> None:
        # if port argument is not provided, set it with default value
        if port is None:
            self.port = "localhost:50051"
        else:
            self.port = port

    # function to create a book in the server
    def create_book(self, isbn, title, author, genre, year):
        # connect to server 
        with grpc.insecure_channel(self.port) as channel:
            stub = library_pb2_grpc.InventoryStub(channel)

            # if genre input is not valid, return error
            if genre not in Genre.keys():
                print("The genre you entered is not a valid one, these are the following genre's supported currently:")
                for genre_name in Genre.keys():
                    print(genre_name)
                return
            
            #create a book request to send to server
            create_book_request = library_pb2.Book(isbn=isbn, title=title, author=author, genre=genre, publishing_year=year)

            # retrieve and return the response
            response = stub.CreateBook(create_book_request)
            return response

  
    # function to retrieve a book from the server
    def get_book(self, isbn):
        # connect to server
        with grpc.insecure_channel(self.port) as channel:
            stub = library_pb2_grpc.InventoryStub(channel)

            # create an isbn request to send to server
            isbn_request = library_pb2.ISBN(isbn=isbn)

            # retrieve and return the response
            response = stub.GetBook(isbn_request)
            return response