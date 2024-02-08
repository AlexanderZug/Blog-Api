#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate

for dump in dumps/*dump.json; do
  python3 manage.py loaddata "$dump"
done
