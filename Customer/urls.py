from django.urls import path,include
from  Customer import views

urlpatterns = [
      path('customer/',views.customer.as_view(),name='common'),
    


]