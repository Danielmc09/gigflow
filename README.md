<p align="center">
  <img src ="https://miro.medium.com/max/720/1*DNTrumUzUjbQg3M00l9m9Q.webp" />
</p>

# Challenge gigflow


This API was created to make two GET type requests

- '/services/' : shows us all types of services with their respective relationships
- '/service/{id}' : shows us a specific service with its relations

## Clone the repository

```bash
https://github.com/Danielmc09/gigflow.git
```
## Create virtual env and activate 

```bash
create:
  virtualenv name_env 
  
activate:
  On Unix or MacOS, using the bash shell: source venv/bin/activate
  On Windows using the Command Prompt: path\venv\Scripts\activate.bat
```
## Install libraries

```bash
pip install -r requirements.txt
```

## Create .env

```bash

from django.core.management.utils import get_random_secret_key

#### DJANGO ####
SECRET_KEY=get_random_secret_key()
DEBUG=False

#### DATABASE ####
DATABASE_ENGINE=django.db.backends.postgresql_psycopg2
DATABASE_NAME=postgresql
DATABASE_USER=postgres
DATABASE_PASS=root
DATABASE_HOST=localhost
DATABASE_PORT=5432

#### DATABASE TEST ####
DATABASE_TEST_ENGINE=django.db.backends.sqlite3
DATABASE_TEST_NAME=test_db.sqlite3

#### USER PG_ADMIN ####
PGADMIN_USER=user@user.co
PGADMIN_PASS=user

```

## Run proyect

```bash
python manage.py runserver
```

## Create migrations

```bash
- python manage.py makemigration
- python manage.py migrate
```

## Run Test

```bash
Inside the project at the manage.py file run the following commands

- coverage run ./manage.py test
- coverage report -m

the first command runs the Tests declared in the tests folder, the second command displays the coverage
```
#### - To create test data, you can create a super user and via django admin register some data

## API with Docker

```bash
already having the .env file configured, you just need to stand at the root of the project and run 

 - docker-compose up --build 

and wait for the containers to deploy, You can enter localhost:80 enter the connection data to pgadmin
create a new server with the information from the example postgres image.

- server: db_postgres
- maintenance: root
- user: root
- password: root

At the time of entering you will find the database created with the migrations already carried out

```

## Note for Docker 

- In the event that the data you entered in the .env for the database does not work for you, you can try these
```bash
DATABASE_ENGINE=django.db.backends.postgresql_psycopg2
DATABASE_NAME=root
DATABASE_USER=root
DATABASE_PASS=root
DATABASE_HOST=db_postgres
DATABASE_PORT=5432

```
- To create information within docker, create a super user, enter the admin of
Django and create some data, to be queried 
```
 docker exec -it <container_id> python manage.py createsuperuser
```

- To run the tests from the container and see the report, run the following commands 
```
 - docker exec -it <container_id> coverage run manage.py test
 - docker exec -it <container_id> coverage report
```


## General notes 

- Note that all containers must be connected to the same network in order for them to work together

- The database used in this project is postgresql

- Ports to use that should not be busy or with local services turned off:
  - Django: 8000
  - Postgresql: 5432

|Path|Verb|Body params|
|----|----|----|
|Local|
|http://localhost:8000/services/|GET||
|http://localhost:8000/service/{id}|GET|int|
|http://localhost:8000/swagger/|GET||
|http://localhost:8000/redoc/|GET||


Autor: <a href="https://www.linkedin.com/in/angeldanielmendieta/">Angel Daniel Menideta Castillo</a> © 2022
