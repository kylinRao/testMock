from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie


@ensure_csrf_cookie
@csrf_exempt
def mock(request):
    print request.body


    name = request.POST.get('name', 'we support no GET method!');
    print name

    return HttpResponse(name)
