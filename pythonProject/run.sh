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
lay_egs ./platform
lay_egs ./api
lay_egs ./simple_visualizer
lay_egs ./block_visualizer
lay_egs ./data_source_json
lay_egs ./data_source_xml



run_server graph_explorer