from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from os import listdir
from os.path import isfile, join

# @get: '/'
def index(request):
    scripts = getScripts("./scripts")
    return HttpResponse("Welcome to transformation", status=200)

# Gets files at path
def getScripts(path: str) -> list:
    return [f for f in listdir(path) if isfile(join(path, f))]
