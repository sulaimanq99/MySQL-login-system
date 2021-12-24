import mysql.connector
import hashlib

db = mysql.connector.connect(host='localhost',
                                 database='login_system',
                                 user='sulaiman',
                                 password='12345')
mycursor = db.cursor()

def enter_credentials(cursor):
    user = input('Enter a username: ')
    mycursor.execute("SELECT count(*) from users WHERE username=%s", (user,))
    count = (list(k for k in mycursor))[0][0]
    if count == 1:
        print('User taken try again')
        return (enter_credentials(cursor))
    password = input('Enter a password: ')
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    mycursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (user, password_hash))
    db.commit()

def is_valid_credentials(user, password):
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    mycursor.execute("SELECT * FROM users WHERE username=%s and password_hash=%s", (user, password_hash))
    if not list(k for k in mycursor):
         return False
    return True

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
        choice = input('Enter 1 to register or 2 to login: ')
        if choice == '1':
            enter_credentials(mycursor)
        elif choice == '2':
            login()
            break

