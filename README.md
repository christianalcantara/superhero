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
  <a href="https://github.com/christianalcantara/book_backend">
    <img src="docs/images/django-logo.png" alt="Logo" height="80">
  </a>
</p>

<h3 align="center">Django Graphql</h3>

  <p align="center">
    A Django GraphQL API example with Django Graphene
    <br />
    👽&nbsp;&nbsp;<a href="https://superheroback.herokuapp.com/">Backend Demo</a>&nbsp;&nbsp;
    👽&nbsp;&nbsp;<a href="https://superherofront.herokuapp.com/">Frontend Demo</a>&nbsp;&nbsp;
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

Clique [here](https://superheroback.herokuapp.com/) to view complete demo.

### Authorization Token

- curl

```shell
curl 'https://superheroback.herokuapp.com/graphql' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Connection: keep-alive' -H 'DNT: 1' -H 'Origin: https://superheroback.herokuapp.com' --data-binary '{"query":"# CREATE USER\nmutation CreateUser {\n  createUser(\n    email: \"admin@example.com\"\n    password: \"123\"\n    username: \"adminuser\"\n  ) {\n    user {\n      username\n      firstName\n    }\n  }\n}\n"}' --compressed
```

- Graphql

```graphql
# CREATE USER
mutation CreateUser {
  createUser(
    email: "admin@example.com"
    password: "123"
    username: "adminuser"
  ) {
    user {
      username
      firstName
    }
  }
}
```

- Response

```json
{
  "data": {
    "createUser": {
      "user": {
        "username": "adminuser",
        "firstName": ""
      }
    }
  }
}
```

### Get Characters

- curl

```shell
curl 'https://superheroback.herokuapp.com/graphql' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Connection: keep-alive' -H 'DNT: 1' -H 'Origin: https://superheroback.herokuapp.com' --data-binary '{"query":"query Characters {\n  characters {\n    edges {\n      node {\n        name\n        description\n        thumbUrl\n      }\n    }\n  }\n}"}' --compressed
```

- graphql

```graphql
query Characters {
  characters {
    edges {
      node {
        name
        description
        thumbUrl
      }
    }
  }
}
```

<details>
<summary>Response</summary>

```json
{
  "data": {
    "characters": {
      "edges": [
        {
          "node": {
            "name": "Hantaro",
            "description": "Hamtaro, conhecido no Japão como Trotting Hamtaro, é uma série japonesa de mangás e contos de fadas criada e ilustrada por Ritsuko Kawai",
            "thumbUrl": "////superheroback.herokuapp.com/media/character/download_1.jpeg"
          }
        },
        {
          "node": {
            "name": "Vision",
            "description": "",
            "thumbUrl": "////superheroback.herokuapp.com/media/character/013vis_ons_crd_01-1.jpg"
          }
        },
        {
          "node": {
            "name": "Falcon",
            "description": "",
            "thumbUrl": "////superheroback.herokuapp.com/media/character/014fal_ons_crd_02.jpg"
          }
        }
      ]
    }
  }
}
```

</details>

### Create Characters

- curl

```shell
curl 'https://superheroback.herokuapp.com/graphql' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Connection: keep-alive' -H 'DNT: 1' -H 'Origin: https://superheroback.herokuapp.com' --data-binary '{"query":"mutation CreateCharacter {\n  createCharacter(\n    name: \"Loki\"\n    description: \"God of Mischief and brother to Thor, Loki’s tricks and schemes wreak havoc across the realms.\"\n  ) {\n    character {\n      id\n      created\n      name\n    }\n  }\n}\n"}' --compressed
```

- graphql

```graphql
mutation CreateCharacter {
  createCharacter(
    name: "Loki"
    description: "God of Mischief and brother to Thor, Loki’s tricks and schemes wreak havoc across the realms."
  ) {
    character {
      id
      created
      name
    }
  }
}

```

<details open="open">
<summary>Response</summary>

```json
{
  "data": {
    "createCharacter": {
      "character": {
        "id": "4",
        "created": "2021-02-24T07:19:24.881772+00:00",
        "name": "Loki"
      }
    }
  }
}
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
