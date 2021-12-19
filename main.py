from time import *
from math import sqrt

print("┏━━┓━━━━━━━━━┏┓━━━━━━┏━━━┓━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┏┓━━━━━━┏┓━━━━━━━━━━━━━━━┏━━━┓┏┓━━━━━━━━━━━━━━━┏┓━┏┓━━━━━━")
print("┃┏┓┃━━━━━━━━━┃┃━━━━━━┃┏━┓┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃┃━━━━━┏┛┗┓━━━━━━━━━━━━━━┃┏━┓┃┃┃━━━━━━━━━━━━━━┏┛┗┓┃┃━━━━━━")
print("┃┗┛┗┓┏━━┓┏━━┓┃┃┏┓━━━━┃┗━┛┃┏━━┓┏━━┓┏━━┓┏┓┏┓┏┓┏┓┏━━┓┏━┓━┏━┛┃┏━━┓━┗┓┏┛┏┓┏━━┓┏━┓━━━━━┃┃━┃┃┃┃━┏━━┓┏━━┓┏━┓┏┓┗┓┏┛┃┗━┓┏┓┏┓")
print("┃┏━┓┃┃┏┓┃┃┏┓┃┃┗┛┛━━━━┃┏┓┏┛┃┏┓┃┃┏━┛┃┏┓┃┃┗┛┃┃┗┛┃┃┏┓┃┃┏┓┓┃┏┓┃┗━┓┃━━┃┃━┣┫┃┏┓┃┃┏┓┓━━━━┃┗━┛┃┃┃━┃┏┓┃┃┏┓┃┃┏┛┣┫━┃┃━┃┏┓┃┃┗┛┃")
print("┃┗━┛┃┃┗┛┃┃┗┛┃┃┏┓┓━━━━┃┃┃┗┓┃┃━┫┃┗━┓┃┗┛┃┃┃┃┃┃┃┃┃┃┃━┫┃┃┃┃┃┗┛┃┃┗┛┗┓━┃┗┓┃┃┃┗┛┃┃┃┃┃━━━━┃┏━┓┃┃┗┓┃┗┛┃┃┗┛┃┃┃━┃┃━┃┗┓┃┃┃┃┃┃┃┃")
print("┗━━━┛┗━━┛┗━━┛┗┛┗┛━━━━┗┛┗━┛┗━━┛┗━━┛┗━━┛┗┻┻┛┗┻┻┛┗━━┛┗┛┗┛┗━━┛┗━━━┛━┗━┛┗┛┗━━┛┗┛┗┛━━━━┗┛━┗┛┗━┛┗━┓┃┗━━┛┗┛━┗┛━┗━┛┗┛┗┛┗┻┻┛")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┏━┛┃━━━━━━━━━━━━━━━━━━━━━")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┗━━┛━━━━━━━━━━━━━━━━━━━━━")

######################################################################################################################################
#######################################-Welcome to our book recommendation algorithm-#################################################
#########################################-Authors : Paul Mandon ; Thomas Masselles-###################################################
#######################################################-EFREI L1, int4-###############################################################
######################################################################################################################################

readers = 'readers.txt'
books = 'books.txt'
books_read = 'booksread.txt'
rating_matrix = 'rating_matrix.txt'

def mainmenu():
    ## This function displays the main menu where the user can chose what menu to navigate to: the bbok menu, the reader menu, the recommendation menu, or exit the programm
    global menu_principal
    menu_principal=0
    print("What menu do you want to navigate to?\n")
    menu_principal=int(input("1 : Book menu\n2 : Reader menu\n3 : Recommendation menu\n4 : Quit\n"))
    ##The input is secured with a while loop
    menu_principal = int(inputVerfication(str(menu_principal),1,4))
    return menu_principal

def inputVerfication(user_input,lowerValue,higherValue):
    ##This function helps streamline the verification of integers values, it checks if they belong to the interval required
    valid_input = []
    for i in range(lowerValue,higherValue+1):
        valid_input.append(str(i))
    while user_input not in valid_input:
        user_input=str(input("Wrong value, please enter the value again (must be between {} and {}) : ".format(lowerValue,higherValue)))
    return user_input

def menub():
    '''
    This function displays a sub menu where the user can decide actions linked to the list of books.
    The options are to modify or delete a book, to view the list of books, or to go back to the main menu
    '''
    global menu_book
    menu_book=0
    print("What do you want to do?\n")
    menu_book=int(input("1 : Add a book\n2 : Modify a book\n3 : Delete a book\n4 : View the book list\n5 : Go back to the main menu\n"))
    ##The input is secured with a while loop
    menu_book = inputVerfication(menu_book,1,5)
    return menu_book

def menureader():
    ##This function displays a sub menu where the user can add, modify or delete a reader
    global menu_reader
    menu_reader=0
    print("What do you want to do?\n")
    ##The input is secured with a while loop
    while menu_reader<1 or menu_reader>4:
        menu_reader=int(input("1 : Add a reader\n2 : Modify a reader\n3 : Delete a reader\n4 : Go back to the main menu\n"))
    return menu_reader

def menuRecommend():
    '''
    this function displays a sub menu where the user can rate books to enhance the algorithm, or find a new book he might enjoy
    The input is secured with a while loop
    '''
    global menu_recommend
    menu_recommend=0
    print("What do you want to do?\n")
    menu_recommend=int(input("1 : Add the book you read among the database\n2 : Rate books\n3 : Find a new book\n4 : Go back to the main menu\n"))
    while menu_recommend<1 or menu_recommend>4:
        menu_recommend = int(input("1 : Add the book you read among the database\n2 : Rate books\n3 : Find a new book\n4 : Go back to the main menu\n"))
    return menu_recommend

def newprofile():
    '''
    This function allows to create a new user profile. It requires ton enter a name, a gender, an age, and a reading preference among those selected
    The inputs are secured with a while loop
    '''
    global name
    global gender
    global age
    global style
    ##Declaration of global variables we will need to use in other functions
    name = str(input("What is your name?\n"))
    gender = str(input("Gender selection\n1 : You are a male\n2 : You are a female\n3 : Other\n"))
    verified_gender = inputVerfication(gender, 1, 3)
    age = str(input("What is your age group?\n1: Below 18\n2: Between 18 and 25\n3: Above 25\n"))
    verified_age = inputVerfication(age, 1, 3)
    style = str(input(
        "What is you reading style?\n1 : Science-Fiction\n2 : Biography\n3 : Horror\n4 : Romance\n5 : Fable\n6 : History\n7 : Comedy\n"))
    verified_style = inputVerfication(style, 1, 7)
    with open(readers, "a", encoding='utf-8') as f:
        f.write("{},{},{},{}\n".format(name, verified_gender, verified_age, verified_style))
    with  open(rating_matrix, "a", encoding="utf-8") as f, open("books.txt", "r", encoding="utf-8") as f1:
        books = f1.readlines()
        new_line_recommandation = []
        for j in range(len(books)):
            new_line_recommandation.append("0")
        f.write(" ".join(new_line_recommandation))
        f.write("\n")
    with open(books_read, "a", encoding="utf-8") as f:
        f.write(name+"\n")
    print("Your profile has successfully been added!\n")
    mainmenu()

def modifyProfile():
    '''
    This function allows to modify a profile
    It asks the user the name of the profile he wants to modify
    If the name of the profile exists, then it asks the user what information he wants changed: name, age, gender, reading style, or recommendation algorithm
    The inputs are all secured with while loops
    The rating matrix is also edited accordingly
    '''
    with open("readers.txt", "r", encoding="utf-8") as f, open(rating_matrix, 'r', encoding='utf-8') as g, open(books_read,"r",encoding="utf-8") as h:
        lignes = f.readlines()
        matrix = g.readlines()
        books_read_lines = h.readlines()
        for ligne in lignes:
            print(ligne[:-1])
        profile = str(input("Enter the name of the profile you want to modify : "))
        i = 0
        while i < len(lignes) and not profile in lignes[i]:
            i += 1
    if i >= len(lignes):
        print("The profile {} is not in the profile database".format(profile))
    else:
        modif = lignes[i].split(",")
        newProfile = ""
        name_change = str(input("Do you want to change your name(y/n)? "))
        while name_change != 'y' and name_change != 'n':
            name_change = str(input("Do you want to change your name(y/n)? "))
        if name_change == 'y':
            newProfile += str(input("What's your name?\n"))
        else:
            newProfile += str(modif[0])
        newProfile += ","
        gender_change = str(input("Do you want to change your gender(y/n)? "))
        while gender_change != 'y' and gender_change != 'n':
            gender_change = str(input("Do you want to change your gender(y/n)? "))
        if gender_change == 'y':
            gender = str(input("Gender selection\n1 : You are a male\n2 : You are a female\n3 : Other\n"))
            gender = inputVerfication(gender, 1, 3)
            newProfile += gender
        else:
            newProfile += str(modif[1])
        newProfile += ","
        age_change = str(input("Do you want to change your age group(y/n)? "))
        while age_change != 'y' and age_change != 'n':
            age_change = str(input("Do you want to change your age(y/n)? "))
        if age_change == 'y':
            age = str(input("What is your age group?\n1: Below 18\n2: Between 18 and 25\n3: Above 25\n"))
            age = inputVerfication(age, 1, 3)
            newProfile += age
        else:
            newProfile += str(modif[2])
        newProfile += ","
        style_change = str(input("Do you want to change your favourite genre(y/n)? "))
        while style_change != 'y' and style_change != 'n':
            genre_change_change = str(input("Do you want to change your age(y/n)? "))
        if style_change == 'y':
            style = str(input("What is you reading style?\n1 : Science-Fiction\n2 : Biography\n3 : Horror\n4 : Romance\n5 : Fable\n6 : History\n7 : Comedy\n"))
            style = inputVerfication(style, 1, 7)
            newProfile += style + "\n"
        else:
            newProfile += str(modif[3])
        print("the profile is now {}".format(newProfile))
        with open("readers.txt", "w", encoding="utf-8") as f:
            for j in range(len(lignes)):
                if i == j:
                    f.write(newProfile)
                else:
                    f.write(lignes[j])
        with  open(rating_matrix, "w", encoding="utf-8") as f, open("books.txt", "r", encoding="utf-8") as f1:
            books = f1.readlines()
            for j in range(len(matrix)):
                if i == j:
                    new_line_recommandation = []
                    for k in range(len(books)):
                        new_line_recommandation.append("0")
                    f.write(" ".join(new_line_recommandation))
                    f.write("\n")
                else:
                    f.write(matrix[j])
        with open(books_read, "w", encoding="utf-8") as f:
            for j in range(len(matrix)):
                if i == j:
                    f.write(newProfile)
                else:
                    f.write(books_read_lines[j])

def replaceBook():
    '''
    This function asks the user for the name of the book he wants to be replaced
    The file is then edited in the proper way, the matrix is also edited accordingly
    The inputs are all secured with while loops
    '''
    viewBooks()
    with open("books.txt", "r", encoding="utf-8") as f1, open(rating_matrix,"r",encoding="utf_8") as f2, open(books_read,"r",encoding="utf-8") as f3 :
        lignes = f1.readlines()
        matrice = f2.readlines()
        booksRead = f3.readlines()
        book = str(input("enter the name of the book you want to replace : "))
        i = 0
        while i < len(lignes) and not book in lignes[i]:
             i += 1
        if i >= len(lignes):
            print("The book {} is not in the books database".format(book))
        else:
            new_book=str(input("You want to replace the book {} by ".format(book)))
        with open("books.txt", "w", encoding="utf-8") as f:
            for j in range(len(lignes)):
                if i == j:
                    f.write(new_book+"\n")
                else:
                    f.write(lignes[j])
        with open(rating_matrix,"w",encoding="utf_8") as f:
            for j in range(len(matrice)):
                new_matrice_line=[]
                old_matrice_line=matrice[j].strip("\n").split(" ")
                for k in range(len(old_matrice_line)):
                    if k == i:
                        new_matrice_line.append("0")
                    else:
                        new_matrice_line.append(old_matrice_line[k])
                f.write(" ".join(new_matrice_line)+"\n")
        with open(books_read,"w",encoding="utf-8") as f:
            for j in range(len(booksRead)):
                old_line = booksRead[j].strip("\n").split(",")
                new_line = []
                for k in range(len(old_line)):
                    if  not old_line[k]==str(i):
                        new_line.append(old_line[k])
                    f.write(",".join(new_line)+"\n")

def deleteBook():
    '''
    This function allows the user to delete a book from the list only if it already exists
    The rating matrix is also edited accordingly
    The inputs are all secured with while loops
    '''
    viewBooks()
    with open("books.txt", "r", encoding="utf-8") as f1, open(rating_matrix, "r", encoding="utf_8") as f2, open(
            books_read, "r", encoding="utf-8") as f3:
        lignes = f1.readlines()
        matrice = f2.readlines()
        booksRead = f3.readlines()
    book = str(input("Enter the name of the book you want to replace : "))
    i = 0
    while i < len(lignes) and not book in lignes[i]:
        i += 1
    if i >= len(lignes):
        print("The book {} is not in the  books of the database\n".format(book))
    else:
        with open("books.txt", "w", encoding="utf-8") as f:
            for j in range(len(lignes)):
                if i != j:
                    f.write(lignes[j])
        print("The book {} has been deleted from the available books\n".format(book))
        with open(rating_matrix, "w", encoding="utf_8") as f:
            for j in range(len(matrice)):
                new_matrice_line = []
                old_matrice_line = matrice[j].strip("\n").split(" ")
                for k in range(len(old_matrice_line)):
                    if k != i:
                        new_matrice_line.append(old_matrice_line[k])
                f.write(" ".join(new_matrice_line) + "\n")
        with open(books_read, "w", encoding="utf-8") as f:
            for j in range(len(booksRead)):
                old_line = booksRead[j].strip("\n").split(",")
                new_line = []
                for k in range(len(old_line)):
                    if not old_line[k] == str(i):
                        new_line.append(old_line[k])
                f.write(",".join(new_line) + "\n")

def deleteProfile():
    '''
    This function allows to delete a user profile, but only if it exists
    The rating matrix is also edited accordingly
    The inputs are all secured with while loops
    '''
    viewReaders()
    profile = str(input("Enter the name of the profile you want to delete : "))
    with open(readers, "r", encoding="utf-8") as f1, open(rating_matrix, "r", encoding="utf_8") as f2, open(books_read, "r", encoding="utf-8") as f3:
        lignes = f1.readlines()
        matrice = f2.readlines()
        booksRead = f3.readlines()
    i = 0
    while i < len(lignes) and not profile in lignes[i]:
        i += 1
    if i >= len(lignes):
        print("The profile {} is not in the profile database\n".format(profile))
    else:
        with open("readers.txt", "w", encoding="utf-8") as f:
            for j in range(len(lignes)):
                if i != j:
                    f.write(lignes[j])
        print("The profile {} has been deleted from the profile list\n".format(profile))
        with open(rating_matrix, "w", encoding="utf-8") as f:
            for j in range(len(matrice)):
                if i != j:
                    f.write(matrice[j])
        with open(books_read, "w", encoding="utf-8") as f:
            for j in range(len(booksRead)):
                if j != i:
                    f.write(booksRead[j])

def viewBooks():
    '''
    This function allows to desplay the list of books by printing the content of the 'books.txt' file
    The file is printed line by line
    '''
    with open("books.txt", "r", encoding="utf-8") as f:
        i = 0
        for ligne in f:
            i += 1
            print(i, ":", ligne[:-1])

def viewReaders():
    '''
    This function allows to desplay the list of books by printing the content of the 'books.txt' file
    The file is printed line by line
    '''
    with open("readers.txt ", "r", encoding="utf-8") as f:
        i = 0
        for ligne in f:
            i += 1
            print(i, ":", ligne[:-1])

def addBook():
    '''
    This function allows the user to add a new book to the list only if it doesn't already exist
    The rating matrix is also edited accordingly
    The inputs are all secured with while loops
    '''
    viewBooks()
    with open("books.txt", "r", encoding="utf-8") as f1, open(rating_matrix, "r", encoding="utf_8") as f2:
        lignes = f1.readlines()
        matrice = f2.readlines()
    newbook = str(input("Enter the name of the book you want to insert into the database : "))
    i = 0
    while i < len(lignes) and newbook != lignes[i]:
        i += 1
    if i < len(lignes):
        print("The book {} is already in the  books of the database\n".format(newbook))
    else:
        print("The book {} has been added to the books of the database\n".format(newbook))
        with open(books, "a", encoding="utf-8") as b:
            b.write(newbook + "\n")
        with open(rating_matrix, "w", encoding="utf-8") as f:
            for j in range(len(matrice)):
                new_matrice_line = []
                old_matrice_line = matrice[j].strip("\n").split(" ")
                for k in range(len(old_matrice_line) + 1):
                    if k == len(old_matrice_line):
                        new_matrice_line.append("0")
                    else:
                        new_matrice_line.append(old_matrice_line[k])
                f.write(" ".join(new_matrice_line) + "\n")

def matrixCreation():
    ##This function creates the rating matrix and initialises every value of the matrix to 0
    with open(rating_matrix, "r", encoding="utf_8") as f:
        lignes = f.readlines()
    if lignes == []:
        with open(rating_matrix, "w", encoding="utf_8") as f, open("books.txt", "r", encoding="utf-8") as f1, open(
                "readers.txt", "r", encoding="utf-8") as f2:
            books = f1.readlines()
            users = f2.readlines()
            for i in range(len(users)):
                new_line = []
                for j in range(len(books)):
                    new_line.append("0")
                f.write(" ".join(new_line))
                f.write("\n")

def createBookRead():
    ##This function allows to build the 'booksread.txt' file,  when the file is empty ith the name of the readers contain in 'readers.txt'
    with open(books_read,"r",encoding="utf_8") as f:
        lignes = f.readlines()
    if lignes==[]:
        with open(books_read,"w",encoding="utf-8") as f1, open(readers,"r",encoding="utf-8") as f2:
            users=f2.readlines()
            for i in range(len(users)):
                user=users[i].split(",")
                f1.write(user[0])
                f1.write("\n")

def bookRead():
    ##This function allows the user to give the name of the books they read to update the booksread.txt file accordingly
    global readers
    global books
    global books_read
    viewReaders()
    profile = str(input("Enter your pofile's name : "))
    with open(readers, "r", encoding="utf-8") as f1, open(books,"r",encoding="utf-8") as f2, open(books_read,"r",encoding="utf-8") as f3:
        readers_lines = f1.readlines()
        books_lines = f2.readlines()
        books_read_lines = f3.readlines()
        i = 0
        while i < len(readers_lines) and not profile in readers_lines[i]:
            i += 1
    if i >= len(readers_lines):
        print("The profile {} is not in the profile database\n".format(profile))
    else:
        viewBooks()
        numberBooksRead = str(input("Enter how many book did you read : "))
        j = 0
        booksRead = []
        while j < len(books_lines) and j < int(numberBooksRead):
            numberBook = int(input("Enter the number of the book read : "))
            numberBook = int(inputVerfication(str(numberBook), 1, len(books_lines)))
            if not numberBook in booksRead and not str(numberBook) in books_read_lines[i]:
                booksRead.append(numberBook)
            else:
                print("You already enter this book's number")
            j += 1
        booksRead.sort(reverse=False)
        for j in range(len(booksRead)):
            booksRead[j] = str(booksRead[j])
        with open(books_read, "r", encoding="utf-8") as f1:
            lines = f1.readlines()
        with open(books_read, "w", encoding="utf-8") as f:
            for j in range(len(lines)):
                if j == i:
                    line = lines[j].split(",")
                    f.write(line[0].strip("\n") + ",")
                    f.write(",".join(booksRead))
                    f.write("\n")
                else:
                    f.write(lines[j])

def rateBook():
    ##This function allows the user to rate every book in the matrix rating that did not receive a grade already and update 'rating_matrix.txt' accordingly
    viewReaders()
    profile = str(input("Enter your pofile's name : "))
    with open(readers, "r", encoding="utf-8") as f1, open(books, "r", encoding="utf-8") as f2, open(books_read, "r",encoding="utf-8") as f3, open(rating_matrix,"r",encoding="utf-8") as f4:
        readers_lines = f1.readlines()
        books_lines = f2.readlines()
        books_read_lines = f3.readlines()
        matrix = f4.readlines()
        i = 0
        while i < len(readers_lines) and not profile in readers_lines[i]:
            i += 1
    if i >= len(readers_lines):
        print("The profile {} is not in the profile database\n".format(profile))
    else:
        profile_read_book = books_read_lines[i].strip("\n").split(",")
        if profile_read_book[1:] != []:
            print("You have previously read : ")
            for j in range(1,len(profile_read_book)):
                print("{} : {}".format(j,books_lines[int(profile_read_book[j])-1].strip("\n")))
            indice_books_read_lines = 1
            with open(rating_matrix,"w",encoding="utf-8") as f:
                for j in range(len(matrix)):
                    new_line = []
                    old_line = matrix[j].strip("\n").split(" ")
                    for k in range(len(old_line)):
                        if j == i and k == int(profile_read_book[indice_books_read_lines])-1:
                            grade = str(input("Enter a grade between 1 and 5 for the book {} : ".format(books_lines[k].strip("\n"))))
                            grade = inputVerfication(grade,1,5)
                            new_line.append(grade)
                            if indice_books_read_lines != len(profile_read_book)-1:
                                indice_books_read_lines+=1
                        else:
                            new_line.append(old_line[k])
                    f.write(" ".join(new_line)+"\n")
        else:
            print("You have not read any books\n")

def bookRecommandation():
    '''
    This is the function that recommend books to user using the grade he gave to other book and the other user's grade.
    Firstly, it checks if the profile of the user exsits by checking if the name given by the user exists in the lines of 'readers.txt' by giving the line if it exists.
    Secondly, it creates the similarity matrix with the grades of users given to books. The matrix is a square matrix, it's number of rows and columns is equal to othe number of readers.
    Thirdly, it gives a list of recommended books that have not been read by the user by comparing the set of books read by the user and the set of books read by the person with similar tastes
    Finally, it allows the user to choose one book among those that have not been read if they exists. If a book is chosen, it will be counted as read and the user will have the choice
    to rate the book chosen previously
    '''
    with open(rating_matrix,"r",encoding="utf-8") as f1, open(readers,"r",encoding="utf-8") as f2, open(books,"r",encoding="utf-8") as f3, open(books_read,"r",encoding="utf-8") as f4:
        matrix_lines = f1.readlines()
        readers_lines = f2.readlines()
        books_lines = f3.readlines()
        books_read_lines = f4.readlines()
    for i in range(1,len(readers_lines)+1):
        profile_line = readers_lines[i-1].strip("\n").split(",")
        print(i,":",profile_line[0])
    profile = str(input("Enter your profile's name : "))
    i = 0
    while i < len(readers_lines) and not profile in readers_lines[i]:
        i += 1
    if i >= len(readers_lines):
        print("The profile {} is not in the profile database".format(profile))
    else:
        similarity_matrix=[]
        for j in range(len(readers_lines)):
            similarity_matrix_line = []
            A = matrix_lines[j].strip("\n").split(" ")
            for k in range(len(readers_lines)):
                B = matrix_lines[k].strip("\n").split(" ")
                sum_a_b = 0
                sum_a_square = 0
                sum_b_square = 0
                for l in range(len(A)):
                    sum_a_b+=int(A[l])*int(B[l])
                    sum_a_square += int(A[l])**2
                    sum_b_square += int(B[l])**2
                if sum_a_square == 0 or sum_b_square == 0:
                    similarity_matrix_line.append(0)
                else:
                    similarity_matrix_line.append(round(sum_a_b/(sqrt(sum_a_square)*sqrt(sum_b_square)),2))
            similarity_matrix.append(similarity_matrix_line)
        profile_row = similarity_matrix[i]
        max_similarity = profile_row[0]
        max_similarity_ind = 0
        for j in range(len(profile_row)):
            if i != j:
                if max_similarity < profile_row[j]:
                    max_similarity = profile_row[j]
                    max_similarity_ind = j
        profile_book_read = books_read_lines[i].strip("\n").split(",")[1:]
        profile_book_simil = books_read_lines[max_similarity_ind].strip("\n").split(",")[1:]
        profile_no_read_book = list(set(profile_book_simil)-set(profile_book_read))

        if profile_no_read_book != []:
            print("We can recommand you these book : ")
            for j in range(len(profile_no_read_book)):
                print("{} : {}".format(profile_no_read_book[j],books_lines[int(profile_no_read_book[j])-1].strip("\n")))

            selection_choice = str(input("Do you want to select a book (y/n)? "))
            while selection_choice!='y' and selection_choice!='n':
                selection_choice = str(input("Do you want to select a book (y/n)? "))
            if selection_choice == 'y':
                selection_book = str(input("Enter the number linked to the book you are interested in : " ))
                while selection_book not in profile_no_read_book:
                    selection_book = str(input("Enter the number linked to the book you are interested in(it must among those you never read before) : "))
                with open(books_read, "w", encoding="utf-8") as f:
                    for j in range(len(books_read_lines)):
                        if j == i:
                            old_line = books_read_lines[j].strip("\n").split(",")
                            new_line = [old_line[0]]
                            temporary_new_line = []
                            for k in range(1,len(old_line)):
                                temporary_new_line.append(int(old_line[k]))
                            temporary_new_line.append(int(selection_book))
                            temporary_new_line.sort()
                            for k in range(len(temporary_new_line)):
                                temporary_new_line[k] = str(temporary_new_line[k])
                            new_line+=temporary_new_line
                            f.write(",".join(new_line))
                            f.write("\n")
                        else:
                            f.write(books_read_lines[j])
                rate_question=str(input("Do you want to rate the book (y/n)? "))
                while rate_question != 'y' and rate_question != 'n':
                    rate_question=str(input("Do you want to rate the book (y/n)? "))
                if rate_question == 'y':
                    with open(rating_matrix, "w", encoding="utf-8") as f:
                        for j in range(len(matrix_lines)):
                            new_line = []
                            old_line = matrix_lines[j].strip("\n").split(" ")
                            for k in range(len(old_line)):
                                if j == i and k == int(selection_book) - 1:
                                    grade = str(input("Enter a grade between 1 and 5 for the book {} : ".format(books_lines[k].strip("\n"))))
                                    grade = inputVerfication(grade, 1, 5)
                                    new_line.append(grade)
                                else:
                                    new_line.append(old_line[k])
                            f.write(" ".join(new_line) + "\n")
                else:
                    print(("Don't forget to rate the book !"))



#########################################################################################################################
##########################################-The Main code starts here-####################################################
#########################################################################################################################


if __name__=='__main__':
    matrixCreation()
    createBookRead()
    ##In this part of the code, we implement all the functions and how the user can navigate through them
    main_menu = mainmenu()
    while main_menu != 4:
        ##This is the implementation of the 1st part: the reader profiles
        if main_menu == 1:
            menu_book = menub()
            if menu_book ==1:
                addBook()
            elif menu_book == 2:
                replaceBook()
            elif menu_book == 3:
                deleteBook()
            elif menu_book ==4:
                viewBooks()
            elif menu_book == 5:
                main_menu = mainmenu()
        ##This is the implementation of the 2nd part: the book depository
        elif main_menu == 2:
            menu_reader = menureader()
            if menu_reader ==1:
                newprofile()
            elif menu_reader ==2:
                modifyProfile()
            elif menu_reader ==3:
                deleteProfile()
            elif menu_reader ==4:
                main_menu = mainmenu()
        ##This is the implementation of the 3rd part: the book recommendation
        elif main_menu== 3:
            menu_recommend = menuRecommend()
            if menu_recommend ==1:
                bookRead()
            elif menu_recommend ==2:
                rateBook()
            elif menu_recommend ==3:
                bookRecommandation()
            elif menu_recommend ==4:
                main_menu = mainmenu()
    print("Goodbye! See you soon!")
    quit()
