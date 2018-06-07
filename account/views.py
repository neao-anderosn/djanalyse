from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def account_login(request):
    """
    用户登录
    """
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        username = request.POST["account"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # if not request.POST.get('remember_me', None):
            #     request.session.set_expiry(0)
            return redirect("/account/profile")
        else:
            return render(request, "login.html", {'errorMsg': '登录失败，用户名或者密码错误'})


def account_profile(request):
    """
    用户信息
    """
    return render(request, "profile.html")
