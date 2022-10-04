from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('retete', views.retete, name='retete'),
    path('condimente', views.condimente, name='condimente'),
    path('blog', views.blog, name='blog'),
    path('join', views.join, name='join'), 
]

urlpatterns += staticfiles_urlpatterns()