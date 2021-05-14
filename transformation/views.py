from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import default_storage

from .helper import getScripts, process

# @ get: '/'
# @ description: index.html, saves files to MEDIA_ROOT
def index(request):
    scripts = getScripts("transformation/scripts")
    template = loader.get_template('transformation/index.html')

    context = {
        'scripts': scripts,
    }

    if (request.method == 'POST'):
        file = request.FILES['file']
        fileName = default_storage.save(file.name, file)
        chosenScript = request.POST.get('scripts')

        # Need to check this logic -> tempatles/index.html
        if process(fileName, chosenScript):
            context['excelName'] = fileName
            context['success'] = True
        else:
            context['excelName'] = fileName
            context['success'] = True
        
        return HttpResponse(template.render(context, request), status=200)
    else:
        return HttpResponse(template.render(context, request), status=200)
