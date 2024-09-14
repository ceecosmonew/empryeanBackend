from django.urls import path
from . import views

urlpatterns = [
    path('poststudentInfo/', views.post_studentInfo_api_views, name='poststudentInfo'),
    path('getstudentInfo/', views.get_studentInfo_api_views, name='getstudentInfo')
]