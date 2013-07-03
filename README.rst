.. role:: python(code)
   :language: python

Jack Bower
==========

Installing frontend Django dependencies via bower.

Installation
------------

To get the latest stable release from PyPi:: bash

    $ pip install jack-bower

To get the latest commit from GitHub:: bash

    $ pip install -e git+git://github.com/Celc/jack-bower.git#egg=bower

Add ``bower`` to your ``INSTALLED_APPS``:: python

    INSTALLED_APPS = (
        ...,
        'bower',
    )


Usage
-----

Use :python:`./manage.py bower_init <app_name>` to bootstrap an app with
:python:`.bowerrc`, :python:`bower.json` and :python:`.gitignore`. Add your
dependencies to :python:`bower.json` like:: python

    {
        "dependencies": {
            "backbone": "1.0.0",
            "underscore": "1.4.4"
        }
    }

Then just run :python:`./manage.py bower_install` and it'll install all the
dependencies in all the :python:`INSTALLED_APPS` apps that has a
:python:`bower.json`. Default install path is :python:`static/libs/<library>`,
you can edit :python:`.bowerrc` to change that.

Use like normal in templates::

    {% load staticfiles %}
    {% static 'lib/bootstrap/bootstrap.js'%}

Contribute
----------

If you want to contribute to this project, please perform the following
steps:: bash

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 jack-bower
    $ node -g install bower
    $ python setup.py install

    $ git co -b feature_branch master
    # Implement your feature
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
