import login

# In this project I want to try and create a simple login application that will allow you to
# create a new account, delete or deactivate an account, login, and ability to change anything in the profile.

accounts = open("accounts.txt", "a")

user = login.Account('Slinkydo', 'Quantum99', 'Ryan', 'Sleszynski', 'sleszynski.ryan@gmail.com', '516-557-8823' ,'')
accounts.write(user)
print(accounts)