"""
Django settings for bookmarks project.

Generated by 'cookiecutter'
https://github.com/cookiecutter/cookiecutter
from 'cookiecutter-django2-simplest' template
https://github.com/mk-dv/cookiecutter-django-2-simplest/
using Django 2.2.7.

For more information on this package, see:
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see:
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import dynaconf
from dynaconf.utils.parse_conf import _jinja_formatter, converters, Lazy # noqa
from pathlib import Path


# Monkey patch adds a `@path` cast that equivalent `@jinja` but returns
# `pathlib.Path` object.
class PathFormatter:
    def __init__(self, function, token):
        self.function = function
        self.token = token

    def __call__(self, value, **context):
        return Path(self.function(value, **context))

    def __str__(self):
        return str(self.token)


def path_converter(value):
    Lazy(value, formatter=PathFormatter(_jinja_formatter, 'jinja'))


converters['@path'] = path_converter

# HERE STARTS DYNACONF EXTENSION LOAD (Keep at the very bottom of other
# settings).
# Read more at https://www.dynaconf.com/#using-django
settings = dynaconf.DjangoDynaconf(
    __name__,
    ENVVAR_PREFIX_FOR_DYNACONF='BOOKMARKS',
    CORE_LOADERS=['YAML'],
    ENV_SWITCHER_FOR_DYNACONF='BOOKMARKS_ENV',
    # Load this files in the order.
    SECRETS=['.secrets.yaml'],
    settings_files=['base.yaml', 'development.yaml', 'production.yaml'],
)
# HERE ENDS DYNACONF EXTENSION LOAD (No more code below this line)
