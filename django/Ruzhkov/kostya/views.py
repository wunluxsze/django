from django.shortcuts import render
from django.http import HttpResponse


def index(request, name, fname):
    return HttpResponse(f'name: {name} <br> fname: {fname}')


def about(request, about):
    return HttpResponse(f'обо мне: {about}')

def contact(request, phone):
    return HttpResponse(f'contacts: {phone}')