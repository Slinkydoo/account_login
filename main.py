import csv
import login

# In this project I want to try and create a simple login application that will allow you to
# create a new account, delete or deactivate an account, login, and ability to change anything in the profile.
# user = login.Account('Slinkydo', 'password', 'Ryan', 'Sleszynski', 'ryansleszynski@gmail.com', '516-654-1348' ,'')

print('Welcome to the account login practice')
print('Would you like to sign-in or sign-up?')

user_input = input('1) sign-in\n'
                   '2) sign-up')

if user_input.lower() == '1':
    pass

with open('accounts_list.csv', 'r') as csv_file:
    accounts_list = csv.reader(csv_file, delimiter=',')
    # next(accounts_list)
    for line in accounts_list:
        # print(line)
        if line[0] == 'Slinkydont':
            print('This username is taken.')
