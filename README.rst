.. role:: python(code)
   :language: python

.. role:: bash(code)
   :language: bash

Jack Bower
==========

Installing frontend Django dependencies via bower.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    $ pip install jack-bower

To get the latest commit from GitHub

.. code-block:: bash

    $ pip install -e git+git://github.com/Celc/jack-bower.git#egg=bower

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
``bower.json``. Default install path is ``static/libs/<library>``,
you can edit ``.bowerrc`` to change that.

Use like normal in templates::

    {% load staticfiles %}
    {% static 'lib/bootstrap/bootstrap.js'%}

Contribute
----------

If you want to contribute to this project, please perform the following
steps:

.. code-block:: bash

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
