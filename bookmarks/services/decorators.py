import functools

from django.http import HttpResponseBadRequest


def ajax_required(f):
    """
    Decorator that return HttpResponseBadRequest for non-ajax requests.

    Args:
        f (function): view that accept request

    Returns:
         Function or `HttpResponseBadRequest` from `django.http`.
    """

    @functools.wraps(f)
    def wrapper(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    return wrapper
