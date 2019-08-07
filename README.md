# [award_line][(https://awardline.herokuapp.com/)]
### This is a project that  assesses ones projects , awardline. Users can sign up login, view and post projects and review and rate.

 
### July 22, 2019
#### By **[ANTONY MWANIKI](https://github.com/amwaniki180)**
## Description
[AWARD-LINE](())This is a project that  assesses ones projects , awardline. Users can sign up login, view and post projects and review and rate.


## USER STORIES
1.Register and Sign in to the application.
2.Upload projects to the application.
3.See my profile with all my pictures.
4.Review the projects  on my  timeline.
5.Like or Save and leave a comment on it.

### Prerequisites
1. Ubuntu Software
2. Python3.6
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)
### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/amwaniki180/awardline`
### Activate virtual environment
Activate virtual environment using python3.6 as default handler
```bash
virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
```
### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`
### Create the Database
```bash
psql
CREATE DATABASE photos;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'awar'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True
```
### Run initial Migration
```bash
python3.6 manage.py makemigrations photos
python3.6 manage.py migrate
```
### Run the app
```bash
python3.6 manage.py runserver
```
Open terminal on `localhost:8000`
## Known bugs
Copy functionality does not work
## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - Bootstrap 3
    - JavaScript
## Support and contact details
Contact me on developer on amwaniki180@gmail.com for any comments, reviews or advice.
## License
This project is licensed under the MIT License - see the LICENSE file for details
