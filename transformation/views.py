from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import default_storage
from django.utils.encoding import smart_str

from .helper import getScripts, process

basePath = '/home/transformation/'

# @ get: '/'
# @ description: index.html, saves files to MEDIA_ROOT
def index(request):
    scripts = getScripts(basePath + "transformation/scripts")
    template = loader.get_template("transformation/index.html")

    context = {
        'scripts': scripts,
    }

    # Processes the file uploaded
    if (request.method == 'POST'):
        file = request.FILES['file']
        fileName = default_storage.save(file.name, file)
        chosenScript = request.POST.get('scripts')

        # Need to check this logic -> templates/index.html
        if process(fileName, chosenScript, basePath):
            context['excelName'] = fileName
            context['success'] = True

            with open(basePath + 'generatedFiles/' + fileName, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = 'inline; filename=' + fileName
                return response

        else:
            context['excelName'] = fileName
            context['success'] = False
        
        return HttpResponse(template.render(context, request), status=200)
    else:
        return HttpResponse(template.render(context, request), status=200)
