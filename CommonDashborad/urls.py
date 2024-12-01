from django.urls import path,include
from  CommonDashborad import views
urlpatterns = [
    #SECTION - ===========================create account and login =========================================
    path('',views.common.as_view(),name='common'),
    path('User-login/',views.Userlogin.as_view(),name='Userlogin'),
]