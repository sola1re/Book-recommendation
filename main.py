from time import *

print("┏━━┓━━━━━━━━━┏┓━━━━━━┏━━━┓━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┏┓━━━━━━┏┓━━━━━━━━━━━━━━━┏━━━┓┏┓━━━━━━━━━━━━━━━┏┓━┏┓━━━━━━")
print("┃┏┓┃━━━━━━━━━┃┃━━━━━━┃┏━┓┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃┃━━━━━┏┛┗┓━━━━━━━━━━━━━━┃┏━┓┃┃┃━━━━━━━━━━━━━━┏┛┗┓┃┃━━━━━━")
print("┃┗┛┗┓┏━━┓┏━━┓┃┃┏┓━━━━┃┗━┛┃┏━━┓┏━━┓┏━━┓┏┓┏┓┏┓┏┓┏━━┓┏━┓━┏━┛┃┏━━┓━┗┓┏┛┏┓┏━━┓┏━┓━━━━━┃┃━┃┃┃┃━┏━━┓┏━━┓┏━┓┏┓┗┓┏┛┃┗━┓┏┓┏┓")
print("┃┏━┓┃┃┏┓┃┃┏┓┃┃┗┛┛━━━━┃┏┓┏┛┃┏┓┃┃┏━┛┃┏┓┃┃┗┛┃┃┗┛┃┃┏┓┃┃┏┓┓┃┏┓┃┗━┓┃━━┃┃━┣┫┃┏┓┃┃┏┓┓━━━━┃┗━┛┃┃┃━┃┏┓┃┃┏┓┃┃┏┛┣┫━┃┃━┃┏┓┃┃┗┛┃")
print("┃┗━┛┃┃┗┛┃┃┗┛┃┃┏┓┓━━━━┃┃┃┗┓┃┃━┫┃┗━┓┃┗┛┃┃┃┃┃┃┃┃┃┃┃━┫┃┃┃┃┃┗┛┃┃┗┛┗┓━┃┗┓┃┃┃┗┛┃┃┃┃┃━━━━┃┏━┓┃┃┗┓┃┗┛┃┃┗┛┃┃┃━┃┃━┃┗┓┃┃┃┃┃┃┃┃")
print("┗━━━┛┗━━┛┗━━┛┗┛┗┛━━━━┗┛┗━┛┗━━┛┗━━┛┗━━┛┗┻┻┛┗┻┻┛┗━━┛┗┛┗┛┗━━┛┗━━━┛━┗━┛┗┛┗━━┛┗┛┗┛━━━━┗┛━┗┛┗━┛┗━┓┃┗━━┛┗┛━┗┛━┗━┛┗┛┗┛┗┻┻┛")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┏━┛┃━━━━━━━━━━━━━━━━━━━━━")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┗━━┛━━━━━━━━━━━━━━━━━━━━━")

######################################################################################################################################
###############################Modify the file directories to access the files on your machine########################################
######################################################################################################################################

readers = 'C:\\Users\\iampa\\PycharmProjects\\book_recommendation\\readers.txt'
books = 'C:\\Users\\iampa\\PycharmProjects\\book_recommendation\\books.txt'
books_read = 'C:\\Users\\iampa\\PycharmProjects\\book_recommendation\\booksread.txt'

def mainmenu():
        global menu_principal
        menu_principal=0
        print("What menu do you want to navigate to?\n")
        menu_principal=int(input("1 : Book menu\n2 : Reader menu\n3 : Recommendation menu\n4 : Quit\n"))

def menub():
        global menu_book
        menu_book=0
        menu_book=int(input("1 : Add a book\n2 : Modify a book\n3 : Delete a book\n4 : View the book list\n5 : Go back to the main menu\n"))

def menureader():
        global menu_reader
        menu_reader=0
        print("What do you want to do?\n")
        menu_reader=int(input("1 : Add a reader\n2 : Modify a reader\n3 : Delete a reader\n4 : Go back to the main menu\n"))

def menurecommend():
        global menu_recommend
        menu_recommend=0
        print("What do you want to do?\n")
        menu_recommend=int(input("1 : Rate books\n2 : Find a new book\n3 : Go back to the main menu\n"))

def newprofile():
        global name
        global gender
        global age
        global style
        name = str(input("What is your name?\n"))
        gender = str(input("Gender selection\n1 : You are a male\n2 : You are a female\n3 : Other\n"))
        age = str(input("What is your age?\n"))
        style = str(
                input("What is you readin style?\n1 : Science-Fiction\n2 : Biography\n3 : Horreur\n4 : Romance\n5 : Fable\n6 : History\n7 : Comedy\n"))

        with open(readers, "a", encoding='utf-8') as f:
                f.write(name + "," + gender + "," + age + "," + style+"\n")
        f.close()
        print("Your profile has successfully been added!\n")
        sleep(2)
        mainmenu()

def modifyprofile():
        #Edit this code so it doesn't print the whole line, but only the profile name, in other words, everything before th first comma
        with open("fichierTest.txt", "r") as f:
                i = 0
                for ligne in f:
                        i += 1
                        print(i, ":", ligne)
        f.close()
        modreader = int(input("What line do you want to modify? \n"))

########################################Main code starts here############################################################

mainmenu()

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
                """
                Add function to Remove book line
                """
        elif menu_book ==4:
                """
                print the content of the book file
                """
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

elif menu_principal == 4:
        print("Goodbye!")
        quit()
