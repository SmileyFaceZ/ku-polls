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

### Installiation:

Install and set up a project using the [Installation](Installation.md) guide.

#### Create a virtual environment and activate it
To create a virtual environment, run the following command:

```commandline
python -m venv venv
```
or 
```commandline
python3 -m venv venv
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

### Run server:
Launch the server by running the following command:
```commandline
python manage.py runserver
```
or
```commandline
python3 manage.py runserver
```
To stop the server, simply press `Ctrl-C` in the terminal.

### Demo Account:
| Username | Password |
|----------|----------|
| demo1    | easy1    |
| demo2    | easy2    |
| demo3    | easy3    |
| demo4    | easy4    |
| demo5    | easy5    |

## Project Documents

All project documents are in the [Project Wiki](../../wiki/Home).

- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)
- [Development Plan](../../wiki/Development-Plan)
- [Iteration 1 Plan](../../wiki/Iteration-1-Plan)
- [Iteration 2 Plan](../../wiki/Iteration-2-Plan)
- [Iteration 3 Plan](../../wiki/Iteration-3-Plan)
- [Iteration 4 Plan](../../wiki/Iteration-4-Plan)
- [Project Board](../../projects?query=is%3Aopen)

## Django Tutorial:
- [Part 1](https://docs.djangoproject.com/en/4.1/intro/tutorial01/): Creation of a basic poll application.
- [Part 2](https://docs.djangoproject.com/en/4.1/intro/tutorial02/): Set up the database.
- [Part 3](https://docs.djangoproject.com/en/4.1/intro/tutorial03/): Focus on creating the public interface.
- [Part 4](https://docs.djangoproject.com/en/4.1/intro/tutorial04/): Focus on form processing and cutting down our code.
- [Part 5](https://docs.djangoproject.com/en/4.1/intro/tutorial05/): Built a web-poll application and create some automated tests.
- [Part 6](https://docs.djangoproject.com/en/4.1/intro/tutorial06/): Add a stylesheet and an image.
- [Part 7](https://docs.djangoproject.com/en/4.1/intro/tutorial07/): Focus on customizing Django’s automatically-generated admin site.