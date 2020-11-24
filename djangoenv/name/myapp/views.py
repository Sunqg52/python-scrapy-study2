from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
test = "hello word!"

def index(request):
	return render(request, 'hello.html', {'test': test})
