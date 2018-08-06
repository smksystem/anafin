# Market Price Level (THB)
# Tick sizes (THB)
# (effective since March 30, 2009)
# Less than 2	
# 0.01
# 2 up to less than 5	
# 0.02
# 5 up to less than 10	
# 0.05
# 10 up to less than 25	
# 0.10
# 25 up to less than 100	
# 0.25
# 100 up to less than 200	
# 0.50
# 200 up to less than 400	
# 1.00
# 400 up	
# 2.00

import pandas as pd
import numpy as np
 # there's also can use linspace to include endpoint
a=np.arange(0.00,2.00,0.01)
b=np.arange(2.00,5.00,0.02)
print(b)
if b==2.06:
	print (b)
# pd.between (0,2,inclusive=true)
