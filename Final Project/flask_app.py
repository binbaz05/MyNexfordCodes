from flask import Flask, render_template, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import csv
from pymongo.errors import ServerSelectionTimeoutError
import os

app = Flask(__name__)

# MongoDB URI for Cloud MongoDB (MongoDB Atlas)
#mongo_uri = "mongodb+srv://<user_data>:<Tt9Yq3bQVxOLAi9d>@cluster0.r9xgh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
uri = "mongodb+srv://user_data:Tt9Yq3bQVxOLAi9d@cluster0.r9xgh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# MongoDB Setup

db = client["user_data"]
collection = db["users"]

# Define CSV file and headers

csv_file_path = 'user_data.csv'
headers = ['Age', 'Gender', 'Total Income', 'Utilities', 'Entertainment', 'School Fees', 'Shopping', 'Healthcare']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    age = request.form['age']
    gender = request.form['gender']
    total_income = request.form['income']
    expenses = {
        'utilities': request.form['utilities'],
        'entertainment': request.form['entertainment'],
        'school_fees': request.form['school_fees'],
        'shopping': request.form['shopping'],
        'healthcare': request.form['healthcare']
    }

    # Save data to MongoDB

    user_data = {
        'age': age,
        'gender': gender,
        'total_income': total_income,
        'expenses': expenses
    }
    collection.insert_one(user_data)

     # Write data to CSV

    write_mode = 'a' if os.path.exists(csv_file_path) else 'w'
    with open(csv_file_path, mode=write_mode, newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write headers if file is newly created
        if write_mode == 'w':
            writer.writerow(headers)
        # Write the row of user data
        writer.writerow([
            age, gender, total_income, 
            expenses['utilities'], expenses['entertainment'], 
            expenses['school_fees'], expenses['shopping'], 
            expenses['healthcare']
        ])

    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
