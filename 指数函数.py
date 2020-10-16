import math 
import numpy as np 
import matplotlib.pyplot as plt 
import mpl_toolkits.axisartist as axisartist 
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

fig=plt.figure(figsize=(6,4)) 
ax=axisartist.Subplot(fig,111) 
fig.add_axes(ax) 

def exponential_func(x, a=2): 
  y=math.pow(a, x)
  return y

X=np.linspace(-4, 4, 40) 
Y=[exponential_func(x) for x in X] 
ax.plot(X, Y) 
plt.show()
