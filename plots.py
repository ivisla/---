import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.interpolate import splrep, splev
from matplotlib import image



img = image.imread('minion.jpg')

print(type(img))
print(img.shape)
plt.imshow(img)
plt.show()




lenght1, lenght2, lenght3, lenght4, lenght5, lenght6, lenght7 = [],[],[],[],[],[],[]

name1 = 'C:\\Users\\i.koshevarov\\Documents\\plot_g.txt'
name2 = 'C:\\Users\\i.koshevarov\\Documents\\plot_g1.txt'
name3 = 'C:\\Users\\i.koshevarov\\Documents\\plot_g2.txt'
name4 = 'C:\\Users\\i.koshevarov\\Documents\\plot_g3.txt'
name5 = 'C:\\Users\\i.koshevarov\\Documents\\plot_g4.txt'
namcupc_x = 'C:\\Users\\i.koshevarov\\Documents\\1_CuPc_10.txt'
namcupcPTCDA_y = 'C:\\Users\\i.koshevarov\\Documents\\3_CuPC_PTCDA_10_10.txt'

def plotting(name,lenght):
    with open(name, 'r') as f:
        rows = f.read().splitlines()
    for row in rows:
        elems = row.split('\t')
        lenght.append([float(elems[0]),float(elems[1])])

def convolving (y, win):
    filt = np.ones(win)/win
    mov = win//2
    res = np.convolve(y, filt, mode='same')
    return res




plotting(name1,lenght1)
plotting(name2,lenght2)
plotting(name3,lenght3)
plotting(name4,lenght4)
plotting(name5,lenght5)
plotting(namcupc_x,lenght6)
plotting(namcupcPTCDA_y,lenght7)


x1 = [l[0] for l in lenght1]
y1 = [l[1] for l in lenght1]

x2 = [l[0] for l in lenght2]
y2 = [l[1] for l in lenght2]

x3 = [l[0] for l in lenght3]
y3 = [l[1] for l in lenght3]

x4 = [l[0] for l in lenght4]
y4 = [l[1] for l in lenght4]

x5= [l[0] for l in lenght5]
y5 = [l[1] for l in lenght5]

x6= [l[0] for l in lenght6]
y6 = [l[1] for l in lenght6]

x7= [l[0] for l in lenght7]
y7 = [l[1] for l in lenght7]

y1_conv = convolving(y1,10)
y2_conv = convolving(y2,10)
y3_conv = convolving(y3,10)
y4_conv = convolving(y4,10)
y5_conv = convolving(y5,10)
y6_conv = convolving(y6,10)
y7_conv = convolving(y7,10)


x1_conv = convolving(x1,6)
x2_conv = convolving(x2,6)
x3_conv = convolving(x3,6)
x4_conv = convolving(x4,6)
x5_conv = convolving(x5,6)
x6_conv = convolving(x6,6)
x7_conv = convolving(x7,6)
y6_a= 100-y6_conv
y7_a= 100-y7_conv
'''''
plt.figure()
bspl = splrep(namcupc_x,namcupcPTCDA_y,s=5)
bspl_y = splev(namcupc_x,bspl)
plt.plot(namcupc_x,namcupcPTCDA_y)
plt.plot(namcupc_x,bspl_y)'''
plt.subplot(1,3,1)
plt.plot(x1,y1_conv,'g')
plt.plot(x2,y2_conv,'black')
plt.plot(x3,y3_conv,'white')
plt.plot(x4,y5_conv,'purple')
plt.xlim(350.0,1000.0)
plt.ylim(0.0,1.0)
plt.subplot(1,3,2)
plt.plot(x6,y6_conv,'r')
plt.plot(x7,y7_conv,'y')
plt.xlim(350.0,1000.0)
plt.ylim(0.0,100.0)
plt.subplot(1,3,3)
plt.plot(x6,y6_a,'r')
plt.plot(x7,y7_a,'y')


'''plt.plot(x1,y2,'g')
plt.plot(x2,y3,'r')
plt.plot(x3,y3,'b')
plt.plot(x4,y4,'black')
plt.plot(x5,y5,'white')
plt.plot(x6,y6,'y')
plt.plot(x7,y7,'purple')'''
plt.xlim(350.0,1000.0)
plt.ylim(0.0,100.0)
plt.title('')
plt.show()