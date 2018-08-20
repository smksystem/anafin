from django.shortcuts import render

# Create your views here.

def dummypage(request):
	print("dummypage")
	context={}
	template="maindummy.html"
	return render(request,template,context)

def dummysuccess(request):
	print("dummypage")
	context={}
	template="dummysuccess.html"
	return render(request,template,context)

def dummyrt(request):
	print("dummypage")
	# print (STATIC_URL)
	context={}
	template="porder.html"
	return render(request,template,context)

