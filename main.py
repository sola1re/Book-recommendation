from time import *

print("Hello, welcome to this book suggestion algorithm, first: \n What would you like to do?\n")

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
## this function displays the main menu where the user can chose what menu to navigate to: the bbok menu, the reader menu, the recommendation menu, or exit the programm
        global menu_principal
        menu_principal=0
        print("What menu do you want to navigate to?\n")
        menu_principal=int(input("1 : Book menu\n2 : Reader menu\n3 : Recommendation menu\n4 : Quit\n"))
        ##The input is secured with while loops
        while menu_principal>4 or menu_principal<1:
                menu_principal = int(input("1 : Book menu\n2 : Reader menu\n3 : Recommendation menu\n4 : Quit\n"))

def menub():
        ##this function displays a sub menu where the user can decide action linked to the list of books. 
        ##The options are to modify or delete a book, to view the list of books, or to go back to the main menu
        global menu_book
        menu_book=0
        menu_book=int(input("1 : Add a book\n2 : Modify a book\n3 : Delete a book\n4 : View the book list\n5 : Go back to the main menu\n"))
        ##The input is secured with while loops
        while menu_book<1 or menu_book>5:
                menu_book = int(input("1 : Add a book\n2 : Modify a book\n3 : Delete a book\n4 : View the book list\n5 : Go back to the main menu\n"))


def menureader():
        ##this function displays a sub menu where the user can add, modify or delete a reader
        global menu_reader
        menu_reader=0
        print("What do you want to do?\n")
        ##The input is secured with while loops
        while menu_reader<1 or menu_reader>4:
                menu_reader=int(input("1 : Add a reader\n2 : Modify a reader\n3 : Delete a reader\n4 : Go back to the main menu\n"))

def menurecommend():
        ##this function displays a sub menu where the user can rate books to enhance the algorithm, or find a new book he might enjoy
        ##The input is secured with while loops
        global menu_recommend
        menu_recommend=0
        print("What do you want to do?\n")
        menu_recommend=int(input("1 : Rate books\n2 : Find a new book\n3 : Go back to the main menu\n"))
        while menu_recommend<1 or menu_recommend>3:
                menu_recommend = int(input("1 : Rate books\n2 : Find a new book\n3 : Go back to the main menu\n"))

def newprofile():
        ##this function allows to create a new user profile. It requires ton enter a name, a gender, an age, and a reading preference among those selected
        ##The inputs are secured with while loops
        global name
        global gender
        global age
        global style
        name = str(input("What is your name?\n"))
        gender = str(input("Gender selection\n1 : You are a male\n2 : You are a female\n3 : Other\n"))
        while int(gender)>3 or int(gender)<1:
                menu_recommend = int(input("1 : Rate books\n2 : Find a new book\n3 : Go back to the main menu\n"))
        age = str(input("What is your age group?\n1: below 18\n2: between 18 and 25\n3: above 25\n"))
        while int(age)<1 or int(age)>3:
                age = str(input("What is your age group?\n1: below 18\n2: between 18 and 25\n3: above 25\n"))
        style = str(input("What is you readin style?\n1 : Science-Fiction\n2 : Biography\n3 : Horreur\n4 : Romance\n5 : Fable\n6 : History\n7 : Comedy\n"))
        while int(style)>7 or int(style)<1:
                style = str(input("What is you readin style?\n1 : Science-Fiction\n2 : Biography\n3 : Horreur\n4 : Romance\n5 : Fable\n6 : History\n7 : Comedy\n"))
        with open(readers, "a", encoding='utf-8') as f:
                f.write("{},{},{},{}\n".format(name,gender,age,style))
        with  open(rating_matrix,"a",encoding="utf-8") as f, open("books.txt","r",encoding="utf-8") as f1:
                books=f1.readlines()
                new_line_recommandation = []
                for j in range(len(books)):
                        new_line_recommandation.append("0")
                f.write(" ".join(new_line_recommandation))
                f.write("\n")
        print("Your profile has successfully been added!\n")
        sleep(2)
        mainmenu()

def modifyProfile():
        ##This function allows to modify a profile
        ##It asks the user the name of the profile he wants to modify
        ##If the name of the profile exists, then it asks the user what information he wants changed: name, age, gender, reading style, or recommendation algorithm
        ##The inputs are all secured with while loops
        ##The rating matrix is also edited accordingly
        with open("readers.txt", "r",encoding="utf-8") as f, open(rating_matrix,'r',encoding='utf-8') as g:
                lignes = f.readlines()
                matrix = g.readlines()
                for ligne in lignes:
                        print(ligne[:-1])
                profile = str(input("enter the name of the profile you want to modify : "))
                i=0
                while i<len(lignes) and not profile in lignes[i]:
                        i+=1
        if i>=len(lignes):
                print("the profile {} is not in the profile database".format(profile))
        else:
                modif=lignes[i].split(",")
                newProfile=""
                name_change=str(input("do you want to change your name(y/n)? "))
                while name_change!='y' and name_change!='n':
                        name_change = str(input("do you want to change your name(y/n)? "))
                if name_change=='y':
                        newProfile+=str(input("What's your name?\n"))
                else:
                        newProfile+=str(modif[0])
                newProfile+=","
                gender_change=str(input("do you want to change your gender(y/n)? "))
                while gender_change!='y' and gender_change!='n':
                        gender_change = str(input("do you want to change your gender(y/n)? "))
                if gender_change=='y':
                        gender = str(input("Gender selection\n1 : You are a male\n2 : You are a female\n3 : Other\n"))
                        while int(gender) > 3 or int(gender) < 1:
                                gender = int(input("Gender selection\n1 : You are a male\n2 : You are a female\n3 : Other\n"))
                        newProfile+=gender
                else:
                        newProfile+=str(modif[1])
                newProfile+=","
                age_change = str(input("do you want to change your age group(y/n)? "))
                while age_change != 'y' and age_change != 'n':
                        age_change = str(input("do you want to change your age(y/n)? "))
                if age_change == 'y':
                        age = str(input("What is your age group?\n1: below 18\n2: between 18 and 25\n3: above 25\n"))
                        while int(age) < 1 or int(age) > 3:
                                age = str(input("What is your age group?\n1: below 18\n2: between 18 and 25\n3: above 25\n"))
                        newProfile += age
                else:
                        newProfile += str(modif[2])
                newProfile+=","
                genre_change = str(input("do you want to change your favourite genre(y/n)? "))
                while genre_change != 'y' and genre_change != 'n':
                        genre_change_change = str(input("do you want to change your age(y/n)? "))
                if genre_change == 'y':
                        style = str(input("What is you readin style?\n1 : Science-Fiction\n2 : Biography\n3 : Horreur\n4 : Romance\n5 : Fable\n6 : History\n7 : Comedy\n"))
                        while int(style) > 7 or int(style) < 1:
                                style = str(input("What is you readin style?\n1 : Science-Fiction\n2 : Biography\n3 : Horreur\n4 : Romance\n5 : Fable\n6 : History\n7 : Comedy\n"))
                        newProfile+=style+"\n"
                else:
                        newProfile+=str(modif[3])
                print("the profile is now {}".format(newProfile))
                with open("readers.txt","w",encoding="utf-8") as f:
                        for j in range(len(lignes)):
                                if i==j:
                                        f.write(newProfile)
                                else:
                                        f.write(lignes[j])
                reco_change = str(input("do you want to reset your recomandation algorithm(y/n)? "))
                while reco_change != 'y' and reco_change != 'n':
                        reco_change = str(input("do you want to reset your recomandation algorithm(y/n)? "))
                if reco_change == 'y':
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

def replaceBook():
        ##This function asks the user for the name of the book he wants to be replaced 
        ##The file is then edited in the proper way, the matrix is also edited accordingly
        ##The inputs are all secured with while loops
        viewBooks()
        with open("books.txt", "r", encoding="utf-8") as f1, open(rating_matrix,"r",encoding="utf_8") as f2 :
                lignes = f1.readlines()
                matrice = f2.readlines()
                book = str(input("enter the name of the book you want to replace : "))
                i = 0
                while i < len(lignes) and not book in lignes[i]:
                        i += 1
        if i >= len(lignes):
                print("the book {} is not in the books database".format(book))
        else:
                new_book=str(input("you want to replace the book {} by ".format(book)))
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


def deleteBook():
        ##This function allows the user to delete a book from the list only if it already exists
        ##The rating matrix is also edited accordingly
        ##The inputs are all secured with while loops
        viewBooks()
        with open("books.txt", "r", encoding="utf-8") as f1, open(rating_matrix, "r", encoding="utf_8") as f2:
                lignes = f1.readlines()
                matrice = f2.readlines()
        book = str(input("enter the name of the book you want to replace : "))
        i=0
        while i<len(lignes) and not book in lignes[i]:
                i+=1
        if i>=len(lignes):
                print("the book {} is not in the  books of the database\n".format(book))
        else:
                with open("books.txt","w",encoding="utf-8") as f:
                        for j in range(len(lignes)):
                                if i!=j:
                                        f.write(lignes[j])
                print("the book {} has been deleted from the available books\n".format(book))
                with open(rating_matrix, "w", encoding="utf_8") as f:
                        for j in range(len(matrice)):
                                new_matrice_line = []
                                old_matrice_line = matrice[j].strip("\n").split(" ")
                                for k in range(len(old_matrice_line)):
                                        if k != i:
                                                new_matrice_line.append(old_matrice_line[k])
                                f.write(" ".join(new_matrice_line) + "\n")

def deleteProfile():
        ##This function allows to delete a user profile, but only if it exists
        ##The rating matrix is also edited accordingly
        ##The inputs are all secured with while loops
        viewReaders()
        profile = str(input("enter the name of the profile you want to delete : "))
        with open("readers.txt","r",encoding="utf-8") as f1, open(rating_matrix,"r",encoding="utf-8") as f2:
            lignes = f1.readlines()
            matrice = f2.readlines()
            i=0
            while i<len(lignes) and not profile in lignes[i]:
                    i+=1
        if i>=len(lignes):
                print("the profile {} is not in the profile database\n".format(profile))
        else:
                with open("readers.txt","w",encoding="utf-8") as f:
                        for j in range(len(lignes)):
                                if i!=j:
                                        f.write(lignes[j])
                print("the profile {} has been deleted from the profile list\n".format(profile))
                with open(rating_matrix,"w",encoding="utf-8") as f:
                        for j in range(len(matrice)):
                                if i!=j:
                                        f.write(matrice[j])


def viewBooks():
        ##This function allows to desplay the list of books by printing the content of the 'books.txt' file
        ##The file is printed line by line
        with open("books.txt","r",encoding="utf-8") as f:
                i = 0
                for ligne in f:
                        i += 1
                        print(i, ":", ligne[:-1])
                print("\n")

def viewReaders():
        ##This function allows to desplay the list of books by printing the content of the 'books.txt' file
        ##The file is printed line by line
        with open("readers.txt ","r",encoding="utf-8") as f:
                i = 0
                for ligne in f:
                        i += 1
                        print(i, ":", ligne[:-1])
                print("\n")

def addBook():
        ##This function allows the user to add a new book to the list only if it doesn't already exist
        ##The rating matrix is also edited accordingly
        ##The inputs are all secured with while loops
        viewBooks()
        with open("books.txt", "r", encoding="utf-8") as f1, open(rating_matrix, "r", encoding="utf_8") as f2:
                lignes = f1.readlines()
                matrice = f2.readlines()
        newbook = str(input("enter the name of the book you want to insert into the database : "))
        i = 0
        while i < len(lignes) and newbook!=lignes[i]:
                i += 1
        if i < len(lignes):
                print("the book {} is already in the  books of the database\n".format(newbook))
        else:
                print("the book {} has been added to the books of the database\n".format(newbook))
                with open(books, "a", encoding="utf-8") as b:
                        b.write(newbook + "\n")
                with open(rating_matrix,"w",encoding="utf-8") as f:
                        for j in range(len(matrice)):
                                new_matrice_line = []
                                old_matrice_line = matrice[j].strip("\n").split(" ")
                                for k in range(len(old_matrice_line)+1):
                                        if k == len(old_matrice_line):
                                                new_matrice_line.append("0")
                                        else:
                                                new_matrice_line.append(old_matrice_line[k])
                                f.write(" ".join(new_matrice_line) + "\n")

def matrixCreation():
        ##This function creates the rating matrix, which takes into account the reader's prerferences
        with open(rating_matrix,"r",encoding="utf_8") as f:
                lignes = f.readlines()
                if lignes==[]:
                        with open(rating_matrix,"w",encoding="utf_8") as f, open("books.txt","r",encoding="utf-8") as f1, open("readers.txt","r",encoding="utf-8") as f2:
                                books=f1.readlines()
                                users=f2.readlines()
                                for i in range(len(users)):
                                        new_line=[]
                                        for j in range  (len(books)):
                                                new_line.append("0")
                                        f.write(" ".join(new_line))
                                        f.write("\n")


#########################################################################################################################
#######################################-The Main code starts here-#######################################################
#########################################################################################################################


if __name__=='__main__':
        matrixCreation()
        mainmenu()
        while menu_principal != 4:
                if menu_principal == 1:
                        menub()
                        if menu_book ==1:
                                addBook()
                        elif menu_book == 2:
                                replaceBook()
                        elif menu_book == 3:
                                deleteBook()
                        elif menu_book ==4:
                                viewBooks()
                        elif menu_book == 5:
                                mainmenu()

                elif menu_principal == 2:
                        menureader()
                        if menu_reader ==1:
                                newprofile()
                        elif menu_reader ==2:
                                modifyProfile()
                        elif menu_reader ==3:
                                deleteProfile()
                        elif menu_reader ==4:
                                mainmenu()

                elif menu_principal == 3:
                        menurecommend()
                        if menu_recommend ==1:
                                """
                                Call a function for the reader to rate new books to have more accurate recommendations for the future
                                """
                        elif menu_recommend ==2:
                                """
                                Call function to recommend new book to the reader based on previous grades given
                                """
                        elif menu_recommend ==3:
                                mainmenu()

        print("Goodbye!")
        quit()
