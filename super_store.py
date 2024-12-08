from flask import Flask, render_template
import sqlite3

from numpy import convolve

app = Flask(__name__)


# Path to the SQLite database file


# Function to get a database connection
def get_db():
    conn = sqlite3.connect("/Users/pavithragunasekaran/Documents/DAB111/Week 12_flask/superstore.db")
    conn.row_factory = sqlite3.Row  # This allows us to access rows like dictionaries
    return conn

# Route to view users in the database

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/data')
def data():
    conn = get_db()
    
    superstore=conn.execute("select * from super_table").fetchall()
    print(superstore)
    # sample=conn.execute("create table harini1 (name char,num integer)")
    
    return render_template('data.html',data=superstore)

    # Query to get all data from the database
    # cursor.execute("select * from global_superstore")  # Adjust the table name as needed
    # rows = cursor.fetchall()

    # Close the database connection

@app.route('/Services')
def service():
    return render_template('service.html')  
@app.route('/contact')
def contact():
    return render_template('contact.html')
 
if __name__ == '__main__':
    app.run(debug=True)
