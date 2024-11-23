README: Flask Application for User Data Collection
 
Project Overview
This Flask application collects user data, including Age, Gender, Total Income, and various Expenses, stores it in a MongoDB database, and writes the data to a CSV file for backup and processing. If MongoDB is unreachable, the application ensures a CSV file is created with appropriate headers.
 
Features
•	Collects user demographic and expense data via a web form.
•	Stores data in a MongoDB database and appends it to a CSV file.
•	Ensures data backup with headers when MongoDB is unreachable.
•	Designed for deployment on local environments or AWS.
 
Requirements
Local System Prerequisites
1.	Python 3.8 or higher.
2.	pip (Python package installer).
3.	MongoDB (local or cloud instance, e.g., MongoDB Atlas).
4.	Flask framework.

Python Dependencies
Install the required Python packages:


pip install flask pymongo

Installation and Setup

Step 1: Clone the Repository


git clone https://github.com/binbaz05/MyNexfordCodes.git
cd to the cloned folder

Step 2: Configure MongoDB
•	If using a local MongoDB instance, ensure MongoDB is running on localhost:27017.
•	If using MongoDB Atlas:
1.	Create a database and collection.
2.	Update the connection string in the flask_app.py file:
client = pymongo.MongoClient("your_mongo_uri_here")



Step 3: Run the Application
1.	Start the Flask application:

python flask_app.py

2.	Open your browser and navigate to http://127.0.0.1:5000.
 

Deployment on AWS
Step 1: Create an EC2 Instance
1.	Log in to your AWS Management Console.
2.	Navigate to EC2 and launch an instance.
3.	Choose an Amazon Linux 2 AMI or Ubuntu as the OS.
4.	Select an instance type (e.g., t2.micro for free tier).
5.	Configure security groups:
o	Allow HTTP (port 80) and SSH (port 22).
o	Open port 5000 for testing, but use port 80 in production.
Step 2: SSH into the Instance
Obtain the .pem file for your key pair, then connect to the instance:


ssh -i "your_key.pem" ec2-user@your_ec2_public_ip
Step 3: Install Required Packages
1.	Update the instance:


sudo yum update -y
or for Ubuntu:


sudo apt update && sudo apt upgrade -y
2.	Install Python and pip:


sudo yum install python3 -y  # Amazon Linux
sudo apt install python3-pip -y  # Ubuntu
3.	Install Flask and pymongo:


pip3 install flask pymongo
Step 4: Transfer Application Files
1.	Transfer files using scp:


scp -i "your_key.pem" flask_app.py ec2-user@your_ec2_public_ip:/home/ec2-user/
scp -i "your_key.pem" templates/index.html ec2-user@your_ec2_public_ip:/home/ec2-user/templates/
Step 5: Run the Flask Application
1.	Start the Flask app:


python3 flask_app.py
2.	Access the app:
o	Navigate to http://your_ec2_public_ip:5000.
Step 6: Serve the Application on Port 80 (Optional)
1.	Install gunicorn:


pip3 install gunicorn
2.	Run Flask with gunicorn:


gunicorn -w 4 -b 0.0.0.0:80 flask_app:app
3.	Access the app at http://your_ec2_public_ip.
