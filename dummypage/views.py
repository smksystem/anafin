import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import QueryDict
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

@csrf_exempt
def dummyrt(request):

	print("dummyrt")
	
	mmi=[]
	if request.method == "POST":
		test=dict(request.POST)
		# print(test)
		for i in test:
			# print ("No ="+ i)
			mmi=i.replace('[',"")
			mmi=mmi.replace(']',"")
			mmi=json.loads(mmi)
			print (type(mmi))
			print (mmi["status"])

			# print(i[0])
		
		# print (mmi)
		# for datalist in mmi:
		# for dic,key in mmi.items():
		# 	print (dic)
		# 	print(key)
		# 	# for key in dic:
			# 	print(key)
			# print (y)
			# for x in i:
			# 	print ("my no=" + x)
		# print(request.POST["QueryDict"]["status"])
		# if request.POST.get("points"):
			# points = int(request.POST.get("points"))
			# template = loader.get_template('porder.html')
			# template = 'porder.html'
			# context = {'message': "any message"}
			# return HttpResponse(template.render(context, request))
		result="okokokokokokokok"
		data="test"	
		mytest={"result" : result, "data" : data }
		response = json.dumps({"result" : result, "data" : data })
		return HttpResponse(response)
	else:

		# print (STATIC_URL)
		context={}
		template="porder.html"
		return render(request,template,context)


	