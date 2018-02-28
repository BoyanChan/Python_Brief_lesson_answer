def display_message():
    """print a message to show what i will do"""
    print("This character, I will learn how to use function")

def favorite_book(book):
    print("My favourite book is "+book)


display_message()

print("------------------------------")

books = input("Enter a name of book: ")
favorite_book(books)

