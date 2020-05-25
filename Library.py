class Library:
    try:
        def __init__(self):
            import pyodbc
            self.db = pyodbc.connect('Driver=SQL Server;'
                                 'server=localhost;'
                                 'Database=Library;'
                                 'Trusted_connection=yes;')
            self.cursor = self.db.cursor()
    except Exception:
        print("Whoops!Something went Wrong!")
        print("Please Verify your Internet connectivity.")    

    def displayavailablebook(self):
        print("Available Book :")
        self.availablebook = self.cursor.execute("Select * From tbl_library_master where current_status='Available'")
        for row in self.availablebook:
            print(row.books_name)

    def lendbook(self, requestedbook):
        self.cursor.execute("Select current_status From tbl_library_master where books_name='" + requestedbook + "'")
        result1 = self.cursor.fetchone()
        # print(result1)
        if result1 is  not None:
            for row in result1:

                if row == "Available":
                    self.cursor.execute(
                        "update tbl_library_master set current_status='Lended' where books_name='" + requestedbook + "'")
                    if self.cursor.rowcount > 0:
                        self.db.commit()
                        print("Successful! You Lented " + requestedbook)
                    else:
                        print("Please enter the vaild book name!.")

                else:
                    print("This book is already lended by someone.")

                    print("Already Lended!")
        else:
            print("Please enter the vaild book name!.")

    def add_book(self, returnedbook):
        self.cursor.execute("Select current_status From tbl_library_master where books_name='" + returnedbook + "'")
        result2 = self.cursor.fetchone()
        # print(result1)
        if result2 is  not None:
            for row in result2:
                if row == "Lended":
                    self.cursor.execute(
                        "update tbl_library_master set current_status='Available' where books_name='" + returnedbook + "'")
                    if self.cursor.rowcount > 0:
                        self.db.commit()
                        print("Successful! You Returned the  " + returnedbook + " book.")
                    else:
                        print("Already exist!")

                else:
                    print("This book is already in library")
                    print("Please enter the vaild book name!.")

        else:
            print("Please enter the vaild book name!.")


class Customer:
    def requestbook(self):
        self.book = input("Enter book for request : ")
        return self.book

    def returnbook(self):
        self.book = input("ENter book going to be returned:")
        return self.book

library = Library()
customer = Customer()
print("1-Display availablebook.")
print("2-RequestBook.")
print("3-ReturnBook.")
print("4-Quit.")
while True:
    try:
        userchoice = int(input("Enter choice :"))
        if userchoice is 1:
            library.displayavailablebook()
        elif userchoice is 2:
            requestedbook = customer.requestbook()
            library.lendbook(requestedbook)
        elif userchoice is 3:
            returnedbook = customer.returnbook()
            library.add_book(returnedbook)
        elif userchoice>4 or userchoice<=0:
            print("Please enter Positive num below 4")
        elif userchoice==4:
            quit()
    except ValueError:
        print("Whoops!Something went Wrong!")
        print("Please Enter Any Number.")
