import json
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
import matplotlib
from scipy import cluster
with open("testovaci_data.json", "r") as f:
   dict= json.load(f)
#konvoluci si predstavit jakoze druhy seznam (sonda) je otoceny a postupne nasobi ten prvni

#vypsal jsem si do seznamu "klice" klice ve slovniku a pak na ne odkazuji ne slovem ale cislem
klice=list(dict.keys())
#zkusebni data na porozumneni
fakedata=[2,2,3,4,5,6]
fakesonda=[1,2,3]
sonda=dict[klice[0]]
skut=dict[klice[1]]
namer=dict[klice[2]]
namer_sum=dict[klice[3]]
nastrel=[1,1,1,1,1,1]
konvoluce=list(np.convolve(fakesonda,fakedata,"same"))

plt.plot(skut,marker="o",mfc="black")
#plt.show()
print(namer)
print(skut)
#zkouska nástřelu, jenze jaka optimalizacni funkce?
nastrel=[1,1,1,1,1,1]
test1=list(np.convolve(fakesonda,nastrel))
print(test1)


neco=scipy.signal.deconvolve(namer,sonda)
print(neco)

# print(json.dumps(dict,indent=4,sort_keys=True))