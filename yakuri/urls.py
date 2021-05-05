from django.urls import path
from .import views

app_name='yakuri'

urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('list/<int:id>',views.PharmList.as_view(),name='list'),
    path('index/<int:id>',views.PharmIndex.as_view(),name='index'),
    ]
    
