from django.shortcuts import render
from django.http import HttpResponse


def echo_get(request):
    """Prints the value of msg key in the URL query parameters"""
    if request.method == "GET":
        try:
            content = "Echo : " + request.GET['msg'] 
            return HttpResponse(content)
        except:
            return HttpResponse("Echo: null")
    else:
        return HttpResponse("No GET Request")


