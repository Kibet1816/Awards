# Instagram

## Description

 This is a website where users can post projects and be reviewed by other users

 By **Denis Kibet**

The user can:

- Register to use the program
- Sign In to his/her profile
- Post projects and view them in the profile page
- Grade the project on creativity,usability,content and design

## Setup/Installation Requirements

### Prerequisites

- python3.6
- pip
- Virtual environment(virtual)

### Cloning and running

- Clone the application using git clone(this copies the app onto your device). In terminal:

          $ git clone https://github.com/Kibet1816/Awards.git
          $ cd Awards

- Creating the virtual environment

          $ python3.6 -m venv --without-pip virtual
          $ source virtual/bin/env
          $ curl https://bootstrap.pypa.io/get-pip.py | python

- Installing Flask and other Modules

          $ python3.6 -m pip install -r requirements.txt

- Run the application:

          $ python3.6 manage.py runserver

### Testing the Application

- To run the tests for the class files:

          $ python3.6 manage.py test

## Technologies Used

- Python 3.6
- Flask

## Behaviour driven development/ Specifications

| Behaviour               |       Sample Input       | Sample Output                                        |
| :---------------------- | :----------------------: | :--------------------------------------------------- |
| Sign Up required    |       On page load       | Registration form apperars                 |
| Registration            | Submit regitration form  | User creates an account and receives welcome email   |
| Subscription            | Submit subscription form | User receives email eb=very time there is a new post |
| Post an project          |  | Project is posted and appears on profile page |


## Support and contact details

For any questions, troubleshooting or contributions, find me on:

- Email: kibet1816@gmail.com

### License

[MIT LICENSE](https://github.com/Kibet1816/Awards/blob/master/license)
Copyright (c) {2019}
