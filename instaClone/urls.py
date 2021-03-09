from django.contrib import admin
from django.urls import path,include
from users import views as users_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',users_views.registerUserView,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"),name="login"),
]