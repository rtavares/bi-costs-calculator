# Python Django Project - POC of a costs calculator for B.I..
## Goal
Get the total price of a set of selected products

## Disclaimer:
This projects is a Proof Of Concept (P.O.C.), so some functionalities may be not available or not working properly. 

## Code repository
https://github.com/rtavares/bi-costs-calculator   
Note: to help speed up the development, we used this Django blueprint - same author - as a bootstraper: https://github.com/rtavares/django-blueprint-generic-views

## Live Running and monitoring
- Deployed on [PythonAnywhere](https://www.pythonanywhere.com/) at https://openmindszone.pythonanywhere.com/    
- Live running monitoring: [Sentry](https://sentry.io/welcome/) - free tier

## Tech stack
- Programming language - [Python](https://www.python.org/) - 3.10.5
  - The project was initially developed on Python 3.12.4.    
  However, due it being deployed to PythonAnywhere that only supports Python 3.10.5, this version was adopted.   
  Also considering that the development environment should mirror the production environment. 
- Web framework - [Django](https://www.djangoproject.com/) - 5.0.7
- UI framework - [Bootstrap](https://getbootstrap.com/)  - 5
- Python version manager - [PyEnv](https://github.com/pyenv/pyenv) - 2.4.4
- Python dependencies manager - [Poetry](https://python-poetry.org/) - 1.8.3
- Project tasks manager - [Make](https://www.gnu.org/software/make/) - 3.81
- Code Version Control System - [Git](https://git-scm.com/) - 2.39.3
- DVCS host - GitHub
- OS - MacOS Sonoma - 14.5
### Development environments
- On top of local OS, inside a virtual environment
- On containers using Docker 
## Local setup
- Clone the code repository to your local development folder - `git clone https://github.com/rtavares/bi-costs-calculator.git`
  - The "project root" is the directory `project` from where the commands should be run.
- Setup Python version to 3.10.5
- Create and activate a Python virtual environment
- Install the project dependencies
  - Using Poetry: 
    - `poetry install`
    - `poetry shell`
  - Using `python -v venv <project_venv>`:
    - `<project_venv>/bin/activate`
      - `pip install -U pip`
      - `pip install -r backend/requirements.txt`
  - ### Bootstrapping the project:
    - On local, using SQlite:
      - `backend/source/products_prices/manage.py migrate --settings=products_prices.settings.development_local`
      - `backend/source/products_prices/manage.py createsuperuser --settings=products_prices.settings.development_local`
    - On containers, using PostGreSQL:
      - `make start` or `make startbg`
      - `make osshell` and once inside run `./products_prices/manage.py createsuperuser`
        - or
      - `docker-compose run backend products_prices/manage.py createsuperuser`
      - The same syntax can be used to run any `manage.py` command.
      - Migrations are run automatically every time the container starts.

## Running the project
- Locally inside the virtualenv:
  - Type `make` to see a list of available commands
  - `make run-local` starts the project locally.
- On containers:
  - `make start` or `make startbg`
- The project web page will be available on the usual Django port 8000.
  
### Questions?
Please feel free to open an issue on the GitHub repository of the project.
## To-Do
### Code
- Add TypeHints
### Application
- Login and signup pages: Manage incorrect values
- Style numbers display on a more readable form
- Add CRUD for backoffice to manage Products.
  - Once the Django Admin should not be made available for end-users.
- Create 3 user levels
  - Admin
  - Content manager
  - User
- Create a standalone Client App.
  - Vue / Nuxt / Vuetify would be a good option
### Project
- Add git pre-commit hooks
- Add tests
- Add Terraform script to deploy to AWS ECS

----



