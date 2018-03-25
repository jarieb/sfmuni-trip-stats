# sfmuni-trip-stats

##Description##
SFMuni Trip stats is a Django application that collects travel times for muni commuters and compares
those trips times to the RESTbus API for SF-MTA: http://restbus.info/api/agencies/sf-muni/

##Requirements##
1) Install Python 3

2) Install virtualenv
    See https://virtualenv.pypa.io/en/stable/

3) Clone "sfmuni-trip-stats" repo. Move into repo's root directory
    $ git clone https://github.com/jarieb/sfmuni-trip-stats.git 
    $ cd sfmuni-trip-stats 

4) Create virtual python3 environment
    $ virtualenv -p python3 venv

5) Activate virtual environment
    $ . venv/bin/activate

6) Install required Python components
    $ pip install -r requirements.txt

7) Create initial SQLite3 database
    $ python manage.py migrate

8) Create application's root user
    $ python manage.py createsuperuser
    $ user: ____
    $ email: ____
    $ password: ____
    $ repeat: _____

9) Launch application
    $ python manage.py runserver (note: in Django 2, IP:port no longer necessary)
