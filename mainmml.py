from pinkybot.rangevalue import rangevalue
from pinkybot.tkconsole import outputlog



if __name__=="__main__":
	print("Welcom Main Pinkybot by MML") 

	console=outputlog()
	chooserange=rangevalue("C")
	myrange=chooserange.getRangeSeries()
	


	# work ok for hightlight
	for eachval,data in myrange.items():console.txtout("|"+eachval+" | Vol="+data["vol"] +  
														   " | Order=" +data["order"] + 
														   " | State=" + data["state"]

														)
	
	console.highlight_text("Vol")
	console.highlight_text("Order")
	console.highlight_text("State")
	console.highlight_text("7.05")


	console.Refresher()

	console.mainloop()