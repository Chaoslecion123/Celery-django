from django.shortcuts import render
import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

def create_user_random(cantidad):
    for i in range(cantidad):
        username = 'username_{}'.format(get_random_string(5,string.ascii_letters))
        email = '{}@test.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username,email=email,password=password)

    return '{} Usuarios creados correctamente'.format(i)
