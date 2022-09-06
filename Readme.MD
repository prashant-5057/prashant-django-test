Deploying a django based rest api with postgresql backend using docker-compose

1. Create an empty project directory.
2. Create a new file called Dockerfile in your project directory.
3. Add the following content to the Dockerfile.
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

This Dockerfile starts with a Python 3 parent image. The parent image is modified by adding a new code directory.
The parent image is further modified by installing the Python requirements defined in the requirements.txt file.

4. Save and close the Dockerfile.
5. Create a requirements.txt in your project directory.
This file is used by the RUN pip install -r requirements.txt command in your Dockerfile.

6. Add the required software in the file.
7. Save and close the requirements.txt file.
8. Create a file called docker-compose.yml in your project directory.

The docker-compose.yml file describes the services that make your app. In this example those services
are a web server and database. The compose file also describes which Docker images these services use,
how they link together, any volumes they might need mounted inside the containers. Finally, the
docker-compose.yml file describes which ports these services expose. See the docker-compose.yml
reference for more information on how this file works.

9. Add the following configuration to the file.
version: "3.3"

services:
  postgres:
    image: postgres
    restart: always
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - db-data:/var/lib/postgresql/data:cached

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    env_file:
      .env
    depends_on:
      - postgres
    links:
      - postgres

      

volumes:
  db-data:

This file defines two services: The db service and the web service.

10. Save and close the docker-compose.yml file.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

These settings are determined by the postgres Docker image specified in docker-compose.yml.

3. Save and close the file.
4. Run the docker-compose up command from the top level directory for your project.
$ docker-compose up
$ docker-compose up --build
djangosample_db_1 is up-to-date
Creating djangosample_web_1 ...
Creating djangosample_web_1 ... done
Attaching to djangosample_db_1, djangosample_web_1
db_1   | The files belonging to this database system will be owned by user "postgres".
db_1   | This user must also own the server process.
db_1   |
db_1   | The database cluster will be initialized with locale "en_US.utf8".
db_1   | The default database encoding has accordingly been set to "UTF8".
db_1   | The default text search configuration will be set to "english".

. . .

web_1  | May 30, 2017 - 21:44:49
web_1  | Django version 1.11.1, using settings 'composeexample.settings'
web_1  | Starting development server at http://0.0.0.0:8000/
web_1  | Quit the server with CONTROL-C.

At this point, your Django app should be running at port 8000 on your Docker host.
On Docker for Mac and Docker for Windows, go to http://localhost:8000 on a web browser to see
the Django welcome page.

NOTE: for creating super user for django project use the script provided at the management/commands/createsu. NOTE: Modify the database settings in /settings.py


Now for migrating database to postgresql 

~$ docker-compose exec app python manage.py makemigrations
~$ docker-compose exec app python manage.py migrate