# Market Price Level (THB)
# Tick sizes (THB)
# (effective since March 30, 2009)

#A Less than 2	0.01
#B 2 up to less than 5	0.02
#C 5 up to less than 10	0.05
#D 10 up to less than 25	0.10
#E 25 up to less than 100	0.25
#G 100 up to less than 200	0.50
#H 200 up to less than 400	1.00
#I 400 up					2.00

# {"value [range]":"order[buy/sel]","status[open,pending,match]","volumn[100]",}

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

class rangevalue():
	"""docstring for ClassName"""
	def __init__(self,index):  

		datatype={
		"A":[0,2,0.01,200],  # 0 to 2 step 0.01
		"B":[2,5,0.02,],
		"C":[5,10,0.05],

		}
		a=[i for i in range(datatype[index][0],datatype[index][1])]
		print (index)
		print (a)
		pass
	
	def update():
		pass
		
import numpy as np
if __name__=="__main__":

	c=np.arange(2,5,0.02)
	print (c)
	test=rangevalue("B")

	print ("hello")