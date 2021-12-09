from time import *

print("Hello, welcome to this book suggestion algorithm, first: \n What would you like to do?\n")

######################################################################################################################################
###############################Modify the file directories to access the files on your machine########################################
######################################################################################################################################

readers = 'readers.txt'
books = 'books.txt'
books_read = 'booksread.txt'

def mainmenu():
        ## this function display the main menu where the user can chose what he wants ti di
        global menu_principal
        menu_principal=0
        print("What menu do you want to navigate to?\n")
        menu_principal=int(input("1 : Book menu\n2 : Reader menu\n3 : Recommendation menu\n4 : Quit\n"))
        while menu_principal>4 or menu_principal<1:
                menu_principal = int(input("1 : Book menu\n2 : Reader menu\n3 : Recommendation menu\n4 : Quit\n"))

def menub():
        ##this function display a sub menu where the user can decide action linked to the book or the list of books
        global menu_book
        menu_book=0
        menu_book=int(input("1 : Add a book\n2 : Modify a book\n3 : Delete a book\n4 : View the book list\n5 : Go back to the main menu\n"))
        while menu_book<1 or menu_book>5:
                menu_book = int(input("1 : Add a book\n2 : Modify a book\n3 : Delete a book\n4 : View the book list\n5 : Go back to the main menu\n"))


def menureader():
        ##this function display a sub menu where the user can add, modify ir delete a reader
        global menu_reader
        menu_reader=0
        print("What do you want to do?\n")
        menu_reader=int(input("1 : Add a reader\n2 : Modify a reader\n3 : Delete a reader\n4 : Go back to the main menu\n"))

def menurecommend():
        ##this function display a sub menu where the user can rate or find a new book
        global menu_recommend
        menu_recommend=0
        print("What do you want to do?\n")
        menu_recommend=int(input("1 : Rate books\n2 : Find a new book\n3 : Go back to the main menu\n"))
        while menu_recommend<1 or menu_recommend>3:
                menu_recommend = int(input("1 : Rate books\n2 : Find a new book\n3 : Go back to the main menu\n"))

def newprofile():
        ##this function allows to create a new profile
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
        f.close()
        print("Your profile has successfully been added!\n")
        sleep(2)
        mainmenu()

def modifyprofile():
        ##this function allows to modify a profile
        #Edit this code so it doesn't print the whole line, but only the profile name, in other words, everything before th first comma
        with open("readers.txt", "r",encoding="utf-8") as f:
                i = 0
                for ligne in f:
                        i += 1
                        print(i, ":", ligne[:-1])
        f.close()
        modreader = int(input("What line do you want to modify? \n"))

def deleteBook():
        book = str(input("enter the book you want to delete : "))
        with open("books.txt",'r',encoding="utf-8") as f:
            lignes = f.readlines()
            i=0
            while i<len(lignes) and not book in lignes[i]:
                    i+=1
        if i>=len(lignes):
                print("the book {} is not in the  books of the database".format(book))
        else:
                with open("books.txt","w",encoding="utf-8") as f:
                        for j in range(len(lignes)):
                                if i!=j:
                                        f.write(lignes[j])
                print("the book {} has been deleted from the available books".format(book))

def deleteProfile():
        profile = str(input("enter the name of the profile you want to delete : "))
        with open("readers.txt",'r',encoding="utf-8") as f:
            lignes = f.readlines()
            i=0
            while i<len(lignes) and not profile in lignes[i]:
                    i+=1
        if i>=len(lignes):
                print("the profile {} is not in the profile database".format(profile))
        else:
                with open("readers.txt","w",encoding="utf-8") as f:
                        for j in range(len(lignes)):
                                if i!=j:
                                        f.write(lignes[j])
                print("the profile {} has been deleted from the profile list".format(profile))

def viewBooks():
        with open("books.txt","r",encoding="utf-8") as f:
                i = 0
                for ligne in f:
                        i += 1
                        print(i, ":", ligne[:-1])
                sleep(2)
                print("\n")

                            


########################################Main code starts here############################################################
if __name__=='__main__':
        mainmenu()
        while menu_principal != 4:
                if menu_principal == 1:
                        menub()
                        if menu_book ==1:
                                """
                                Add function to append a book to the book file
                                """
                        elif menu_book == 2:
                                """
                                Add function to replace a book by one he enters
                                """
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
                                modifyprofile() #can be improved, see the function for more
                        elif menu_reader ==3:
                                """
                                Function to delete a line
                                """
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
