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
#### Create new project called `learning_log`    
1) !! you MUST include the period at the end !! Create project using 
    - `django-admin.py startproject learning_log .`
2) this will create the following :
    - `manage.py` a project specific file that directs commands to various parts of Django. Specifically, it
        - puts proejct packages on the `sys.path`
        - sets up the `DJANGO_SETTINGS_MODULE` environment variable so that it points to the project settings file
    - `learning_log` directory that contains:
        - settings.py >> manages Django behavior   
        - urls.py >> manages pages Django creates
        - wsgi.py >> manages a `web server gateway interface`
    #### Although `django-admin` is the CLI for adminstrative tasks, it is simpler to manage a project through `manage.py`
#### Database Installation
1) Create the database (SQLite by default):
    - `python manage.py migrate`
2) this will create a `db.sqlite3` file 
#### Run Server to view the boiler plate project
1) Run the server to verify the project setup
    - `python manage.py runserver`
    - The following default page can be seen on a browser directed to `http://127.0.0.1:8000/`
        <div>  <img  src = './django_setup_good.png' width = 40%/> </div>

2) If you accidentally close the terminal in VSCODE and need to quit the server, enter the following in a new terminal
    - `sudo kill $(lsof -t -i:8000)`
#### Create Django setup files for new app called `learning_logs`
1) In a new terminal window, activate the virtual environment 
    -`source ll_env/bin/activate` 
2) Run startapp to build initial infrastructure files
    - `python manage.py startapp learning_logs`
3) This will create a new directory with the following files:
        <div><img src  = './learning_logs.png' /></div>
    - `models.py` >> manages app data
    - `admin.py` >> displays models in the django admin panel
    - `views.py` >> views are a Python function or class that takes a web request and return a web response. In Django, views have to be created in the app's views.py file  
#### Define models
Models are simply clases that define how Danjgo should interact with the app's data. 