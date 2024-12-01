from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View
# Create your views here.

class common(View):
    
    template_name='common/home.html'

    def get (self,request,*args, **kwargs):
 
     
        return render(request,self.template_name)
    
    def post(self,request,*args, **kwargs):
        pass
class Userlogin(View):
    
    template_name='common/userlogin.html'

    def get (self,request,*args, **kwargs):
 
     
        return render(request,self.template_name)
    
    def post(self,request,*args, **kwargs):
        pass
