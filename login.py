
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

def check_if_unique(data,user):
    for u in data:
        if u['username'] == user:
            return True
    else:
        return False

def enter_credentials():
    USERDETAILS = load_data(path)
    user = input('Enter a username: ')
    if check_if_unique(USERDETAILS,user):
        print('User taken, please enter again')
        return enter_credentials()
    password = input('Enter a password: ')
    USERDETAILS.append({'username':user,'password_hash':password})

    save_data(path,USERDETAILS)
    print(USERDETAILS)

def is_valid_credentials(user,password):
    USERDETAILS = load_data(path)
    if USERDETAILS.get(user,None) == password:
        return True
    return False






if __name__ == '__main__':
    enter_credentials()

