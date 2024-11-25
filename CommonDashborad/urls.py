from django.urls import path,include
from  CommonDashborad import views

urlpatterns = [
    #SECTION - ===========================create account and login =========================================
    path('common/',views.common.as_view(),name='common'),

]