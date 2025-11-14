from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

def print_available_books():
    available = False                          #flag to take care of extreme case of no books available
    for i in library_books:
        if i['available'] == True:
            available = True                    #if atleast one book available, set available to true
            print(f"Book ID: {i['id']}\nTitle: {i['title']}\nAuthor: {i['author']}\n")
    if available == False:                        #case for if available equals false/ no books available
        print ("No books are available.\n")      

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

def find_book():
    user_input = input("Enter an author or a genre")
    matching_books = []
    for i in library_books:
        if user_input.strip().lower() == i['author'].lower():             #compares with everything lowercase to disregard case-sensitive
            matching_books.append(i)
        if user_input.strip().lower() == i['genre'].lower():                #checks for genre as well as author
            matching_books.append(i)                        #appends all matches to empty list
    
    if len(matching_books) > 0:
        for i in matching_books:
            print(f"Book ID: {i['id']}\nTitle: {i['title']}\nAuthor: {i['author']}\nGenre: {i['genre']}\nAvailable: {i['available']}")   #prints all info of books in matching list
    else:                       # takes care of no matches in the user's search
        print("No matches found.")

    



# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def checkout_book():
    book_id = input("Enter the ID of the book you would like to checkout.")
    id_found = False                            #flag to take care of wrong ID input
    for book in library_books:
        if book['id'] == book_id:
            id_found = True                     #if book found, set the flag variable to True
            if book['available'] == True:
                book['available'] = False
                book['due_date'] = (datetime.today() + timedelta(days=14)).strftime("%x") #used w3schools (https://www.w3schools.com/python/python_datetime.asp) and AI to understand the datetime class. 
                book['checkouts'] += 1
                print(f"You checked out {book['title']}. Please return it by {book['due_date']}")
            else:
                print("This book has currently been checked out. It will return on " + book['due_date'])     #prints a checked out message with return date
    if id_found == False:                                       #if flag stayed false, no book was found
        print("No book with ID: '" + book_id + "' exists.")


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

def return_book_by_id():
    return_id = input("Please enter the ID of the book you would like to return")
    id_found = False                #flag for wrong ID input

    for book in library_books:
        if book['id'] == return_id:
            id_found = True                     #if book found, set flag to true
            if book['available'] == False:
                book['available'] = True
                book ["due_date"] = None
                print("You returned book " + return_id)
            else:
                print("This book is currently available")          #if the book was already set to available
    if id_found == False:                                   #check flag to ensure the book id was entered properly
        print("No book with ID: '" + book_id + "' exists.")


# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out

def check_overdue_books():
    overdue_books = []      #list to store overdue books
    overdue_found = False       # flag 
    for book in library_books:
        if book['available'] == False and book['due_date'] is not None and datetime.strptime(book['due_date'], "%x") < datetime.today():     # checks for due date being set to None to avoid error with datetime class functions--- Used the following webstie to learn how to test for if due date is past today (https://www.geeksforgeeks.org/python/python-convert-string-to-datetime-and-vice-versa)
            overdue_found = True                        #adjusts flag when a book is overdue
            overdue_books.append(book)
    for book in overdue_books:
        print(book['title'] + "\n")
    if overdue_found == False:
        print("No books are overdue.")


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!



# You can use this space to test your functions
checkout_book()
print()
checkout_book()
