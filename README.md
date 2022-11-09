# PAYMENTS SERVICE

[![Language](https://img.shields.io/badge/language-python-green.svg)](https://github.com/sartim/fast_api_shop)
![build](https://github.com/sartim/fast_api_shop/workflows/build/badge.svg)



## Setup

**Requirements**

To run the project you will need these setup

* Python 3+
* Virtualenv
* PostgreSQL

**Setup**

    $ pip install virtualenv
    $ virtualenv <envname> -p python3
    $ source <envname>/bin/activate
    $ pip install -r requirements.txt


**Running app using manage.py for development server**

Running this will get you development server up and running

    $ python manage.py run_server

**Running app using gunicorn for production server**

Optimal number of workers ```-w``` = ```(2 x $num_cores) + 1```

    $ gunicorn main:app -w 4 -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker

