from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View
# Create your views here.

class common(View):
    
    template_name=''

    def get (self,request,*args, **kwargs):
 
     
        return HttpResponse('GET')
    
    def post(self,request,*args, **kwargs):
        pass
