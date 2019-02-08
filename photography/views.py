from django.shortcuts import render
from allauth.account.views import SignupView, LoginView


class MySignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            pass
        return super(MySignupView, self).dispatch(request, *args, **kwargs)


class MyLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            pass
        return super(MyLoginView, self).dispatch(request, *args, **kwargs)
    template_name = 'login.html'


def home(request):
    return render(request, template_name='index.html')


def gallery(request):
    return render(request, template_name='gallery.html')


def services(request):
    return render(request, template_name='services.html')


def contact(request):
    return render(request, template_name='login.html')


def about(request):
    return render(request, template_name='about.html')
