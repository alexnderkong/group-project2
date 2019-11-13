#! /bin/sh
# check the database available
while ! nc -z mysql 3306; do echo "waiting for db..."; sleep1; done
#run the create scripts
python3 create.py
#run the application
python3 run.py
