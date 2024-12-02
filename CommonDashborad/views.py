from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View
# Create your views here.

class home(View):
    
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
class about(View):
    
    template_name='common/about.html'

    def get (self,request,*args, **kwargs):
 
     
        return render(request,self.template_name)
    
    def post(self,request,*args, **kwargs):
        pass

class contact(View):
    
    template_name='common/contact.html'

    def get (self,request,*args, **kwargs):
 
     
        return render(request,self.template_name)
    
    def post(self,request,*args, **kwargs):
        pass
class crewlogin(View):
    
    template_name='common/crewlogin.html'

    def get (self,request,*args, **kwargs):
 
     
        return render(request,self.template_name)
    
    def post(self,request,*args, **kwargs):
        pass
    
class userlogin(View):
    
    template_name='common/userlogin.html'

    def get (self,request,*args, **kwargs):
 
     
        return render(request,self.template_name)
    
    def post(self,request,*args, **kwargs):
        pass
    
class createuser(View):
    
    template_name='common/creteuser.html'

    def get (self,request,*args, **kwargs):
 
     
        return render(request,self.template_name)
    
    def post(self,request,*args, **kwargs):
        pass
    
class userdashborad(View):
    
    template_name='common/userdashborad.html'

    def get (self,request,*args, **kwargs):
 
     
        return render(request,self.template_name)
    
    def post(self,request,*args, **kwargs):
        pass

class userdashborad(View):
    
    template_name='common/user.html'

    def get (self,request,*args, **kwargs):
 
     
        return render(request,self.template_name)
    
    def post(self,request,*args, **kwargs):
        pass
class servicedashborad(View):
    
    template_name='common/servicesprovider.html'

    def get (self,request,*args, **kwargs):
 
     
        return render(request,self.template_name)
    
    def post(self,request,*args, **kwargs):
        pass
    

