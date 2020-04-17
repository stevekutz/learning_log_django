from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """ Regsiter a new user if GET request made """
    if request.method != 'POST' and request.method == 'GET':
        # present user a registration form with no data
        form = UserCreationForm()
    else:     
        # process a completed form with POST data
        form = UserCreationForm(data = request.POST)

        if form.is_valid:
            new_user = form.save()
            # Log in user and the redirect to home page

            login(request, new_user)
            return redirect('learning_logs:index')

    # Display blank of invalid form
    context = { 'form': form }        
    return render(request, 'registration/register.html', context)
