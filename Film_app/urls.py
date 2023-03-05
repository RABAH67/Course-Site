from django.urls import path
from .views import home ,detail ,homme ,signup,profile,profile_edit
from Film_app import views





urlpatterns = [
    
    path('',views.homme,name='home'),
    path('course/',views.home,name='course'),
    path('course/detail/<int:myid>',views.detail,name='detail'),
    path('apell_nous/',views.apell_nous,name='apell_nous'),
    path('plus_info/',views.plus_info,name='plus_info'),
    path('offre/',views.ofre,name='ofre'),
    path('course/command/',views.command,name='command'),
    path('course/command/confirmation/',views.confarmation,name='confarmation'),
    path('singup/',views.signup,name='singup'),
    path('accounts/profile/',views.profile,name='profile'),
    path('profile_edit/',views.profile_edit,name='profile_edit'),

]
