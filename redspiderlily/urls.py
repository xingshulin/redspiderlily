from django.conf.urls import include, url
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^app/', include('app.urls')),
    url(r'^status/', views.status, name='status'),
    url(r'^admin/', admin.site.urls),
]
