import hashlib
import json
path = r'C:\Users\Sulaiman\Desktop\Pythonprojects\loginsystem\venv\data.json'


def save_data(path, data):
    """
    Save data to a JSON-formatted file.

    This will overwrite previous file contents.
    """
    with open(path, "w") as user_data:
        json.dump(data, user_data)


def load_data(path):
    """
    Load JSON data from a JSON-formatted file and return it.
    """
    with open(path, "r") as user_data:
        data = json.load(user_data)

    return data


def check_if_unique(data, user):
    for u in data:
        if u['username'] == user:
            return True
    else:
        return False


def enter_credentials():
    userdetails = load_data(path)
    user = input('Enter a username: ')
    if check_if_unique(userdetails, user):
        print('User taken, please enter again')
        return enter_credentials()
    password = input('Enter a password: ')
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    userdetails.append({'username': user, 'password_hash': password_hash})

    save_data(path, userdetails)
    print(userdetails)


def is_valid_credentials(user, password):
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    userdetails = load_data(path)
    for u in userdetails:
        if u['username'] == user and u['password_hash'] == password_hash:
            return True
    return False

def login():
    user = input('Enter username: ')
    password = input('Enter password: ')
    if is_valid_credentials(user, password):
        print('Logged in')
        return
    else:
        print('Invalid combination, please try again')
        return login()

if __name__ == '__main__':
    while True:
        choice = input('Enter 1 to add new users or 2 to login: ')
        if choice == '1':
            enter_credentials()
        elif choice == '2':
            login()
            break


