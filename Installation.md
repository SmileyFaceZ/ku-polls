# Run and Install

<hr>

### Steps to install and run the project.
#### [Step 1](#step-1): Clone the Repository
#### [Step 2](#step-2): Check the Directory
#### [Step 3](#step-3): Install the Required Modules
#### [Step 4](#step-4): Create a Virtual Environment and Activate It
#### [Step 5](#step-5): Run Tests
#### [Step 6](#step-6): Database Migrations
#### [Step 7](#step-7): Run the Server

<hr>

## Step 1: Clone the repository
Clone the repository and using this command on terminal:
```commandline
git clone https://github.com/SmileyFaceZ/ku-polls.git
```

## Step 2: Check the directory
To ensure that your are in the correct directory (ku-polls), run the following command:

Windows:
```commandline
cd
```

macOS / Linux:
```commandline
pwd
```

If you are not in the correct directory, navigate to the project directory before proceeding with the installation:
```commandline
cd ku-polls
```

## Step 3: Install the required modules

Installing the required `Python` modules by executing the following command:
```commandline
pip install -r requirements.txt
```

To verify that all modules are installed, run the following command:
```commandline
pip list
```

## Step 4: Create a virtual environment and activate it
To create a virtual environment, run the following command:

```commandline
python -m venv venv
```

To activate the virtual environment, use one of the following commands:

Windows
```commandline
venv\Scripts\activate
```

macOS / Linux:
```commandline
source venv/bin/activate
```

The command prompt should changes to show the virtual env is active.

> #Windows
> 
> (env) cmd>
> 
> #macOS / Linux
> 
> (env) $

If you want to deactivate the virtual environment, run the following command:

```commandline
deactivate
```

## Step 5: Run test

To execute the test, run the following command:
```commandline
python manage.py test
```

## Step 6: Database migrations

To create a new database, run the following command:
```commandline
python manage.py migrate
```

Load the initial data for the polls app, run the following command:

```commandline
python manage loaddata data/polls.json data/users.json
```


## Step 7: Run server
Launch the server by running the following command:
```commandline
python manage.py runserver
```
To stop the server, simply press `Ctrl-C` in the terminal.
