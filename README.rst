=============================
Associati
=============================

.. image:: https://badge.fury.io/py/dj_associati.svg
    :target: https://badge.fury.io/py/dj_associati

.. image:: https://travis-ci.org/foscomerlacci/dj_associati.svg?branch=master
    :target: https://travis-ci.org/foscomerlacci/dj_associati

.. image:: https://codecov.io/gh/foscomerlacci/dj_associati/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/foscomerlacci/dj_associati

Una semplice anagrafica soci

Documentation
-------------

The full documentation is at https://dj_associati.readthedocs.io.

Quickstart
----------

Install Associati::

    pip install dj_associati

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_associati.apps.DjAssociatiConfig',
        ...
    )

Add Associati's URL patterns:

.. code-block:: python

    from dj_associati import urls as dj_associati_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_associati_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
