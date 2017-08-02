# coding=utf-8
from django.shortcuts import render

from django.http import HttpResponse
from configFile import *


# Create your views here.
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie


@ensure_csrf_cookie
@csrf_exempt
def api(request):
    if request.method == "POST":
        res = postService(request);
        return HttpResponse(res)
    if request.method == "GET":
        return HttpResponse('we support no GET method!');
def postService(request):
    res = "nothing matched"
    requestBody = request.body
    for para in requestBody.split("&"):
        if keyPara in para:
            requestDic[para] = requestBody
    rbPieceList = requestBody.split("&")
    for rbPiece in rbPieceList:
        methodDic = resList.get(rbPiece,)
        #匹配上了方法，则可以对方法内部的多种具体参数组合再进行匹配
        if methodDic:
            for paraCombString in methodDic.keys():
                flag = 0
                singleParaList = paraCombString.split("&")
                print singleParaList
                for keyParameter in singleParaList:
                    if keyParameter not in requestBody:
                        break;
                    else:
                        flag = flag + 1;
                if singleParaList.__len__() == flag:



                    return methodDic.get(paraCombString)
    return res
@csrf_exempt
def getReq(request):
    print requestDic
    return HttpResponse(requestDic.get(request.body,"null"))