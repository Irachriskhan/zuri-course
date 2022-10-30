from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. 
# Views are called request handler request - response
# templates are what the user see: webpages

# STEP 1
def sayHello(request):
    return HttpResponse('Hello World')

# step 2 
def greetings(request):
    return render(request, 'index.html')