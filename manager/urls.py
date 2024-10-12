from django.urls import path
from .views import users_reservations


app_name = 'manager'

urlpatterns = [
    path('users_reservations/', users_reservations, name='users_reservations'),
]