# DEPI-DevOps Project

- **By** [**Omar Barakat**](https://linkedin.com/in/omarbarakota/)

## Table Of Content

[1- Description](#1--description)

[2- Installation](#2--installation)

- [2.1- Dependencies install](#install-dependencies)

- [2.2- Run Application](#run-application)

[3- Testing](#3--testing)

[Best Practices Followed](#best-practices-followed)

[Folder Structure](#folder-structure)

[Future Notes](#future-notes-if-you-will-edit)

## 1- Description

This is a website made **By** [**Omar Barakat**](https://linkedin.com/in/omarbarakota/)
That has alot of functionalities to apply **DevOps** tools and technicques

### Features

- Text To QRcode Generator
- Password Generator
- Weather Provider
- Real Time Clock
- Maps Provider
- To-Do List
  
## 2- Installation

---

Finally  To Create Virtual Enviroment:

```bash
python3 -m venv venv
```

Now you created venv folder which is your virtual enviroment
To run terminal commands inside the virutal Enviroment use

On Linux

```bash
source venv/bin/activate
```

On Windows

```shell
venv\Scripts\activate
```

### Clone the repo and navigate to the project directory

Note that `~/Project_directory` is the location you've selected on your PC make sure you're in venv (Virtual Enviromnet)

```bash
git clone https://github.com/omarbarakota/DevOps_Project.git
cd venv
```

### Install dependencies

```bash
pip install -r requirments.txt
```

### Run application

the application will be available at `http://localhost:8000`

```bash
gunicorn wsgi
```

## 3- Testing

### Tests

   1. **Run All tests:**

      Use `python3 -m pytest` to execute the test suite for the application:
      That file has all scripts to be run

      ````bash
      python3 -m pytest
      ````

      This ensures all functionalities are working correctly.

   1. **Run Specific test:**

      Open the terminal in `/tests` file and make sure that the project is running
      Use `python3 tests_name.py` to execute the needed test case:

      ````bash
      python3 tests_name.py
      ````

      This ensures each functionality is working correctly.

## Best Practices Followed

- **Virtual Environment**: Utilization of `venv` for package management, ensuring a clean environment isolated from system-wide Python packages.

- **Separation of Concerns**: HTML templates are stored in the `templates/` directory, maintaining separation between front-end and back-end logic.

- **Testing**: Integration of automated tests (`pytest`) to verify application functionality, ensuring reliability and consistency.

## Folder Structure

````bash
DevOps Project
      │
      └── main.py                   # Main Flask application file
      ├── templates/             # HTML templates (separation of concerns)
      │   └── index.html         # Main page template
      │   └── Generate.html      # Page that generates QR Code template
      │   └── Password.html      # Page that generates Password template
      │   └── Weather.html       # Page that Get the weather of a city
      ├── tests/
      │   └── test_qr.py         # Test QR generation feature for the application
      │   └── test_tasks.py      # Test Do do list features for the application
      │   └── test_time.py       # Test time display for the application
      │   └── test_weather.py    # Test weather display feature for the application
      │   └── test_password.py   # Test suite for the application
      └── requirements.txt       # List of dependencies
````

## Future notes if you will edit

To make all libraries, verions and dependencies together to easy download them later (Don't not run this command)

```bash
pip freeze > requirments.txt
```

- make all new test files in `/tests` folder

- Any new test files are created add it in `run_test.py`

- all new HTML files put it in `/templates` folder

- whenever you want to deactivate your virtual enviroment

```bash
source deactivate
```
