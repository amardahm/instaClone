from django.contrib import admin
from django.urls import path,include
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
import posts
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',users_views.registerUserView,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"),name="login"),
    path('', include("posts.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)