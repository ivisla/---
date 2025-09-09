import numpy as np
import matplotlib.pyplot as plt

# Данные для расчета
distance_au = np.array([0.39, 0.72, 1.00, 1.52, 5.20, 9.54, 19.22, 30.11])
distance_m = distance_au * 1.496e11 # Расстояние в метрах

# Константы
G = 6.674e-11
M = 1.989e30

# Рассчитываем скорость
velocity = np.sqrt(G * M / distance_m)

# Построение графика
plt.plot(distance_au, velocity, 'o-')
plt.xlabel('Расстояние до Солнца (а.е.)')
plt.ylabel('Скорость (м/с)')
plt.title('Зависимость скорости вращения планет от расстояния до Солнца')
plt.show()

# Аппроксимация с помощью метода наименьших квадратов
from scipy.optimize import curve_fit

def hyperbola(x, a, b):
  return a / x + b

popt, pcov = curve_fit(hyperbola, distance_au, velocity)

# Уравнение гиперболы
a = popt[0]
b = popt[1]

# Проверка на погрешность
predicted_velocity = hyperbola(distance_au, a, b)
error = abs(velocity - predicted_velocity)

# Вывод результатов
print('Уравнение гиперболы: v =', a, '/r +', b)
print('Погрешность:')
for i in range(len(distance_au)):
  print(f'Планета {i+1}: {error[i]} м/с')
