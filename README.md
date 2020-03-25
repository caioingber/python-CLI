# Python Contact Book

This application replicates a contact book and is intended to be utilized via the command line. Currently, the application allows users to read, create, and delete contacts from a locally run PostgreSQL database.

## Getting Started

To run the application locally, please ensure you have pipenv installed on your machine and fork and clone the repository. Once the repo has been cloned locally, run `pipenv install` to install dependencies. Ensure that you are running Postgres on your machine and update the user and password in model.py to match that of your local Postgres DB.

Connect to your Postgres from the root level of this directory DB and run `\i lib/setup.sql`.

Enter the `pipenv shell` and run the following commands (in order):

```Python

python model.py
python seed.py
python app.py

```

## Development

I began the project by simply first creating my database connection and then templating the singular Contact Model. The model as of now remains simple, consisting of just a first & last name, as well as a phone number. The application itself functions as a class and create, read and delete are all methods called within the App class.

I began by writing pseudocode highlighting the user experience and began by implementing read functionality. There is both an option to search for a specific contact as well as list all contacts in the book. I then implemented create functionality and finished with delete.

## Unsolved Problems

In future iterations of this project I would like to implement edit functionality so that a user can update contacts. Additionally, I would like to improve the overall user experience by building a UI using tkinter or pygame.

## Challenges

I struggled most implementing a user friendly search that would list all similar contacts based off the input of the first name. To solve this issue I used the 'like' operator in PeeWee looping through the list of contacts to find similar matches:

```Python

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
```

## Technologies Used

- Python
- PeeWee
- PostgreSQL

## Contributing

I welcome any and all contributions to this project. Please fork, clone and submit a pull request with description of any changes made.
