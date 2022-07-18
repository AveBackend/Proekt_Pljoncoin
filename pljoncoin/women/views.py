from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .forms import UserRegistrationForm


menu = [{'title': 'Регистрация'}]
def basis(request):
    return render(request, 'women/index.html',)# Основная страница
#def registration(request):
#    return render(request, "women/index1.html")# регистрация

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return redirect("/")
    else:
        user_form = UserRegistrationForm()
    return render(request, 'women/index1.html', {'user_form': user_form})









