from django.urls import path
from . import views

from django.contrib.auth.views  import LoginView,LogoutView

urlpatterns = [
    
    path('',views.index,name='index'),
 	path('register/',views.register,name='registration'),
 	path('login/',LoginView.as_view(template_name = 'account/login.html'),name ='login'),
 	path('logout/',LogoutView.as_view(template_name = 'account/logout.html'),name ='logout'),
 	path('index/',views.index,name='index'),
 	path('home/',views.home,name='home'),
 	path('contact/',views.contact,name='contact'),

]