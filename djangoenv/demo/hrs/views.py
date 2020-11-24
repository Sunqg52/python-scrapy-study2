from django.shortcuts import render
from io import StringIO
from  django.http import HttpResponse

# Create your views here.
depts_list = [
	{'no':10, 'name':'孙全刚','age':21,'location':'承德'},
	{'no':30, 'name':'孙全威','age':11,'location':'承德'}
]

def index(request):
	return render(request, 'index.html', {'depts_list': depts_list})