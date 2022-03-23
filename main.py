import csv

import login

# In this project I want to try and create a simple login application that will allow you to
# create a new account, delete or deactivate an account, login, and ability to change anything in the profile.
# user = login.Account('Slinkydo', 'Quantum99', 'Ryan', 'Sleszynski', 'sleszynski.ryan@gmail.com', '516-557-8823' ,'')
# with open('accounts_list.csv', 'a') as accounts:
    # accounts.write(user.username, user.password, user.first_name, user)
user = csv.reader('accounts_list.csv')
print(user)
# accounts.write(user)
# print(accounts)