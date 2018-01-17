from django.shortcuts import render
def hello(request):
	text = """<h1>welcome to my app </h1>"""
	return HttpResponse(text)

# Create your views here.
