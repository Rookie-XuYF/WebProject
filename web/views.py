from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Dashboard
class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        print(request.session)
        greeting = {'title': "Dashboard", 'pageview': "Nazox"}
        return render(request, 'menu/index.html', greeting)


# Dashboard
class TestView(LoginRequiredMixin, View):
    def get(self, request):
        print(request.session)
        greeting = {'title': "Dashboard", 'pageview': "Nazox"}
        return render(request, 'test.html', greeting)


class HomeView(View):
    def get(self, request):
        return redirect('auth-login')
