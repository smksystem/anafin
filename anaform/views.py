from django.shortcuts import render
from .forms import RTLoginForm

from anaform.vthread import imonitor


# import threading

# t = threading.Thread(target=long_process,
#                             args=args,
#                             kwargs=kwargs)
# t.setDaemon(True)
# t.start()
# return HttpResponse()

def mainpage(request):

	form=RTLoginForm()
	context={"form":form}

	template="mainpage.html"
	return render(request,template,context)
def home(request):
	
	# print(re
	# request.POST['email']
	myuser=""
	mybrokeId=""
	mypassword=""
	if 'password' in request.POST:
		# print("Username is called !!!!!!!!!!")
		# print(request.POST['username'])
		
		LoginParams={
					"myuser":request.POST['username'],
					"mypassword":request.POST['password'],
					"mybrokeId":request.POST['brokeid'],
					}
		imonitor(LoginParams)
		# login= pinkystart()
		# login.mypinkylogin(myuser,mypassword,mybrokeId)

	form=EmailForm()
	# print(form)

	context={"form":form,"hello":"this is hello"+ myuser ,"brokeid":mybrokeId}
	template="home.html"
	return render(request,template,context)

def login(request):
	form=LoginForm()
	context={"form":form,"hello":"this is hello"+ myuser ,"brokeid":mybrokeId}
	template="home.html"
	return render(request,template,context)	

# Create your views here.
