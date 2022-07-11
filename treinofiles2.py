file = open("books.txt", "r")

for i in file:
    book_letter = i[0]
    book_len = len(i.replace("\n", ""))
    print(book_letter + str(book_len))
file.close()