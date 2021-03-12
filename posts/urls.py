from django.urls import path
from . import views
urlpatterns = [
    path('publish/',views.Publish,name="publish"),
    path('',views.home,name="home"),
    path('<int:pk>/',views.PostDetail.as_view(),name="post-detail"),
    path('<int:pk>/update/',views.Update,name="update"),
]
