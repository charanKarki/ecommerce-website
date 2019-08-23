from django.urls import path
from .views import signupView
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns=[
    path('login/',LoginView.as_view(template_name='users/login.html',extra_context={'next':'/'}),name='login'),
    path('logout/',LogoutView.as_view(next_page='/'),name='logout'),
    path('signup/',signupView,name='signup')
]