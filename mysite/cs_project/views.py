from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

@login_required
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(username=username, password = password1)
            user.save();
            return redirect('/login')
        else:
            messages.info(request, "Password not the same")
            return redirect('register')
        
    else:
        return render(request, 'register.html')
    
#   FIX FOR FLAW 1
#   if request.method == 'POST':
#       username = request.POST['username']
#       password1 = request.POST['password1']
#       password2 = request.POST['password2']

#       if password1 == password2:
#           if len(password1) < 8:
#               messages.info(request, "Password must be at least 8 characters")
#               return redirect('register')
#           elif any(a.isdigit() for a in password1) == False:
#               messages.info(request, "Password must contain a number")
#               return redirect('register')
#           else:
#               user = User.objects.create_user(username=username, password = password1)
#               user.save();
#               return redirect('/login')
#       else:
#           messages.info(request, "Password not the same")
#           return redirect('register')
#   else:
#       return render(request, 'register.html')




