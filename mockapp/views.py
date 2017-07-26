from django.shortcuts import render

from django.http import HttpResponse
from configFile import *


# Create your views here.
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie


@ensure_csrf_cookie
@csrf_exempt
def mock(request):
    if request.method == "POST":
        res = postService(request);
        return HttpResponse(res)
    if request.method == "GET":
        return HttpResponse('we support no GET method!');
def postService(request):
    res = "nothing matched"
    for key in dic.keys():
        flag = 0
        keyPieceList = key.split("&")
        for keyPiece in keyPieceList:
            if keyPiece not in request.body:
                break;
            else:
                flag = flag + 1;
        if flag == keyPieceList.__len__():
            return dic[key]
    return res
