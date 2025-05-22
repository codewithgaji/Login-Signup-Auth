from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomUserCreationForm
# Create your views here.



@login_required
def home(request):
  return render(request, "home.html", {})

def signup_view(request):
  if request.method == "POST":
    form = CustomUserCreationForm(request.POST) # This is used to save a new user
    if form.is_valid():
      user = form.save()
      login(request, user)
      # Thanks to the crazy mapping of urls in the Main urls I have to map every url to its app
      return redirect("baseapp:home") # This is used to redirect the page to homepage after they sign up                                                                                                                                                                                     
  else:
   form = CustomUserCreationForm()

  context = {
    "form_key" : form
  }

  return render(request, "registration/signup.html", context)