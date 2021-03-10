from django.urls import path
from . import views
urlpatterns = [
    path('publish/',views.Publish,name="publish"),
    path('',views.home,name="home"),
]