[![Django CI](https://github.com/christianalcantara/superhero/actions/workflows/django.yml/badge.svg)](https://github.com/christianalcantara/book_backend/actions/workflows/django.yml)
[![Updates](https://pyup.io/repos/github/christianalcantara/superhero/shield.svg)](https://pyup.io/repos/github/christianalcantara/superhero/)
[![Python 3](https://pyup.io/repos/github/christianalcantara/superhero/python-3-shield.svg)](https://pyup.io/repos/github/christianalcantara/superhero/)
[![GitHub issues](https://img.shields.io/github/issues/christianalcantara/superhero)](https://github.com/christianalcantara/superhero/issues)
[![GitHub forks](https://img.shields.io/github/forks/christianalcantara/superhero)](https://github.com/christianalcantara/superhero/network)
[![GitHub stars](https://img.shields.io/github/stars/christianalcantara/superhero)](https://github.com/christianalcantara/superhero/stargazers)
[![GitHub license](https://img.shields.io/github/license/christianalcantara/superhero)](https://github.com/christianalcantara/superhero/blob/main/LICENSE)

<!-- PROJECT LOGO -->
<br />
<p align="center">

[![Django Logo][django-logo]](https://book-backend-rest.herokuapp.com/)

</p>

[![Product Name Screen Shot][product-screenshot]](https://book-backend-rest.herokuapp.com/)

<h3 align="center">Django Graphql</h3>

  <p align="center">
    A Django GraphQL API example with Django Graphene
    <br />
    👽&nbsp;&nbsp;<a href="https://book-backend-rest.herokuapp.com/">Backend Demo</a>&nbsp;&nbsp;
    👽&nbsp;&nbsp;<a href="https://book-backend-rest.herokuapp.com/">Frontend Demo</a>&nbsp;&nbsp;
    <br />
    🐛&nbsp;&nbsp;<a href="https://github.com/christianalcantara/book_backend/issues">Report Bug</a>&nbsp;&nbsp;
    ✳&nbsp;&nbsp;<a href="https://github.com/christianalcantara/book_backend/issues">Request Feature</a>
  </p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#deploy-heroku">Deploy Heroku</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#authorization-token">Authorization Token</a></li>
        <li><a href="#get-customers">Get Customers</a></li>
        <li><a href="#get-books">Get Books</a></li>
      </ul>
    </li>
    <li>
       <a href="#roadmap">Roadmap</a>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://book-backend-rest.herokuapp.com/)

- Modern Python development with Python 3.8+
- Bleeding edge Django 3.0+
- PostgreSQL 11.6+
- Complete [Graphql](https://graphql.org/) and [Apollo](https://www.apollographql.com/) integration
- Always current dependencies and security updates enforced by [pyup.io](https://pyup.io/).
- A slim but robust foundation -- just enough to maximize your productivity, nothing more.

<!-- GETTING STARTED -->

## Getting Started

This is an example of how you may give instructions on setting up your project locally. To get a local copy up and
running follow these simple example steps.

### Deploy Heroku

Use Heroku button to deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Installation

<p align="center">

[![asciicast](https://asciinema.org/a/Q1GGnI1ZfcT5WJxCCvBBoiobN.svg)](https://asciinema.org/a/Q1GGnI1ZfcT5WJxCCvBBoiobN)

</p>

1. Clone the repo

   ```bash
   $ git clone https://github.com/christianalcantara/superhero.git

   # jump do path
   $ cd superhero
   ```

2. Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).
   ```bash
   $ virtualenv venv
   $ source venv/bin/activate
   $ pip install -r requirements.txt
   ```
3. Create dotenv file and define enviroment variables.

   ```bash
   $ touch .env
   $ echo "DEBUG=True
    SECRET_KEY=8/drD!+NQTm;e|4M6F:Z1^S{;6&NcQG$)K_P;aTqlN*{xXd+}5
    ALLOWED_HOSTS=*
    DATABASE_URL=postgres://devmetal:123@localhost:5432/superhero
    GRAPHQL_ENDPOINT=http://localhost:8000/graphql" > .env
   ```

4. Migrate the database and run

   ```shell
   $ python manage.py migrate
   # run
   $ python manage.py runserver
   ```

5. Run tests
   ```shell
   $ python manage.py test
   ```

<!-- USAGE -->

## Usage

Clique [here](https://django.herokuapp.com/) to view complete API endpoints.

### Authorization Token

- curl

```bash
curl -X POST "https://book-backend-rest.herokuapp.com/api-token-auth/" -H "accept: application/json" -H "Content-Type: application/json" -H "X-CSRFToken: uoQy2P3gGWwG3jPtI9puLIazKmvGBnmd9KYUK6bopcUuAdyxYaY5YRJOs4s5d22N" -d "{ \"username\": \"admin@gmail.com\", \"password\": \"adminpassword\"}"
```

- Response

```json
{
  "token": "71b3e6c42f5305a2ee4a1a2b46631662ab12a83b"
}
```

### Get Customers

```bash
curl --location --request GET 'https://book-backend-rest.herokuapp.com/api/customers/' --header 'Authorization: Token 71b3e6c42f5305a2ee4a1a2b46631662ab12a83b'
```

<details>
<summary>Response</summary>

```json
{}
```

</details>

### Get Characters

```bash
curl --location --request GET 'https://book-backend-rest.herokuapp.com/api/books'
```

<details>
<summary>Response</summary>

```json
{}
```

</details>

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/christianalcantara/superhero/issues) for a list of proposed features (and
known issues).

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

<a href="mailto:christian.douglas.alcantara@gmail.com">Christian Douglas Alcântara </a>

Project Link: [https://github.com/christianalcantara/superhero](https://github.com/christianalcantara/superhero)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[product-screenshot]: docs/images/screenshot.png
[django-logo]: docs/images/django-logo.png
