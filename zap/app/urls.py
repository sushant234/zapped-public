from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings


urlpatterns = [
    path('', views.index, name='home'),
    path('blog', views.blogg, name='blog'),
    # path('singleblog', views.singleblog, name='singleblog'),
    path('ml', views.ml, name='ml'),
    path('ds', views.ds, name='ds'),
    path('wd', views.wd, name='wd'),
    path('ad', views.ad, name='ad'),
    path('catalogue', views.catalogue, name='catalogue'),
    url(r'^singleblog/(?P<value>\d+)/$', views.singleblog,name='singleblog'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)