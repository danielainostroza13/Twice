from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index),    
    url(r'^album/$',views.album),       
    url(r'^integrantes/$',views.integrantes),
    url(r'^backstage/$',views.backstage),
    url(r'^login/$',views.ingreso,name="login"),
    url(r'^registro/$',views.registroPersona,name="registro"),
    url(r'^salir/$',views.salir,name="logout"),
]
