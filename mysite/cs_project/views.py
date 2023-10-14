from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Note

@login_required
def index(request):
    note = Note.objects.filter(owner=request.user)
    notes = [{'text': n.text} for n in note]
    return render(request, 'index.html', {'notes':notes})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(username=username, password = password1)
            user.save()
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

@login_required
def add_note(request):
    text = request.POST['note']
    n = Note(owner=request.user, text=text, user_id=request.user.id)
    n.save()
    return redirect('/')

@login_required
def viewnotes(request):
    if request.method == 'POST':
        query = request.POST['search']
        sql = "SELECT * FROM cs_project_note WHERE user_id='" + str(request.user.id) + "' and text LIKE '%" + query + "%'"
        notes = Note.objects.raw(sql)
        return render(request, 'index.html', {'notes': notes, 'query': query})
    else:
        x = Note.objects.filter(owner=request.user)
        notes = [{'id': n.id, 'text': n.text} for n in x]
        return render(request, 'index.html', {'notes': notes})

#   FIX FOR FLAW 2
#   if request.method == 'POST':
#       query = request.POST['search']
#       notes = Note.objects.filter(owner=request.user, text__contains=query)
#       return render(request, 'index.html', {'notes': notes})

@login_required
def deletenote(request, noteid):
    n = Note.objects.get(pk=noteid)
    n.delete()
    return redirect('/')

#   FIX FOR FLAW 3
#   @login_required
#   def deletenote(request, noteid):
#       n = Note.objects.get(pk=noteid)
#       if request.user == n.owner:
#           n.delete()
#       return redirect('/')

