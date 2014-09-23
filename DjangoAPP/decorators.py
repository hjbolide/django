
from django.http.response import HttpResponseRedirect
from django.utils.decorators import available_attrs

from functools import wraps


def superuser_only_view(original_func):
    """
    Decorator for views that are only available for superuser.
    Otherwise it will redirect to the index page.
    """
    @wraps(original_func, assigned=available_attrs(original_func))
    def new_func(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return original_func(self, request, *args, **kwargs)
        return HttpResponseRedirect('/admin')
    return new_func