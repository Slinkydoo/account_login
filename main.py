import csv
import login

# In this project I want to try and create a simple login application that will allow you to
# create a new account, delete or deactivate an account, login, and ability to change anything in the profile.
# user = login.Account('Slinkydo', 'password', 'Ryan', 'Sleszynski', 'ryansleszynski@gmail.com', '516-654-1348' ,'')

with open('accounts_list.csv', 'r') as csv_file:
    accounts_list = csv.reader(csv_file)
    # next(accounts_list)
    for line in accounts_list:
        # print(line)
        if line[0] == 'Slinkydont':
            print('This username is taken.')
