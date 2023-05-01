
#a step bar shown in the figure is subjected to a axially applied load of 35 kN.
#Find the maximum and minimum stress produced
import math
#lmfao
d1=int(input("enter dimension  1: "))
d2=int(input("enter dimension 2: "))
print("area1 is ",math.pi*math.pow(d1,2)/4,"mm",'\n',"area 2 is ",math.pi*math.pow(d2,2)/4,"mm")
print("max stress is ",(35*math.pow(10,3))/(math.pi*math.pow(d1,2)/4),'\n',"min stress is ",(35*math.pow(10,3))/(math.pi*math.pow(d2,2)/4))
