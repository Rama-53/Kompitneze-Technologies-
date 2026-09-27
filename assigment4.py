print("------ ONLINE LIBRARY MANAGEMENT SYSTEM ------")


books = ["Python", "Java", "C++"]

print("Available Books:")
print(books)

uppercase_books = [book.upper() for book in books]

print("\nUppercase Book Names:")
print(uppercase_books)

categories = ("Programming", "Database", "Networking")

print("Book Categories:")
for category in categories:
    print(category)

genres = {"Python", "Java", "C++","HTML"}

print("Unique Genres:")
print(genres)

library = {
    101: {"title": "Python", "author": "Alex"},
    102: {"title": "HTML", "author": "Varun"}
}

print("Book Details:")
print("101 ->", library[101])

print("Dictionary Keys:")
print(library.keys())

books_only = {
    101: {"title": "Python"},
    102: {"title": "HTML"}
}

print("Dictionary Values:")
print(books_only.values())

book_not_issued = None

print("Book Not Issued:")
print(book_not_issued)

print("Type of None:")
print(type(book_not_issued))

print("Hash Value:")
print(hash(books[0]))