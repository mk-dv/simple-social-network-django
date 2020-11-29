"""
The `bookmarks` URL configuration.

The `urlpatterns` is list of routes URLs to views. For more information please
 see: https://docs.djangoproject.com/en/2.2/topics/http/urls/

Examples:
    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')
    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('bookmarks.apps.account.urls')),
    # List of auth-backends supported by `social_django`
    # https://python-social-auth.readthedocs.io/en/latest/backends/index.html#supported-backends
    path('social-auth/', include('social_django.urls', namespace='social')),
]

# Now Django development server can send media files by URL.
if settings.DEBUG:
    # Used for local development only. Never use Django as a static or media
    # file provider.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
