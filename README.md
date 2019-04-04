Monster Tech
The above project is an article review blog.
One must have an account in order to edit or post articles
On posting your article you will include a picture to it, the blog will use the default one.


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

The next step you will take is to create “account” where you will be able to upload and write your own articles with will be displayed on the “monster_view” app for all views to see. 
    


get_reviews
+++++++++++

An assignment tag, that simply returns the reviews made for the given object.
An example usage would look like this:

.. code-block:: html.
% extends "base_layout.html" %}

{% block content %}
    <h1>Article List</h1>
    <div class="article">
      {% for article in articles %}
<div class="article">
            <h2><a href="{% url 'articles:details' slug=article.slug %}">{{ article.title }}</a></h2>
            <p>{{ article.snippet }}</p>
            <p>{{ article.date }}</p>
        </div>
      {% endfor %}
    </div>
{% endblock %}~




The above  set of ~code~ outputs the snippet of the article to all views whether registered or not.

user_has_reviewed
+++++++++++++++++

To quickly check if a user has already reviewed the given object, you can use
the admin panel.



Settings
--------

Default behaviour:


* Users can post multiple reviews on one object
* Users can always update their posted reviews


REVIEW_ALLOW_ANONYMOUS
++++++++++++++++++++++

Can only view the snippet of the articles but must have an active account in order enjoy full access. 




REVIEW_DELETION_SUCCESS_URL
+++++++++++++++++++++++++++

Name of the URL to redirect to after deleting a review instance. This could
be your review listing, for example.


REVIEW_UPDATE_SUCCESS_URL (optional)
++++++++++++++++++++++++++++++++++++

Default: DetailView of the instance.

Name of the URL to redirect to after creating/updating a review instance.
This could be your review listing, for example.

.. code-block:: python

    REVIEW_UPDATE_SUCCESS_URL = 'my_view_name'


Or you can also specify a function, that returns the full path. The function
then takes the review as parameter, so you can also access the reviewed item
like follows

.. code-block:: python

    REVIEW_UPDATE_SUCCESS_URL = lambda review:<form class="site-form" action="{% url 'articles:create' %}" method="post" enctype="multipart/form-data">



REVIEW_AVOID_MULTIPLE_REVIEWS
+++++++++++++++++++++++++++++

Avoids multiple reviews by one user, if set to ``True``.
Doesn't work with anonymous users.


REVIEW_PERMISSION_FUNCTION
++++++++++++++++++++++++++

Custom function to check the user's permission. Use a function and note that
the user and the reviewed item are only parameters.

.. code-block:: python

    REVIEW_PERMISSION_FUNCTION = lambda u, item: u.get_profile().has_permission(item)


REVIEW_UPDATE_PERIOD
++++++++++++++++++++

You can limit the period, in which a user is able to update old reviews.
Make sure to use minutes, e.g. 2880 for 48 hours.


REVIEW_CUSTOM_FORM
++++++++++++++++++

You can create your own review form (e.g. if you want to make use of the review
extra info). Just name it.


You can also use a custom form to add another content object to the review
instance.




Contribute
----------

If you want to contribute to this project,

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    
    # Implement your feature and tests
    
    # Send us a pull request for your feature branch
