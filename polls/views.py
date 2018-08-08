from django.http import HttpResponse


def index(requset):
    return HttpResponse("Hello world. U are the polls index.")
