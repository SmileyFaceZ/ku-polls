[![Unit Test](https://github.com/SmileyFaceZ/ku-polls/actions/workflows/python-app.yml/badge.svg)](https://github.com/SmileyFaceZ/ku-polls/actions/workflows/python-app.yml)

## KU Polls: Online Survey Questions 

An application to conduct online polls and surveys based
on the [Django Tutorial project][django-tutorial], with
additional features.

This app was created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at Kasetsart University.

## Install and Run

### Clone the Repository:
Clone the repository and using this command on terminal.
```commandline
git clone https://github.com/SmileyFaceZ/ku-polls.git
```

### Installing:

To check that your are working on the correct directory (ku-polls), use this command.

Windows
```commandline
cd
```

macOS / Linux:
```commandline
pwd
```

If you are not in the correct directory, change to the project directory before proceeding with the installation.
```commandline
cd ku-polls
```

Installing the required modules by using code blocks
```commandline
pip install -r requirements.txt
```

To check if all modules are installed, use this command.
```commandline
pip list
```

To create a new database using this command.
```commandline
python manage.py migrate
```

### Running the server:
Run the following command to start the server.
```commandline
python manage.py runserver
```
To stop the server, you can press `Ctrl-C` in the terminal.

## Project Documents

All project documents are in the [Project Wiki](../../wiki/Home).

- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)
- [Development Plan](../../wiki/Development-Plan)
- [Iteration 1 Plan](../../wiki/Iteration-1-Plan)
- [Iteration 2 Plan](../../wiki/Iteration-2-Plan)
- [Project Board](../../projects?query=is%3Aopen)

[django-tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)