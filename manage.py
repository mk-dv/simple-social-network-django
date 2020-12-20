#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from pathlib import Path
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line  # noqa
    except ImportError as exc:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # This allows easy placement of apps within the interior
    # `bookmarks` directory.
    current_dir = Path(__file__).parent.resolve()
    sys.path.append(str(current_dir / 'bookmarks' / 'apps'))

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
