from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed

# Create your views here.
def hello_world_view(request):
    return HttpResponse('Hello World!')

def hello_python_view(request):
    return HttpResponse('Hello Python')

def hello_html_view(request):
    return render(request, 'todos/hello.html')

def hello_path(request, name):
    return HttpResponse(f'Hello {name}!')

def hello_query(request):
    return HttpResponse(f'Your query was {request.GET.get("q")}')

def special_view(request):
    # do stuff
    return redirect('hello_html')

def post_example(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    name =  request.POST.get('name')
    age =  request.POST.get('age')
    job =  request.POST.get('job')

    return HttpResponse(f'You posted: {name}, {age}, {job}')

def submit_example(request):
    return render(request, 'todos/submit.html')