from django.shortcuts import render, redirect
from .forms import RegisterUserForm

# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect()
    else:
        form = RegisterUserForm()
    context = {'form':form}
    return render(request, 'blog/register.html', context=context)