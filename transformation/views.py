from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import default_storage

from .helper import getScripts

# @ get: '/'
# @ description: index.html, saves files to MEDIA_ROOT
def index(request):
    scripts = getScripts("/transformation/scripts")
    template = loader.get_template('transformation/index.html')

    context = {
        'scripts': scripts,
    }

    if (request.method == 'POST'):
        file = request.FILES['file']
        fileName = default_storage.save(file.name, file)
        chosenScript = request.POST.get('scripts')

        # Need to check how to match chosenscript with script in ./scripts

        context['excelName'] = fileName
        
        return HttpResponse(template.render(context, request), status=200)
    else:
        return HttpResponse(template.render(context, request), status=200)
