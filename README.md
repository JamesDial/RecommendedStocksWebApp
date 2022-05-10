# CSC 450 - Team Project
## Team Members
James Dial,
Mike McKinnon,
Ethan Kenny,
Nathan Pelt,
kris valdez


## Description
For this project we're building a finance website that helps the user have a better understanding in investing in crypto and stocks. This project will be created from HTML, CSS, Flask, and SQL Alchemy. Yahoo Finance API, CoinMarketCap API, and Bezinga API will be external websites used to implent a stock list, a crpto list and the latest news in the stock market for this finance website called U-FI. This website will have a simple login/signup page and when there done with it they will have to complete a questionnaire of 5 questions. When the user has completed the questionnaire they will be given a stock and a crytocurrency watchlist based on the answers they gave. The dashboard will have a regualr watchlist that the user will be able to add cryptocurrencies and stocks they want to watch and a stock and crypto watchlist based on the answers they gave from the questionnaire. The dashboard will also display the latest news articles from the stock market and crypto market. The user will also be able to search crypto and stocks they want to watch from the search bar and clicking on if they want to search for stocks or cryptocurriences. 


## Developer Setup
1. First, use PyCharm professional. You get this for free with a .edu email address.
2. Right click the `app` folder 'Mark Directory As' -> 'Sources Root'
3. Right click the `templates` folder -> Mark Directory As -> Template Folder
4. Create a new virtual environment
    1. If you have an existing `venv` or `.venv` folder, delete it.
    2. File -> Settings -> Project: team-project-team6 -> Python interpreter
    3. Click the Gear icon -> Add. 
    4. Check the New Environment radio button. PyCharm should suggest a `venv` or `.venv` folder in the project directory -- this is fine. Make sure that the "Base Interpreter" is a Python 3 interpreter.
    5. Click 'OK' and allow PyCharm to create the virtual environment and configure the interpreter.
5. Open a new Terminal window in PyCharm. Type the commands 
```
cd src
pip install -r requirements.txt
```
6. Create a new Run Configuration from dropdown next to the run buttons:
   1. In the Run/Debug Configurations window, click the + icon.
   2. Select Flask Server
   3. Next to target type click "Script path". Select the folder icon below it and select the ufi.py file in the file picker dialog.
   4. Check the FLASK_DEBUG checkbox.
   5. In the "Working Directory" box, click the folder icon, and then select the src/app/ folder.
   6. You should now be able to run the Flask ufi.py configuration to start the server.
7. If at any time you change the Database models in `models.py`, you will need to run the following from the Terminal for the database to update with the new structure
```
flask db stamp head
flask db migrate
flask db upgrade
```
----



HeroKu Requirements 

install in requirements.txt 

newsapi==0.1.1

newsapi-python==0.2.6

gunicorn

psycopg2-binary

Deploying to heroku steps 

1. Creating a Heroku account,

2. Installing the Heroku CLI,

3. Setting Up Git, 

4. Creating a Heroku Application, 

5. Working with a Heroku Postgres Database, 

6. Updates to Requirements, 

7. The Procfile,

8. Deploying the Application, 

9. Deploying Application Updates



From the Welcome Page, click the link "Reset database" link at the bottom to purge and initialize the database with some new users:

* kris@example.com, 1234pass
* mike@example.com, word5678
* james@example.com, marv8902

Currently:
* The login page works and **is connected to the database**
* The stock list Dashboard will display, but **_is not_** conencted to the database
* The Signup page will display, but _**is not**_ connected to the database

To pre-load some Stock or Crypto data into the database, add it to the `reset` method in `ufi_database.py` and click the "Reset Database" link.
