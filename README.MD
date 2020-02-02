## Initial Setup

### Virtual environment
A virtual environment ties the application with all its required packages into a 
1) Create virtual environment called `ll_env` by entering into terminal: 
    - `python3 -m  venv ll_env`
    - There shoudl be a new folder called `ll_env` that contains a `pyenv.cfg` file.
2) Activate the virtual environment (for Mac Os)
    - `source ll_env/bin/activate` 
     - the start of your path should now show `(ll_env)`
3) Exit or deactivate virtual environment 
    - enter `deactivate` in terminal OR close terminal to exit the virtual environment

### Setting up Django
#### Django Installation
1) Activate virtual environment
2) Install Django in terminal using
    - `pip install Django`
3) !! you MUST include the period at the end !! Create project using 
    -`django-admin.py startproject learning_log .`
    - this will create the following :
        - `manage.py` a file that directs commands to various parts of Django
        - `learning_log` directory that contains:
            - settings.py >> manages Django behavior   
            - urls.py >> manages pages Django creates
            - wsgi.py >> manages a `web server gateway interface`
#### Database Installation
1) Create the database (SQLite by default):
    - `python manage.py migrate`
    - this will create a `db.sqlite3` file 
#### Run Server
1) Run the server to verify the project setup
    - `python manage.py runserver`
    - The following default page can be seen on a browser directed to `http://127.0.0.1:8000/`
        <div>  <img  src = './django_setup_good.png' width = 40%/> </div>

    - if you accidentally close the terminal in VSCODE and need to quit the server, enter the following in a new terminal `sudo kill $(lsof -t -i:8000)`
#### Setup App
1) In a new terminal window, activate the virutal environment `source ll_env/bin/activate` and run startapp:
    - `python manage.py startapp learning_logs`
    - this will create a new directory with the following files:
        <div><img src  = './learning_logs.png' /></div>
        -  `models.py` >> manages app data
        - `admin.py` >> 
        - `views.py`   
