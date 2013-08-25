.. role:: bash(code)
   :language: bash

Jack Bower
==========

.. image:: https://api.travis-ci.org/Celc/jack-bower.png?branch=master
        :target: https://travis-ci.org/Celc/jack-bower

.. image:: https://coveralls.io/repos/Celc/jack-bower/badge.png?branch=master
        :target: https://coveralls.io/r/Celc/jack-bower?branch=master

.. image:: https://pypip.in/v/jack-bower/badge.png
        :target: https://crate.io/packages/jack-bower 

.. image:: https://pypip.in/d/jack-bower/badge.png
        :target: https://crate.io/packages/jack-bower

Installing frontend Django dependencies via bower.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install jack-bower

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/Celc/jack-bower.git#egg=bower

Add ``bower`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'bower',
    )


Usage
-----

Use :bash:`./manage.py bower_init <app_name>` to bootstrap an app with
``.bowerrc``, ``bower.json`` and ``.gitignore``. Add your
dependencies to ``bower.json``

.. code-block:: javascript

    {
        "dependencies": {
            "backbone": "1.0.0",
            "underscore": "1.4.4"
        }
    }

Then just run :bash:`./manage.py bower_install` and it'll install all the
dependencies in all the ``INSTALLED_APPS`` apps that has a
``bower.json``. Default install path is ``static/bower_components/<library>``,
you can edit ``.bowerrc`` to change that.

Use like normal in templates::

    {% load staticfiles %}
    {% static 'components/bootstrap/bootstrap.js'%}

Contribute
----------

If you want to contribute to this project, please perform the following
steps:

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 jack-bower
    npm install -g bower
    make develop

    git add . && git commit
    # Send us a pull request
