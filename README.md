# Online book management system

Introduction:
This application is an online library application, which helps the user to read a subset of e-books stored in Project Gutenberg's e-book storage site. Project Gutenberg is an initiative to provide access to the world of e-books for all internet users. Currently, all the books stored in this particular application's database point to the corresponding book in Project Gutengerg's site, and I would like to give all due credit to the initiative.


Development platforms:
This application follows the MVC (technically shared-nothing) architecture:
1. HTML 5.5, CSS and Javascript(minimal) for the presentation tier.
2. Python with Django (specific packages used could be checked in the requirements.txt file) for the logic tier.
3. MYSQL database for the persistence tier.


Deployment:
This particular application has been deployed in heroku and is currently running in the url: https://desolate-everglades-70182.herokuapp.com/library


Requirements:
1. Python 3.4 or above (https://www.python.org/)
2. pip (run python get-pip.py from the folder containing get-pip.py)
3. Django 1.11.5 or higher (pip install django)
4. pymysql 0.7.11 (pip install pymysql)
5. urllib3 1.22 (pip install urllib3)
6. requests 2.18.4 (pip install requests)
7. MYSQL 5.7 or higher


Setting it up on the local system:
1. Clone the repository
2. Ensure you have MYSQL 5.7 or above installed on the system. Run CREATE DATABASE databaseName command in mysql. Import the .sql file into mysql provided under db folder, after selecting the database you created earlier.
3. In the DatabaseConnection.txt, reset the username, password, hostname and the databasename parameters.
4. In command prompt, navigate to the project folder and enter the command 'python manage.py runserver'
5. The app would be hosted at '127.0.0.1:8000/library/'
6. Try admin login with user email: 'arjun.sureshn2000@gmail.com' and password: 'Password'. 
7. You can also try inserting a user of type 'admin' into the database created earlier. The insert statement would resemble 'INSERT INTO users(email, username, userpassword, usertype) values('admin@email', 'Administrator', 'password', 'admin');'. Following this step, you can try with useremail as 'admin@email' and password as 'password' in the admin login.


Notes:
For this project, I haven't used django models, but directly executed sql queries from python using pymysql package. This is because of the class project requirement.
