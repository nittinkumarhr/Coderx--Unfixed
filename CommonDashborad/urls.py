from django.urls import path,include
from  CommonDashborad import views
urlpatterns = [
    #SECTION - ===========================create account and login =========================================
    path('',views.home.as_view(),name='home'),
    path('User-login/',views.Userlogin.as_view(),name='Userlogin'),
    path('about/',views.about.as_view(),name='about'),
    path('contact/',views.contact.as_view(),name='contact'),
      path('crew-login/',views.crewlogin.as_view(),name='crewlogin'),
    path('user-login/',views.userlogin.as_view(),name='userlogin'),
    path('user-crate/',views.createuser.as_view(),name='createuser'),
    path('user-dashborad/',views.userdashborad.as_view(),name='userdashborad'),
    path('use-dashboard/',views.userdashborad.as_view(),name='user'),
    path('service-dashborad/',views.servicedashborad.as_view(),name='servicedashborad'),
    # path('service/',views.service.as_view(),name='home'),
]