from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('getQuery', views.getQuery),
    path('queryCallback', views.queryCallback),
    path('getRulesVersion', views.getRulesVersion),
    path('download/rules.json', views.getRuleFile),
]
