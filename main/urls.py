from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('',views.loginhpg,name="login_homepage"),
    path('register/',views.regis,name='register'),
    path('forgot_password/',views.forpw,name='forgot_password'),
    path('forgot_password/2/',views.forpw2,name='forgot_password_2'),
]