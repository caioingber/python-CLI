from model import *

class App:
    def intro(self):
        option = input("""Welcome to the Contact Book. Choose from the following options: \n 
        (a) Look for a contact\n 
        (b) Add a new contact\n
        (c) Show all contacts\n
        (d) Delete Contact\n
        (e) Leave \n""")
        if option == 'a':
            self.search()
        elif option == 'b':
            self.create()
        elif option == 'c':
            self.show_all()
        elif option == 'd':
            self.delete()
        elif option == 'e':
            quit()
        else:
            print("Invalid Input")
            self.home()

    def show_all(self):
        query = Contact.select()
        query = list(query)
        for contact in query:
            print(f"{query.index(contact) + 1}. Name: {contact.first_name} {contact.last_name}\n Number: {contact.phone_number}\n")
        self.home()

    def search(self):
        search_name = input("Please Enter a First Name: ")
        query = Contact.select().where(Contact.first_name ** f"%{search_name}%")
        if query.exists() and search_name != '':
            query = list(query)
            if len(query) > 1:
                for contact in query:
                    print(f"{query.index(contact) + 1}. Name: {contact.first_name} {contact.last_name}\n Number: {contact.phone_number}\n")
                # return query
                self.home()
            else:
                for contact in query:
                    print(f"Name: {contact.first_name} {contact.last_name}\nNumber: {contact.phone_number}\n")
                # return query
                self.home()
        else:
            cant_find = input("Sorry, we couldn't find that contact. Wan't to do another search? Y/N ")
            if cant_find == 'Y':
                self.search()
            else:
                self.intro()
        
    
    def home(self):
        error = input('Enter "home" to go back or "exit" to leave the application ')
        if error == 'home':
            self.intro()
        elif error == 'exit':
            quit()
        else:
            self.home()

    def create(self):
        first = input('Enter a First Name: ')
        second = input('Enter a Last Name: ')
        number = input('Enter a Phone Number: ')
        Contact(first_name=first, last_name=second, phone_number=number).save()
        self.intro()
    
    def delete(self):
        first = input("Enter a First Name: ")
        second = input("Enter a Second Name: ")
        person = list(Contact.select().where(Contact.first_name == first, Contact.last_name == second))
        if person is None:
            print("Sorry, contact does not exist")
            self.home()
        else:
            for contact in person:
                print(f'Name: {contact.first_name} {contact.last_name}\nNumber: {contact.phone_number}\nContact ID: {contact.id}')
            remove = int(input("Enter contact ID to remove from contact book: "))
            query = Contact.get_or_none(Contact.id == remove)
            if query is not None:
                print(f"{query.first_name} {query.last_name} has been deleted")
                query.delete_instance()
                self.home()
            else:
                print("Sorry, contact does not exist")
                self.home()

start = App()
start.intro()