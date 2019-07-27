# Flask Tutorial
This documentation is for Windows. Please refer to official docs for usage in other OS

## Installation
*Requirement: Python 3.0 or newer.*

1. `py -3 -m venv venv` (makes a new virtual environment)
2. `venv\Scripts\activate` (activates the virtual environment)
3. `pip install flask` (installs flask in the virtual environment)

## Alternative installation method
`pip install -e .`

## How to run in development mode
*Make sure the virtual environment is activated first (venv\Scripts\activate).*

1. `set FLASK_APP=flaskr` (set environment variable)
2. `set FLASK_ENV=development` (set environment variable)
3. `flask init-db` (initialize the sqlite database)
4. `flask run` (runs the server)

## How to run unit tests
`coverage run -m pytest`

## How to create a production build
1. `py setup.py bdist_wheel` (creates a distribution file)
2. Find the `dist/flaskr-1.0.0-py3-none-any.whl` file, copy it to another machine.

## Installing the production build
1. `pip install flaskr-1.0.0-py3-none-any.whl`
2. `export FLASK_APP=flaskr`
3. `flask init-db`
4. `python -c "import os; print(os.urandom(16))"` (outputs a random string)
5. Create `config.py` file in the instance folder.
6. Put `SECRET_KEY = <RANDOM_STRING>` in the config.py file

## Run the production server
`waitress-serve --call 'flaskr:create_app'`