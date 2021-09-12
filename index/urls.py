from django.urls import path, include
from . import views
urlpatterns = [
path('index', views.index),
path('login', views.login),
path('join', views.join),
path('board', views.board),
path('write', views.write),
path('boardview', views.boardview),
path('intro', views.intro),
path('word', views.word),
path('Idiomatic', views.Idiomatic),
path('Proverb', views. Proverb),
path('Abbreviation', views.Abbreviation),
path('Idiom', views.Idiom),
]
