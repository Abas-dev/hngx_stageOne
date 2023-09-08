from django.urls import path
from . import views 

urlpatterns = [
    path('',views.StageOneTask.as_view(),name='firstView'),
]