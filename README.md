# MoBerries Test API

## Overview

A simple API for ordering pizza. 

## Requirements

 - Python 3.6
 - Django 2.0

## Installation

 - create virtualenv
    - `virtualenv --python=python3.6 env`
 - activate virtualenv
    - `source env/bin/activate`
 - install pip dependencies
    - `pip install -r requirements.txt`
 - create the database in PostgreSQL
    - `createdb sample_moberries`
 - migrate all migration files
    - `python manage.py migrate`

## Tests

 - `python manage.py test`

## Documentations

 - API documentations are available at `/docs/`:
    - e.i. `http://localhost:8000/docs/`
