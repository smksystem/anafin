from pinkybot.rangevalue import rangevalue
from pinkybot.tkconsole import outputlog



if __name__=="__main__":
	print("Welcom Main Pinkybot by MML") 
	console=outputlog()
	chooserange=rangevalue("B")
	myrange=chooserange.getRangeSeries()
	# print(myrange)

	for eachval,data in myrange.items():
		# print (eachval)
		# print (data["vol"])
		afilter=eachval.split(".") 
		print (afilter)
		# print (len(afilter[1]))
		# if len(afilter[1])==1: print (eachval)
		console.txtout(eachval+" | vol="+data["vol"])

	


	console.mainloop()