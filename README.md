### Web Application Django

 #Description
 A website with two screens has been relaunched. The first screen shows a table with all the records stored in the database. The second screen has a form that saves the data in the database. The form has email, package, date and quantity.
 To do all this, we used the Django framework with Python3.7, a sqlite3 database and the django and djangorestframework libraries.
 
 #Execution of the application
 1. Initialize the installation of dependencies
	```$ pip install -r requirements.txt```
 2.	Create database migrations
	```$ python manage.py makemigrations```
 3.	Apply migrations
	```$ python manage.py migrate```
 2.	Server Initialization
	```$ python manage.py runserver```