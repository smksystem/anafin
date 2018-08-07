# Market Price Level (THB)
# Tick sizes (THB)
# (effective since March 30, 2009)

#A Less than 2	0.01
#B 2 up to less than 5	0.02
#C 5 up to less than 10	0.05
#D 10 up to less than 25	0.10
#E 25 up to less than 100	0.25
#F 100 up to less than 200	0.50
#G 200 up to less than 400	1.00
#H 400 up					2.00
# {"value [range]":,"volumn[100]","order[buy/sel]","status[open,pending,match]",}

# class Node:

#    def __init__(self,data,nextNode=None):
#        self.data = data
#        self.nextNode = nextNode

#    def getData(self):
#        return self.data

#    def setData(self,val):
#        self.data = val

#    def getNextNode(self):
#        return self.nextNode

#    def setNextNode(self,val):
#        self.nextNode = val
from decimal import Decimal
class rangevalue():
	"""docstring for ClassName"""
	def __init__(self,idx):  

		data={
		"A":[0,2,0.01],  # 0 to 2 step 0.01
		"B":[2,4.98,0.02], # 2 up to less than 5	0.02
		"C":[5,10,0.05],
		"D":[10,25,0.10],
		"E":[25,100,0.25],
		"F":[100,200,0.5],
		"G":[200,400,1],
		"H":[400,1000,2],
		}
		series=[]
		i=data[idx][0]
		while i < data[idx][1]:
			series.append(round(i,2))
			i+=data[idx][2]
		# print(series)
		self.rangestock= self.rangeline(series)

	def rangeline(self,series):
		linedic={}
		# print(series)
		for v in series:
			# print(v)
			linedic[str(v)]={"vol":"0","order":"W","state":"W"}
		return linedic
	def getRangeSeries(self):
		return self.rangestock
	def update():
		pass
		
import numpy as np
if __name__=="__main__":

	# c=np.arange(2,5,0.02)
	# print (c)
	test1=rangevalue("A")
	a=test1.getRangeSeries()
	# print(a)
	# print(a["1.86"])
	# test2=rangevalue("B")
	# test3=rangevalue("C")
