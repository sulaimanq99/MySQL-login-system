import mysql.connector

def main():
    db = mysql.connector.connect(host='localhost',
                            database = 'login_system',
                            user='sulaiman',
                            password='12345')
    mycursor = db.cursor()
    #mycursor.execute("CREATE DATABASE login_system")
    #mycursor.execute('DROP TABLE users')
    #mycursor.execute("CREATE TABLE users (username VARCHAR(255) UNIQUE , password_hash VARCHAR(255))")
    #mycursor.execute('INSERT INTO users (username, password_hash) VALUES("robert", "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f")')
    #db.commit()

if __name__ == '__main__':
  main()