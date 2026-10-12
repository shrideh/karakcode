from django.core.cache import cache
from django.conf import settings
from functools import wraps



def cache_page_custom(timeout, keyprefix):

    def decorator(view_func):

        if settings.DEBUG:
            return view_func

        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):

            page_key = ".".join(
                [f"{k}_{v}" for k, v in kwargs.items()]
            )

            request_type = (
                "ajax"
                if request.headers.get("x-requested-with") == "XMLHttpRequest"
                else "normal"
            )

            query_string = request.GET.urlencode()

            cache_key = (
                f"{keyprefix}."
                f"type_{request_type}."
                f"{page_key}."
                f"{query_string}"
            )

            response = cache.get(cache_key)

            if response:
                return response

            response = view_func(request, *args, **kwargs)

            cache.set(cache_key, response, timeout)

            return response

        return _wrapped_view

    return decorator