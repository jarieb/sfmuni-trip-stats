#!/bin/bash

cd /home/docker/code/app/

# Django settings
if [ ! -e db.sqlite3 ]
then
  python3 manage.py makemigrations
fi

python3 manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'Hello123!')" | python3 manage.py shell

python3 manage.py collectstatic --noinput


# Start all the services
/usr/bin/supervisord -n
