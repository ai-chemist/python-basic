def display_message(chapter):
    print(f"Chapter {chapter.title()}!")

display_message(str(1))

def title(book):
    print(f"Book : {book.title()}")

bookname = input("Enter a book name: ")
title(bookname)