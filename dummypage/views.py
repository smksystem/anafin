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

def writedatatofile(writedata):
	print(writedata)
	postfile=open("stockpost.txt",'a')
	postdata=dict(writedata)
	for i in postdata:
		postarray=json.loads(i)
		print (postarray[0])
		postfile.write(json.dumps(postarray[0])+"\n")
	postfile.close()


@csrf_exempt
def runlogic(request):
	print ("-------Running logic--------views.py dummypage runlogic")
	# response="ok"
	# print(request)
	mytest=dict(request.POST)
	# print(mytest)
	numberid=mytest["data"].pop()
	# a=dict(request.POST)

	# print(a)

	postfile=open("stockpost.txt","r+")
	
	test= postfile.readlines()

	tempwrite=[]	

	for line in test:
		# print ("each line of line views.py line 38")
		mydic=json.loads(line)
		# mydic ["status"]="matched(S)"
		# print( mydic ["status"])
		tempwrite.append(mydic)

		if (len(tempwrite)!= 0):
			if numberid=='0' and tempwrite[-1]["price"]=="4.72":

				tempwrite[-1]["status"]="Pending(S)"  # else False
			if numberid=='1' and tempwrite[-1]["price"]=="4.72":
				tempwrite[-1]["status"]="Open(O)"  # else False
			if numberid=='2' and tempwrite[-1]["price"]=="4.72":
				tempwrite[-1]["status"]="Matched(M)"  # else False
	
			if numberid=='3' and tempwrite[-1]["price"]!="4.72":

				tempwrite[-1]["status"]="Pending(S)"  # else False
			if numberid=='4' and tempwrite[-1]["price"]!="4.72":
				tempwrite[-1]["status"]="Open(O)"  # else False

			if numberid=='5' and tempwrite[-1]["price"]=="4.74":
				tempwrite[-1]["status"]="Matched(M)"  # else False	
			# if numberid=='5' and tempwrite[-1]["price"]!="4.72":
			# 	tempwrite[-1]["status"]="Matched(M)"  # else False




	postfile.truncate(0)
	postfile.close()

	# open('stockpost.txt', 'w').close()


	outfile=open("stockpost.txt",'a')
	for i in tempwrite:
		# print (postarray[0])
		outfile.write(json.dumps(i)+"\n")
	outfile.close()



	response=""




	return HttpResponse(response)
@csrf_exempt
def dummyrt(request):

	print("dummyrt")
	gettype=dict(request.GET)
	posttype=""
	for g,v in gettype.items():
		posttype=gettype[g][0]

	if request.method == "POST":
		print(request.POST)
		writedatatofile(request.POST)


		result="okokokokokokokok"
		data="test"	
		mytest={"result" : result, "data" : data }
		response = json.dumps({"result" : result, "data" : data })
		return HttpResponse(response)
	elif request.method == "GET" and posttype == "refresh" :

		with open("stockpost.txt", "r") as ins:
			stocklist = []
			for line in ins:
				stocklist.append(line.rstrip('\n'))
		print (stocklist)
		print(json.dumps(stocklist))
		# response=json.dumps(stocklist)
		# response=json.dumps(stocklist).replace("\\",'')

		response=json.dumps(stocklist)
		
		print (response)

		return HttpResponse(response)
	else:
		context={}
		template="porder.html"
		return render(request,template,context)	