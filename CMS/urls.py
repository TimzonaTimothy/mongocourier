"""CMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import logout, views as auth_views
from django.urls import path, include
from users import views as user_views
from couriermanage import views as courier_views
from django.urls import re_path as url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', courier_views.home, name='home'),
    # path('logout', courier_views.user_logout, name='logout'),
    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    # path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    # path('main/', courier_views.main, name='main'), 
    path('about/', courier_views.about, name='about'),
    path('services/',courier_views.services, name="services"),
    path('track/', courier_views.track, name='track'),
    path('contact/', courier_views.contact, name='contact'),
    path('sea-freight/', courier_views.sea_freight, name='sea-freight'),
    path('air-freight/', courier_views.air_freight, name="air-freight"),
    path('land-freight/', courier_views.land_freight, name="land-freight"),
    path('warehouse/', courier_views.warehouse, name="warehouse"),
    path('custom-clearance/', courier_views.custom_clearance, name='custom-clearance'),
    # path('login/', courier_views.sign_in, name='login'),
    # path('register/', courier_views.register, name='register'),
    path('search/',courier_views.search,name='search'),
    # path('int:id', courier_views.listing, name='detail'),
    url(r'(?P<id>\d+)/$', courier_views.listing, name='detail'),
]
