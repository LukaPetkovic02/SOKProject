#!/bin/bash

remove_eggs() {
  # The directory path is sent as the first argument
  cd "$1" || exit
  rm -rf build
  # shellcheck disable=SC2035
  rm -rf *.egg-info
  rm -rf dist
  cd ..
  pip uninstall -y "$1"
}

# remove build files from components
remove_eggs platform
remove_eggs api
remove_eggs block_visualizer
remove_eggs simple_visualizer
remove_eggs data_source_json
remove_eggs data_source_xml

# remove db
cd graph_explorer || exit
# shellcheck disable=SC2035
rm -f *.sqlite3  # Use -f flag to prevent error if no matching files are found
cd ..