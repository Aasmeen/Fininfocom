# Fininfocom

This Django project is used to manipulate Employee data by hitting APIs

## Prerequisites

- [Python](https://www.python.org/downloads/) (>=3.6)
- [Django](https://www.djangoproject.com/download/) (>=3.x)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Pipenv](https://pypi.org/project/pipenv/)


## Set Up

1. Clone the project.
2. Navigate to the project dirctory and open terminal. And run following command

   `pipenv shell` to create virtual environment.

   `pipenv install` to install required dependencies.
3. Install postgresql https://www.postgresql.org/download/
4. Create new database using pgadmin.
5. Update the settings file with appropriate DATABASES settings.
6. Run the server using following commang to check if everything is working fine.

   `python manage.py runserver`
7. Terminate the server and run following command to apply the migrations.

    `python manage.py migrate`
8. Create super user using following command.

    `python manage.py createsuperuser`
9. Run the server using following command.

    `python manage.py runserver` The API will be available at http://127.0.0.1:8000/.


## CRUL requests for

### Creating an employee
curl --location 'http://127.0.0.1:8000/api/employee/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "xyz",
    "email":"xyz@gmail.com",
    "age": 25,
    "gender": "male",
    "phoneNo": "90",
    "addressDetails": {
        "hno": "123",
        "street": "xyz",
        "city": "xyz",
        "state": "xyz"
    },
    "workExperience": [
        {
            "companyName": "xyz",
            "fromDate": "20-05-2019",
            "toDate": "20-09-2021",
            "address": "xyz"
        }
    ],
    "qualifications": [
        {
            "qualificationName": "ssc",
            "fromDate": "20-05-2012",
            "toDate": "20-05-2013",
            "percentage": 85
        }
    ],
    "projects": [
        {
            "title": "xyz",
            "description": "description of the project"
        }
    ],
    "photo": ""
}
'

### Updating an employee
curl --location --request PUT 'http://127.0.0.1:8000/api/employee/emp1/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "xyz",
    "email":"xyz@gmail.com",
    "age": 25,
    "gender": "male",
    "phoneNo": "90",
    "addressDetails": {
        "hno": "123",
        "street": "xyz",
        "city": "xyz",
        "state": "xyz"
    },
    "workExperience": [
        {
            "companyName": "xyz",
            "fromDate": "20-05-2019",
            "toDate": "20-09-2021",
            "address": "xyz"
        }
    ],
    "qualifications": [
        {
            "qualificationName": "ssc",
            "fromDate": "20-05-2012",
            "toDate": "20-05-2013",
            "percentage": 85
        }
    ],
    "projects": [
        {
            "title": "xyz",
            "description": "description of the project"
        }
    ],
    "photo": ""
}
'

### Deleting an employee
curl --location --request DELETE 'http://127.0.0.1:8000/api/employee/emp1/'

### getting one employee
curl --location --request GET 'http://127.0.0.1:8000/api/employee/1/'

### getting employee list
curl --location --request GET 'http://127.0.0.1:8000/api/employee/'

