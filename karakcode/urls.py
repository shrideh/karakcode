from django.urls import path, include


urlpatterns = [
    path('', include('home.urls')),
]






# -------------------------------------------------------------------- #
# التطوير                                                              #
# -------------------------------------------------------------------- #
from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    ) # type: ignore
    urlpatterns += debug_toolbar_urls() # type: ignore
