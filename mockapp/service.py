import request as request
from django.http import HttpResponse
from django.shortcuts import render


def mock(request):
    # name = request.REQUEST.get('name', 'xxx');
    return HttpResponse('nihao')