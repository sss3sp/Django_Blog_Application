from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def register(request):
    if request.method == 'POST': # To check if the form is filled out with information
        form = UserRegisterForm(request.POST)
        if form.is_valid(): # To check if the filled out form is valid e.g. same user name or password didn't match
            form.save() #save the new user
            username = form.cleaned_data.get('username') # getting the username in cleaned_data dictionary through get() function
            messages.success(request, f'Account created for {username}! You are now able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm() #GET request
    return render(request, 'user_app/register.html', {'form': form}) #{'form': form} is a context

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'user_app/profile.html', context)




# different kinds of django messages
#     message.debug
#     message.info
#     message.success
#     message.warning
#     message.error