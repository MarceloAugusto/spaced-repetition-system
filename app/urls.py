from django.conf.urls import  include,url
from . import  views

urlpatterns = [
    url(r'^$', views.deck_list),
    url(r'^mydecks/', views.my_decks),
]