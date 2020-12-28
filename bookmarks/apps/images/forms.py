import requests

from pathlib import Path

from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from .models import Image


class ImageCreateForm(forms.ModelForm):
    """
    Form for create an image.

    Users will not manually enter the address. Instead, I add a JS-script
     (I hope for this) to select an image from any(I'm not sure for this)
     third-party site, and the form will receive its URL.
    """

    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        # Render to `<input type="hidden">`.
        widgets = {'url': forms.HiddenInput}

    def clean_url(self):
        """
        Compare file extension with leading dot from URI with valid extensions.

        Returns:
            url (str):
                An url of image.

        Raises:
            `ValidationError` from `django.forms` for url with not valid
              suffixes.
        """

        url = self.cleaned_data['url']
        valid_suffixes = ('.jpg', '.jpeg', '.png', '.gif')
        # Extension with leading dot.
        image_suffix = Path(url).suffix

        if image_suffix not in valid_suffixes:
            raise forms.ValidationError(
                f'The given URL({url}) does not match valid image extensions!'
            )

        return url

    # Keep `super().save()` header.
    # https://docs.djangoproject.com/en/2.2/ref/models/instances/#forcing-an-insert-or-update
    def save(self, force_insert=False, force_update=False, commit=True):
        url = self.cleaned_data['url']
        # Get an image object.
        response = requests.get(url)
        image = super().save(commit=False)
        image_slug = slugify(image.title)

        # The concatenation is quite readable in this case, but possibly `Path`
        # from `pathlib` can be better.
        # P.S.
        # `Path(image_slug).withsuffix(
        #     Path(url).suffix
        # )`
        # does not seem to be the best choice.
        filename_with_extension = image_slug + Path(url).suffix

        # The File class is a thin wrapper around a Python file object with
        # some Django-specific additions. Internally, Django uses this class
        # when it needs to represent a file. The ContentFile class inherits
        # from File, but unlike File it operates on string content (bytes also
        # supported), rather than an actual file.
        # https://docs.djangoproject.com/en/3.1/ref/files/file/#the-contentfile-class
        image.image.save(
            filename_with_extension,
            ContentFile(response.content),
            save=False
        )
        # Keep the original behavior save() - perform saving only if
        # `commit` is True.
        if commit:
            image.save()
        return image
