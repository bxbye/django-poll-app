from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.


def signup(request):
    if request.method == 'POST': # when clicked signup button (post request)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("accounts:login"))
    else: # just open signup page (get request)
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
def profile(request):
    user = request.user
    # print(type(user)) -> output: <class 'django.utils.functional.SimpleLazyObject'>
    return render(request, 'registration/profile.html', {'user': user})