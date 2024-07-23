import mysql.connector

def create_user(username, password):
    conn = mysql.connector.connect(user='user', password='passwd', host='127.0.0.1', database='test_db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
    conn.commit()
    cursor.close()
    conn.close()

def read_user(username):
    conn = mysql.connector.connect(user='user', password='passwd', host='127.0.0.1', database='test_db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_user(username, new_password):
    conn = mysql.connector.connect(user='user', password='passwd', host='127.0.0.1', database='test_db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET password = %s WHERE username = %s', (new_password, username))
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(username):
    conn = mysql.connector.connect(user='user', password='passwd', host='127.0.0.1', database='test_db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE username = %s', (username,))
    conn.commit()
    cursor.close()
    conn.close()
