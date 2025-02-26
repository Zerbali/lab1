import math as mh
l1=mh.log(3.3,6)-2*(0.6**1/6)**3.3*mh.e**-2
l2=mh.tg(4)*mh.cos(mh.sin(5/4)+mh.sin(5/3))
if l1/l2>5:
    l3=l2+mh.e**3-3*l2*mh.e**2
else:
    l3=l2+3*l2
print(l3)
