# Project Title

## HealthThink Backend Web Application

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

    Python 3.6.9

### Installing

You'll need to have a virtual environment installed on your machine

    pip3 install virtualenv

Setup virtual environment

    virtualenv -p python3.6 .virtualenv

Activate virtual environment

    source .virtualenv/bin/activate

Install the requirements

    pip install -r requirements

Install `rabbitmq`, run the following command

    sudo apt-get update & sudo apt install rabbitmq-server

Configuring the settings

    Navigate to settings.py inside openhisa_sec* and change the setting being import to either developemnt_settings or production_settings depending on your use case

Make migrations, createsuperuser and run the server

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

### Built With

    Python - Programming language used
    Django-rest-framework - The web framework used
    django-rest-swagger - Used to generate documentation for all the endpoints

Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

### Authors

EHealth4everyone Python Web Development Team

### Acknowledgments

Regards to everyone whose contributed in the development of this project.
