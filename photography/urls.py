from django.conf.urls import url
from . import views


app_name = 'photography'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^gallery/', views.gallery, name='gallery'),
    url(r'^services/', views.services, name='services'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^about/', views.about, name='about'),

    # allauth login and signup override
    url(r'^accounts/login/$', views.MyLoginView.as_view(), name='login'),
    url(r'^accounts/signup/$', views.MySignupView.as_view(), name='signup'),
]