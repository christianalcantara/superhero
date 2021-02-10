Dango Graphql Backend
=====================

<p align="center">
  <img src="https://alexiej.github.io/assets/img/1535976062785.0faaab3f.png" />
</p>

Features
--------

-   [12 Factor](http://12factor.net/)
-   [Django](https://www.djangoproject.com/)
-   [PostgreSQL](https://www.postgresql.org/)
-   [Graphql](https://graphql.org/)
-   [Apollo](https://www.apollographql.com/)

Usage
-----

Clone `superhero`:

    $ git clone https://github.com/christianalcantara/superhero.git

Create enviroment:

    $ cd superhero
    $ virtualenv venv
    $ pip install -r requirements.txt

Django:

    $ chmod +x manage.py
    $ ./manage.py migrate
    $ ./manage.py createsuperuser
    $ ./manage.py runserver

Django Admin URL:
-----------------
 - [http://localhost:8000/admin](http://localhost:8000/admin)
 - [demo](https://superheroback.herokuapp.com/admin)

 `Username: super`

 `Password: hero`

Graphql Playground:
-------------------
 - [http://localhost:8000/graphql](http://localhost:8000/graphql)
 - [demo](https://superheroback.herokuapp.com/graphql)