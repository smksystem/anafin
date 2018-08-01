from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def index(request):

    context = {}
    template = loader.get_template('app/index.html')
    print ( "this is index")
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    # print ( "this is gent_html")
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))