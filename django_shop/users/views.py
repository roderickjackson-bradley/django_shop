from django.shortcuts import render
#from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm                                                         
from django.contrib import messages


def register(request):
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f"Account created for {username}!")
        # return redirect('') Add redirect later
    else:
      form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

  # form = UserCreationForm()
  # return render (request, 'users/register.html', {'form':form})



