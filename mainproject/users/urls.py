from django.urls import path
from . import views
from . import Script
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.home, name='home'),
                  path('submits/', views.submits),
                  path('external/', views.external),
                  path('aboutus.html/', views.aboutus, name='aboutus'),
                  path('home.html/', views.homes, name='homes'),
                  path('register/', views.register, name='register'),
                  path('profile/', views.profile, name='profile'),
                  path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
                  path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
