
from django.urls import path
from finalproject.views import home , login , logout , test_login

urlpatterns =[
   
    path('login', login),
    path('', home),
    path('test', test_login),
    path('logout', logout)
]