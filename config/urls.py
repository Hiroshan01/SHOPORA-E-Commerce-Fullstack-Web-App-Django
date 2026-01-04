from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]

#Only in development mode
if settings.DEBUG:
    import django_browser_reload #noqa F401
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
