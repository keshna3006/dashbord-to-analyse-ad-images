from django.contrib import admin
from django.urls import path,include
from app_imgs import views

urlpatterns= [
    path("",views.dashboard,name="dashboard"),
    path('upload',views.upload_view,name='upload')
]