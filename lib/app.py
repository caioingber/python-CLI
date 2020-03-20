from './app.py' import models

class Interface:
    def __init__(self):
        self.length = 0
    
    def intro(self):
        option = input("""Welcome to the Contact Book. Choose from the following options: \n 
        (a) Look for a contact\n 
        (b) Add a new contact\n
        (c) Show all contacts""")
        if option == 'a':
            self.search()
        elif option == 'b':
            self.create()
        elif option == 'c':
            self.show_all()
        else:
            self.invalid()

    def show_all(self):
        query = Contact.select()
        query = list(query)
        for contact in query:
            print(f"{query.index(contact) + 1}. Name: {contact.first_name} {contact.last_name}\n Number: {contact.phone_number}\n")


    def search(self):
        search_name = input("Please Enter a First Name: ")
        query = Contact.select().where(Contact.first_name ** f"%{search_name}%")
        if query.exists():
            query = list(query)
            if len(query) > 1:
                for contact in query:
                    print(f"{query.index(contact) + 1}. Name: {contact.first_name} {contact.last_name}\n Number: {contact.phone_number}\n")
                return query
            else:
                for contact in query:
                    print(f"Name: {contact.first_name} {contact.last_name}\nNumber: {contact.phone_number}\n")
                return query
        else:
            cant_find = input("Sorry, we couldn't find that contact. Wan't to do another search? Y/N ")
            if cant_find == 'Y':
                self.search()
            else:
                self.intro()
    
    def invalid(self):
        error = input('Invalid Input - Enter "home" to go back or "exit" to leave the application ')
        if error == 'home':
            self.intro()
        elif error == 'exit':
            quit()
        else:
            self.invalid()

    def create(self):
        first = input('Enter a First Name: ')
        second = input('Enter a Last Name: ')
        number = input('Enter a Phone Number: ')
        Contact(first_name=first, last_name=second, phone_number=number).save()
        self.intro()



start = Interface()
start.intro()