# import inventory_client to access client object
from inventory_client import inventoryClient

# function to retrieve isbn titles from client object
def get_book_titles(test_client, list_of_isbn):
    # list of titles to return
    list_of_titles = []

    # for each isbn, get the respective title and add it to the list
    for isbn in list_of_isbn:
        list_of_titles.append(test_client.get_book(isbn).title)
    
    # return list of titles received from client
    return list_of_titles

# if script is run, create client object and call function to get isbn titles
if __name__ == "__main__":
    # create client object
    test_client = inventoryClient("localhost:50051")

    # call function to retrieve list of titles
    list_of_isbn = ["1000", "1001"]
    list_of_titles = get_book_titles(test_client, list_of_isbn)

    # display titles in CLI
    idx = 1
    for title in list_of_titles:
        print(f"Title #{idx}: {title}")
        idx = idx + 1