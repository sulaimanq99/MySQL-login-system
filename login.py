

USERDETAILS = {}

def enter_credentials():
    user = input('Enter a username: ')
    if user in USERDETAILS:
        print('Sorry user taken, please try again')
        return enter_credentials()
    password = input('Enter a password: ')

    USERDETAILS[user] = password
    print(USERDETAILS)

def is_valid_credentials(user,password):
    if USERDETAILS.get(user,None) == password:
        return True
    return False






if __name__ == '__main__':
    print(USERDETAILS)
    enter_credentials()

