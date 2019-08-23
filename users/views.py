from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.

def signupView(request):
        form = UserCreationForm(request.POST or None)
        if(request.method == request.POST):
                if(form.is_valid()):
                        form.save()
                        login(request,form)
                        return redirect('home')
        else:
                return render(request,'users/createUser.html',{'form':form})