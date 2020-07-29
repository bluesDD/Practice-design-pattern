#!/bin/sh

export FLASK_APP=./edit_spreadsheet/cashman/index.py
flask db init
flask db migrate
flask db upgrade
