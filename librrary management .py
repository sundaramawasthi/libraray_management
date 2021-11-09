
class Library:
    def __init__ (self,list,name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"we have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)
    def lendBook(self,book,name):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:name})
            print("Lender-Book database has been updateed.you can take the book now")
        else:
            print(f"Book is already being used by{self.lendDict[book]}")

    def addBook(self,book):
        self.booklist.append(book)
        print("book has been added to the book list")

    def returnBook (self,book):
        self.booklist.remove(book)

if __name__=='__main__':
    harry = Library(['python','rich Daddypoor Daddy'],"codewithharry")

    while(True):
        print(f"welcome library to{harry.name} library enter choice")
        print("1.Display book")
        print("2.Lend a  book")
        print("3. Add a book")
        print("4. Return a  book")
        user_choice = int(input())
        

        if user_choice == 1:
            harry.displayBooks()

        elif user_choice == 2:
              book = input("enter the name of book want to land")
              name = input(" entter thr name usesr")
              harry.lendBook(book,name)
        elif user_choice == 3:
              book = input("enter the name")
              harry.addBook(book)
        elif user_choice == 4:
               book = input("enter the name")
               harry.returnBook(book)     

        else:
            print("not a valid option")   

        print(" q for quit  c for countinue")  
        user_choice2 =" "
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 =="q":
                exit()
            elif user_choice2 =="c":
                continue
            

