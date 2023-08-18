from django.contrib import admin
from django.urls import path, include
from challan_app import views

urlpatterns = [
    path("", views.index, name='home'),
     path("adminlogin", views.adminlogin, name='login'),
    path("policelogin", views.policelogin, name='login'),
    path("index", views.index, name='index'),
    path("contact",views.contact,name="contact"),
    path("admin",views.admin,name="admin"),
    path("police",views.police,name="police"),
    path("challan_form",views.challan_form,name="challan_form"),
    path("pay_challan", views.pay_challan, name='pay_challan'),
    path("createchallan", views.createchallan, name='createchallan'),
    path("createpolice", views.createpolice, name='createpolice'),
    path("createuser", views.createuser, name='createuser'),
    path("police_list", views.police_list, name='police_list'),
    path("user_list", views.user_list, name='user_list'), 
    path("logout", views.logout_request, name= "logout"),
]
