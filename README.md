# Technical Test - Django
[![codecov](https://codecov.io/gh/vanessavps/vanessa-project/branch/main/graph/badge.svg?token=d8E3MkQdvd)](https://codecov.io/gh/vanessavps/vanessa-project)
[![CircleCI](https://circleci.com/gh/vanessavps/vanessa-project/tree/main.svg?style=svg)](https://circleci.com/gh/vanessavps/vanessa-project/tree/main)

- Deployed on [Heroku](https://vanessa-project.herokuapp.com/) 
- There's a [Postman collection](Postman-Endpoints.postman_collection.json) (v2.1) you can use to test the endpoints on Heroku
- The project uses SQLite. It is filesystem which means Heroku will remove it when [restarts the dyno](https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem). So maybe the testing will not work on Heroku, unless the deploy is triggered again

## Installation
### Dependencies
Install the dependencies on `requirements.txt` file using:

`pip install -r requirements.txt`

### Initial data migration
There are some database initial data that needs to be migrated

`python manage.py migrate`


## Run
`python manage.py runserver`

## Code coverage
`coverage run manage.py test -v 2 `

To see the report in HTML 
Generate HTML code coverage report 

`coverage html`
