#!/bin/bash

lay_egs() {
  pip install $1
}

run_server() {
  cd "$1" || exit
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
}


# build components



run_server graph_explorer