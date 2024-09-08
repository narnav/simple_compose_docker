from flask import Flask, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    # Connect to SQLite database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Create a table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')
    
    # Insert a sample user if the table is empty
    cursor.execute('SELECT * FROM users')
    if len(cursor.fetchall()) == 0:
        cursor.execute("INSERT INTO users (name) VALUES ('John Doe')")
        conn.commit()
    
    # Fetch all users from the database
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    
    # Format the result as a list of dictionaries
    users_list = [{"id": user[0], "name": user[1]} for user in users]
    
    # Return JSON response
    return jsonify(users=users_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
