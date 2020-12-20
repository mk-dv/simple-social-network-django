from pathlib import Path
import random

from django.conf import settings


def get_random_default_profile_photo():
    app_dir = Path(settings.APPS_DIR) / 'account'
    default_photos_dir = (
         app_dir / 'static' / 'account' / 'images' / 'default_profile_photos'
    )

    default_photo_paths = tuple(
        default_photos_dir.rglob('avatar*.png')
    )

    return str(
        random
        .choice(default_photo_paths)
        .relative_to(app_dir)
        .as_posix()  # Django is used '/' for urls.
    )
