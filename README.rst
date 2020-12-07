[WORK IN PROGRESS]
==================

Simple Social Network Django
============================


.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django

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

Dynaconf makes it easy to change the source and format of the settings.
Supports many configuration file formats, external storages, environment
variables, databases, etc. See https://www.dynaconf.com/ for more information.
All configuration files are stored in a separate application called `config`.
The settings are moved to the `config.settings` module, and are divided into
development and production.

Basic settings are set in the `config.settings.base` module. Configs for
development and production are set in the files
`config/settings/development.toml` and `config/settings/production.toml`, for
switching between environments use environment variable `BOOKMARKS_ENV`.

.. _Dynaconf: https://www.dynaconf.com/


Credential data
---------------

The credentials are stored in a separate `.secrets.toml` file included in
`.gitignore`, and can optionally be stored in any convenient location with
dynaconf.


Using linters
-------------

If you wish to check code of the project - you need to install development
dependencies:

::

    $ pipenv install --dev

The project has configs for flake8 and pylint linters - you can use pylava_ to
test an entire project with multiple linters at a time. Pylava_ is a wrapper
over many linters includes pycodestyle, pydocstyle, pyflakes, pylint, and
others. For check - just run:

.. _Pylava: https://github.com/pylava/pylava

::

    $ pylava -l pycodestyle,pydocstyle,pyflakes,pylint

Or use a single linter. For example:

::

    $ pyflakes

::

    $ pylint <path_to_check>


Getting started
---------------

Clone this repo and change the current directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    git clone <current_repository_link>
    git cd <repository_dir>

Install dependecies
^^^^^^^^^^^^^^^^^^^

::

    $ pipenv install

Set the secrets
^^^^^^^^^^^^^^^

* Generate a secret key:

Run the python shell

* Windows

::

$ python

* Linux

::

$ python3

- Generate key

::

    >> from django.core.management.utils import get_random_secret_key
    >> get_random_secret_key
    >> <your-brand-new-secret-key!>

* Create a secrets file

- Copy .secrets.toml.example to .secrets.toml

+ Windows

::

    $ cp .\.secrets.toml.example -Destination .\.secrets.toml

+ Linux

::

    $ cp .secrets.toml.example .secrets.toml

- Change `SECRET_KEY = 'your_secret_key'` with the generated key

* Or set it in the environment variables

Linux::

        $ > export DJANGO_REST_SECRET_KEY=your-brand-new-secret-key

Windows

- Cmd

::

        $ > set DJANGO_REST_SECRET_KEY=your-brand-new-secret-key

- Powershell

::

        $ > $env:DJANGO_REST_SECRET_KEY = "your-brand-new-secret-key"

Select configuration
^^^^^^^^^^^^^^^^^^^^

Linux::

        $ > export DJANGO_REST_ENV=production

Windows

- Cmd

::

        $ > set DJANGO_REST_ENV=production

- Powershell

::

        $ > $env:DJANGO_REST_ENV = "production"

Create a database
^^^^^^^^^^^^^^^^^

Windows

::

    $ py manage.py migrate

Linux

::

    $ python3 manage.py migrate





Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the
  form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go
  to your console to see a simulated email verification message. Copy the link
  into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command

Windows:

::

    $ python manage.py createsuperuser

Linux:

::

    $ python3 manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your
superuser logged in on Firefox (or similar), so that you can see how the site
behaves for both kinds of users.

Run server
^^^^^^^^^^

Windows

::

        $ python manage.py runserver

Linux

::

        $ python3 manage.py runserver
