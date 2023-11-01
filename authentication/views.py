from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth

from authentication.forms import UserLoginForm


# Create your views here.
# Login
class LoginView(View):
    username = []

    def get(self, request):
        if 'username' in request.session:
            return redirect('dashboard')
        else:
            greeting = {'form': UserLoginForm}
            return render(request, 'pages/authentication/auth-login.html', greeting)

    def post(self, request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username)

            if username != '' and password != '':
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    request.session['username'] = username
                    auth.login(request, user)
                    request.session.set_expiry(100)
                    LoginView.username.append(username)
                    data = {'success_message': 'Successfully login'}
                    return JsonResponse(data, safe=False)
                else:
                    data = {'error_message': 'Invalid Credentials'}
                    return JsonResponse(data, safe=False)
            else:
                data = {'error_message': 'Some field is empty'}
                return JsonResponse(data, safe=False)
        else:
            return redirect('auth-login')
