from django.conf.urls import url
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^upload/',views.upload,name ='upload'),
    url(r'^explore/', views.explore, name = 'explore'),
    url(r'^profile$', views.profile, name='profile'),
       
]
if settings.DEBUG:    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
