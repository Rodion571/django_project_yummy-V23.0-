from django.http import HttpResponse
from django.shortcuts import render
from home.models import Reservation
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name='manager').exists() or user.is_staff


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def users_reservations(request):
    return HttpResponse('Manager Page')