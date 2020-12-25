[WORK IN PROGRESS]
==================

Simple Social Network Django
============================

.. image:: https://travis-ci.org/mk-dv/simple-social-network-django.svg?branch=release-0.1
   :target: https://travis-ci.org/mk-dv/simple-social-network-django

.. image:: https://codecov.io/gh/mk-dv/simple-social-network-django/branch/release-0.1/graph/badge.svg?token=AAJNX6IT5R
   :target: https://codecov.io/gh/mk-dv/simple-social-network-django

.. image:: https://api.codeclimate.com/v1/badges/4c21f9716b5b39187a8a/maintainability
   :target: https://codeclimate.com/github/mk-dv/simple-social-network-django/maintainability
   :alt: Maintainability

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
   :target: https://github.com/pydanny/cookiecutter-django/
   :alt: Built with Cookiecutter Django

.. image:: https://img.shields.io/docker/build/mk-dv/simple-social-network-django
   :target: https://www.docker.com/get-started
   :alt: Docker Build Status

.. image:: https://img.shields.io/github/license/Naereen/StrapDown.js.svg
   :target: https://github.com/Naereen/StrapDown.js/blob/master/LICENSE

An example of a social network written on Django.
-------------------------------------------------

Features
--------
* For Django 2.2.X

* Works with Python 3.8

* 12-Factor_ based settings

* Working with users - authorization, registration, profiles.

* Easy and Powerful Settings Configuration with Dynaconf_

* Optimized development and production settings in toml_ format.

* Pipenv for installing packages, and managing the virtual environment.

* Configs for flake8 and Pylint.

.. _12-Factor: http://12factor.net/
.. _toml: https://github.com/toml-lang/toml

Using Dynaconf_ for configuration
---------------------------------

Dynaconf makes it easy to change the source and format of the settings. Supports many configuration file formats, external storages, environment variables, databases, etc. See https://www.dynaconf.com/ for more information. All configuration files are stored in a separate application called `config`. The settings are moved to the `config.settings` module, and are divided into development and production.

Basic settings are set in the `config.settings.base` module. Configs for development and production are set in the files `config/settings/development.toml` and `config/settings/production.toml`, for switching between environments use environement variable `BOOKMARKS_ENV`.

.. _Dynaconf: https://www.dynaconf.com/


Credential data
---------------

The credentials are stored in a separate `.secrets.toml` file included in `.gitignore`, and can optionally be stored in any convenient location with dynaconf.


Using linters
-------------

The project contains configs for flake8 and pylint linters:

* flake8

::

    $ flake8 <path_to_check>

* pylint

::

    $ pylint <path_to_check>


Gettings started
----------------

Create a database
^^^^^^^^^^^^^^^^^
::

    $ python manage.py migrate

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command

::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Select configuration
^^^^^^^^^^^^^^^^^^^^
Linux::

        $ > export BOOKMARKS_ENV=production

Windows

- Cmd

::

        $ > set BOOKMARKS_ENV=production

- Powershell

::

        $ > $env:BOOKMARKS_ENV = "production"

Run server
^^^^^^^^^^

::

        $ python manage.py runserver


:License: MIT
