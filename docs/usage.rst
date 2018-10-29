=====
Usage
=====

To use Associati in a project, add it to your `INSTALLED_APPS`:

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
