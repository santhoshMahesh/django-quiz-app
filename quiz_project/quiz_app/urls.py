from django.urls import path,include
from quiz_app import views

urlpatterns=[
    path('',views.index,name='index'),
]
