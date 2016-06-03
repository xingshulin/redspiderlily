#!/usr/bin/env bash

pip install -r requirements.txt
cp /apps/config.ini /usr/src/app/module
nohup python3 manage.py runserver 0.0.0.0:8000 &