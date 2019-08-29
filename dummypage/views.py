import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import QueryDict
# Create your views here.
# pricerun=4.70
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

# def runlogic(request):
def runlogic(request):
	# pass
	# print ("-------Running logic--------views.py dummypage runlogic")
# 	# response="ok"
	# print(request)
	myrequest=dict(request.POST)
# 	# print(mytest)
	runprice=myrequest["data"].pop()
	checkflag=myrequest["revert"].pop()
	# a=dict(request.POST)

	# print(runprice)
# 	postfile=open("stockpost.txt","r+")
	
# 	test= postfile.readlines()

# 	tempwrite=[]	

# 	for line in test:
# 		# print ("each line of line views.py line 38")
# 		mydic=json.loads(line)
# 		# mydic ["status"]="matched(S)"
# 		# print( mydic ["status"])
# 		tempwrite.append(mydic)

# 		if (len(tempwrite)!= 0):
# 			if numberid=='0' and tempwrite[-1]["price"]=="4.72":
# 				tempwrite[-1]["status"]="Pending(S)"  # else False

# 			if numberid=='1' and tempwrite[-1]["price"]=="4.72":
# 				tempwrite[-1]["status"]="Open(O)"  # else False

# 			if numberid=='2' and tempwrite[-1]["price"]=="4.72":
# 				tempwrite[-1]["status"]="Matched(M)"  # else False
	
# 			if numberid=='3' and tempwrite[-1]["price"]!="4.72":
# 				tempwrite[-1]["status"]="Pending(S)"  # else False


# 			if numberid=='4' and tempwrite[-1]["price"]!="4.72":

				
# 				tempwrite[-1]["status"]="Open(O)"  # else False


# 			if numberid=='5' and tempwrite[-1]["price"]=="4.74":


# 				for mystatus in tempwrite:
# 					if mystatus["status"] != "Open(O)" and mystatus["status"]!="Matched(M)" :
# 						mystatus["status"]="Open(O)"
				
# 				tempwrite[-1]["status"]="Matched(M)"  # else False	

# 			# if numberid=='5' and tempwrite[-1]["price"]!="4.72":
# 			# 	tempwrite[-1]["status"]="Matched(M)"  # else False




# 	postfile.truncate(0)
# 	postfile.close()

# 	# open('stockpost.txt', 'w').close()


# 	outfile=open("stockpost.txt",'a')
# 	for i in tempwrite:
# 		# print (postarray[0])
# 		outfile.write(json.dumps(i)+"\n")
# 	outfile.close()
	# print(checkflag)	
	price=float(runprice)
	if checkflag=="up":

		price=round(price+0.02,2)
		if price == 4.82:
			checkflag="down"

	elif checkflag=="down":
		price=round(price-0.02,2)
		if price ==4.52:
			checkflag="up"

	# print(checkturn)

	# response=str(price) #"okokokokokokokok"
	chkpad=str(price).split(".") 

	if len(chkpad[1])==1:
		tempval=chkpad[1]+"0"
		valuelabel=chkpad[0]+"." +tempval

	else:
		valuelabel=str(price)
	# data="test"	
	# # mytest={"result" : result, "data" : data }
	response = json.dumps({"result" : valuelabel, "checkflag" : checkflag })
	# # stocklist="viewtest"	

	# response=json.dumps(stocklist)

	# print(response)
	# response=str(response)
	# print(HttpResponse(valuelabel))

	# response={"valuelabel":valuelabel,"checkflag":checkflag}

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