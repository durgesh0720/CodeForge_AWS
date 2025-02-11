from django.urls import path
from . import views

urlpatterns = [
    path('',views.landingPage,name='homepage'),
    path('login/',views.loginPage,name='loginpage'),
    path('signup/',views.signupCoder,name='signuppage'),
    path('loginCoder/',views.loginCoder,name='loginpage'),
    path('welcome/',views.welcomePage,name='welcomepage'),
    path('logout/',views.logoutCoder,name='logoutcoder'),
    path('privacy_policy/',views.privacy_policy),
    path('terms-of-service/',views.terms_of_condition),
]
