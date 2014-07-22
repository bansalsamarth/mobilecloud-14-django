from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

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

video = []

@method_decorator(csrf_exempt)
def video_handler(request):
    response = HttpResponse(status = 400)

    if request.method == "GET":
        """Display list of videos if GET request"""

        response['content_type'] = "text/plain"
        for i in video:
            response.write(i['name'] + " : " + i['url'] + "||")
        return response

    elif request.method == "POST":
        """3 Parameters expected in POST Request - name, url, duration 
        If all exist and are vaild, video is added to the list"""

        name = request.POST.get('name', 'null')
        url = request.POST.get('url', 'null')
        duration = request.POST.get('duration','null')
        if (name=="null" or url=="null" or duration=="null" or name.replace(" ", "") <1 or url.replace(" ", "")<10 or duration<=0):
            response['status_code'] = 400
            response.write("Missing ['name','duration','url'].")
            return response
        else:
            v = {'name':name, 'url':url, 'duration':duration}
            video.append(v)
            response.write('VIDEO ADDED')
            return response
