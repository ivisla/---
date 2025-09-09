#import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x**2
#print(x)
#print(y)

plt.subplot(1,2,1)
plt.plot(x,y,'r--')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Y = X**2')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-11111111,11111111,10000)
y = x**2
'''a = list(range(0,10,1))
print(a)
b = []
for in range ()'''
#print(x)
#print(y)

plt.plot(x,y,'r')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('')
plt.show()
