from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # The login function is only needed if you are not using the allauth library
    # and/or if you would like to create your own login page - we are using the
    # home page as our login page, so we do not need this function
    # path('login', views.login_user, name='login'),

    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('record/<int:user_id>', views.customer_record, name='record'),
]