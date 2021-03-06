# BrowseMovie
Simple website to browse for and saves favourite movies on your account.

Designed and written by **Stanisław Stępak**. All rights reserved.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* [Docker compose](https://docs.docker.com/compose/install/)

### Installing

A step by step series of examples that tell you how to get a development env running

Clone this repository:

```
git clone https://github.com/stasius12/browse-movie
```

Then build the project with - this command will also be for running site locally:

```
docker-compose up
```
After build you have also apply migrations to your local DB:

```
docker-compose run --rm web python manage.py migrate
```

Then after running site locally (docker-compose up) go to **localhost:8000** (do not use 127.0.0.1) to see it.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [docker-compose](https://docs.docker.com/compose/) - For orchestration


## Authors

* **Stanisław Stępak** - [Connect with me on LinkedIn](https://www.linkedin.com/in/stanislaw-stepak/)
