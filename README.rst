Django Jack Bower
=================

Installing frontend Django dependencies via bower.

Installation
------------

To get the latest stable release from PyPi::

    $ pip install jack-bower

To get the latest commit from GitHub::

    $ pip install -e git+git://github.com/mediapop/jack-bower.git#egg=bower

Add ``bower`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'bower',
    )


Usage
-----

In your Django app you can place the normal bower files `.bowerrc` and
`bower.json`.

`/my_app/.bowerrc`::

    {
      "directory": "static/libs"
    }

`/my_app/bower.json`::

    {
        "dependencies": {
            "backbone": "1.0.0",
            "underscore": "1.4.4",
            "bootstrap-daterangepicker": "git://github.com/dangrossman/bootstrap-daterangepicker.git"
        }
    }

Then just run `./manage.py bower_install` and it'll install all the dependencies
in all the `INSTALLED_APPS` apps that has a `bower.json`.


Contribute
----------

If you want to contribute to this project, please perform the following steps::

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
