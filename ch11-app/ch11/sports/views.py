from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render


def view_index(req: HttpRequest):
    return HttpResponse(content="django integration")
