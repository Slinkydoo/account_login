class Account:
    def __init__(self, username, password, first_name, last_name, email, phone, bio):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.bio = bio
        accounts = open("accounts.txt", 'a')


def create_account():
    pass


def login():
    pass