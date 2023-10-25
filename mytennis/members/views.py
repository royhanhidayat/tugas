#views memebers
from django.shortcuts import render
from django.http  import HttpResponse
from django.template import loader

def myfist(request):
    template = loader.get_template('myfist.html')
    return HttpResponse (template.render())


def cicak(request):
    template = loader.get_template('cicak.html')
    return HttpResponse (template.render())