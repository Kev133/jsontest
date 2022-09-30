import json
import matplotlib.pyplot as plt
import numpy as np
from numpy import array
import scipy.signal
import scipy.optimize
import matplotlib
from scipy import cluster
with open("testovaci_data.json", "r") as f:
   dict= json.load(f)
#konvoluci si predstavit jakoze druhy seznam (sonda) je otoceny a postupne nasobi ten prvni

#vypsal jsem si do seznamu "klice" klice ve slovniku a pak na ne odkazuji ne slovem ale cislem
klice=list(dict.keys())
#zkusebni data na porozumneni
#fakedata=[2,2,3,4,5,6]
#fakesonda=[1,2,3]
sonda=array(dict[klice[0]])
skut=dict[klice[1]]
namer=dict[klice[2]]
namer_sum=array(dict[klice[3]])
konvoluce=list(np.convolve(sonda,namer_sum,"same"))
print(len(konvoluce))
x0=array(len(namer_sum)*[1])
print(konvoluce)
plt.plot(skut,marker="o",mfc="black")
#plt.show()
def to_opt(x):
   return array(np.convolve(x,sonda,"same"))-array(namer_sum)
print(namer_sum)
print(skut)
heh=scipy.optimize.leastsq(to_opt,x0)
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
print(heh)



# print(json.dumps(dict,indent=4,sort_keys=True))