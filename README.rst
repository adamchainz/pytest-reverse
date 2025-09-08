==============
pytest-reverse
==============

.. image:: https://img.shields.io/github/actions/workflow/status/adamchainz/pytest-reverse/main.yml.svg?branch=main&style=for-the-badge
   :target: https://github.com/adamchainz/pytest-reverse/actions?workflow=CI

.. image:: https://img.shields.io/pypi/v/pytest-reverse.svg?style=for-the-badge
   :target: https://pypi.org/project/pytest-reverse/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

Pytest plugin to reverse test order.

----

**Testing a Django project?**
Check out my book `Speed Up Your Django Tests <https://adamchainz.gumroad.com/l/suydt>`__ which covers loads of recommendations to write faster, more accurate tests.
I created pytest-reverse whilst working on the book!

----

Installation
============

Install with:

.. code-block:: bash

    python -m pip install pytest-reverse

Python 3.9 to 3.14 supported.

Usage
=====

Pytest will automatically find the plugin and use it when you run ``pytest``.
You can reverse test order by passing the ``--reverse`` flag:

.. code-block:: bash

    pytest --reverse

You can make this always apply by adding it to the ``addopts`` setting in your
``pytest.ini`` (or `other configuration
file <https://docs.pytest.org/en/latest/customize.html#adding-default-options>`__):

.. code-block:: ini

    [pytest]
    addopts = --reverse

History
=======

I'm the creator and maintainer of
`pytest-randomly <https://github.com/pytest-dev/pytest-randomly>`__, a plugin
for randomly ordering tests. @thbde opened an issue there pointing to the paper
`Empirically revisiting the test independence
assumption <https://dl.acm.org/doi/10.1145/2610384.2610404>`__, which covers
test reordering techniques. It turns out that reversal is nearly as effective
as randomization.

Test reversal is available `in Django's test
runner <https://docs.djangoproject.com/en/dev/ref/django-admin/#cmdoption-test-reverse>`__.
I figured such an option or plugin would exist for pytest already, but it
didn't, so I made it here.
