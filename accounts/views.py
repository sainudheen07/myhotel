from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:

            auth.login(request, user)
            return redirect('shop:allProdCat')
        else:
            messages.info(request, 'invalid creadentials')

            return redirect('login')

    else:

        return render(request, "login.html")


def register(request):
    if request.method == "POST":

        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email1 = request.POST["email"]
        pswd1 = request.POST["pswd1"]
        pswd2 = request.POST["pswd2"]
        if pswd1 == pswd2:
            # # if User.objects.filter(username=username).exist():
            #     messages.info(request, "username already taken")
            #     return redirect(register)
            # else:

            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email1, password=pswd1,
                                            username=username)
            user.save();
            print("user created")
        elif User.objects.filter(username=username).first():
            messages.error(request, "This username is already taken")
            return redirect('shop:allProdCat')
        else:
            messages.info(request, "password didint mach")
            return redirect(register)
        return redirect('shop:allProdCat')
    else:

        return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('shop:allProdCat')
