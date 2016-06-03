#!/usr/bin/env bash

pip install -r requirements.txt

file="/apps/config.ini"
if [ -f "$file" ]
then
    cp "/apps/config.ini" "/usr/src/app/module"
fi

nohup python3 manage.py runserver 0.0.0.0:8000 &
