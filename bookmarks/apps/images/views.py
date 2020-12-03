from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ImageCreateForm


@login_required
def image_create(request):
    if request.method == 'POST':
        # The name `form` is quite meaningful - it is clear from the context
        # that this is a name, but for example, the name `image_form` would be
        # excessive.
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image added successfully')

            return redirect(new_image.get_absolute_url())
    else:
        # Passing `url` and` title` GET-params from JS to the form.
        form = ImageCreateForm(request.GET)

    return render(
        request,
        'images/image/create.html',
        {
            'section': 'images',
            'form': form
        }
    )
