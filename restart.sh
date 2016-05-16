#!/usr/bin/env bash

kill -9 `ps aux |grep Python |awk 'FNR == 1 {print $2}'`
pip install -r requirements.txt
nohup python manage.py runserver &