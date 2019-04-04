# project-1
# Monster

Django Review
=============

A reusable Django app that lets users write reviews for any model

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    $ pip install monster tech


Add the ``Article`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
     url(r'^$', views.article_list, name="list"),

    )

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate


Usage
-----
