[![Coverage Status](https://coveralls.io/repos/github/R0ixy/epam_project/badge.svg?branch=main)](https://coveralls.io/github/R0ixy/epam_project?branch=main)

# EPAM Online UA Python final project - Department App
## With this app you can:
- ### display a list of departments and the average salary (calculated automatically) for these departments
- ### display a list of employees in the departments with an indication of the salary for each employee and a search field to search for employees born on a certain date or in the period between dates
- ### change (add / edit / delete) the above data

## How to build this project:
- ### Navigate to the project root folder
- ### Optionally set up and activate the virtual environment:
```
virtualenv venv
source env/bin/activate
```

- ### Install the requirements:
```
pip install -r requirements.txt
```
- ### Configure MySQL database
- ### Set the following environment variables:
```
SECRET_KEY=<flask secret key>
DB_USERNAME=<your database username>
DB_PASSWORD=<your database password>
DB_HOST=<your database host>
DB_PORT=<your database port>
```
*You can set these in .env file as the project uses dotenv module to load 
environment variables*
- ### Run migrations to create database infrastructure:
```
flask db upgrade
```
- ### Run the project locally:
```
python -m flask run
```
## Now you should be able to access the web service and web application on the following addresses:

- ### Web Service:
```
localhost:5000/api/departments
localhost:5000/api/departments/<department_id>

localhost:5000/api/employees
localhost:5000/api/employees/<employee_id>
localhost:5000/api/employees/?id=<department_id>
localhost:5000/api/employees/?first_date=<YYYY-MM-DD>
localhost:5000/api/employees/?start_date=<YYYY-MM-DD>&second_date=<YYYY-MM-DD>
localhost:5000/api/employees/?id=<department_id>&first_date=<YYYY-MM-DD>
localhost:5000/api/employees/?id=<department_id>&first_date=<YYYY-MM-DD>&second_date=<YYYY-MM-DD>
```
- ### Web Application:
```
localhost:5000/
localhost:5000/login
localhost:5000/register

localhost:5000/departments
localhost:5000/departments/add
localhost:5000/departments/edit
localhost:5000/departments/delete/<id>

localhost:5000/employees
localhost:5000/employees/<department_id>
localhost:5000/employees/add
localhost:5000/employees/edit
localhost:5000/employees/delete/<id>