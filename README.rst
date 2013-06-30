Django Jack Bower
============

Installing frontend Django dependencies via bower.

Installation
------------

To get the latest stable release from PyPi::

    $ pip install jack-bower

To get the latest commit from GitHub::

    $ pip install -e git+git://github.com/mediapop/jack-bower.git#egg=bower

TODO: Describe further installation steps (edit / remove the examples below):

Add ``bower`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'bower',
    )

Add the ``bower`` URLs to your ``urls.py``::

    urlpatterns = patterns('',
        ...
        url(r'^VAR_URL_HOOK/', include('bower.urls')),
    )

Don't forget to migrate your database::

    ./manage.py migrate bower


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 jack-bower
    $ python setup.py install
    $ pip install -r dev_requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
