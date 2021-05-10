from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage

from os import listdir
from os.path import isfile, join

# @ get: '/'
# @ description: index.html, saves files to MEDIA_ROOT
def index(request):
    scripts = getScripts("./scripts")
    template = loader.get_template('transformation/index.html')
    form = UploadFileForm()

    context = {
        'scripts': scripts,
        'form': form,
    }

    if (request.method == 'POST'):
        form = UploadFileForm(request.POST, request.FILES)

        fs = FileSystemStorage()

        if (form.is_valid):
            fs.save(request.FILES['f'].name, request.FILES['f'])
            context['excelName'] = request.FILES['f'].name
            return HttpResponse(template.render(context, request), status=200)

    else:
        form = UploadFileForm()
        return HttpResponse(template.render(context, request), status=200)

# Gets files at path
def getScripts(path: str) -> list:
    return [f for f in listdir(path) if isfile(join(path, f))]
