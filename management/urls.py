from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from authentication import urls as auth
from home import urls as home

urlpatterns = [
    path('auth/',include(auth)),
    path('',include(home)),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.COURSES_URL, document_root=settings.COURSES_ROOT)