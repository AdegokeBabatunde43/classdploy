from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('setting', views.setting, name='setting'),
    path('signout', views.signout, name='signout'),
]