from django.shortcuts import render, redirect
from . forms import CreateUserForm


def homepage(request):
    return render(request, "users/index.html")

def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("")

    context = {"registerform": form}
    return render(request, "users/register.html", context=context)
