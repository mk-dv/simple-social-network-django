from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ImageCreateForm
from .models import Image


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
            'form': form,
        }
    )


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)

    return render(
        request,
        'images/image/detail.html',
        {
            'section': 'images',
            'image': image,
        }
    )


@login_required
# Returns `HttpResponseNotAllowed`(status code 405) if method isn't POST.
@require_POST
def image_like(request):
    """
    Args:
        request(HttpRequest):
            An `HttpRequest` contains `image-id`(int) and `action`(str)
             - 'like' or 'unlike'.

    Returns:
        JsonResponse:

    Raises:
        `Model.DoesNotExist` from `django.db.models`.
    """
    image_id = request.POST.get('image-id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
        except Model.DoesNotExist:
            return JsonResponse({'status': 'ImageDoesNotExist'})

        if action == 'like':
            # It's obvious <QuerySet> excludes duplicates.
            image.users_liked.add(request.user)
        elif action == 'unlike':
            # When an attempt to delete a user who is not in liked users,
            # an exception is not thrown.
            image.users_liked.remove(request.user)

        return JsonResponse({'status': 'ok'})

    return JsonResponse({'status': 'Bad request'})

    return JsonResponse({'status': 'ok'})
