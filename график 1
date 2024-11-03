import numpy as np
import matplotlib.pyplot as plt

# Параметры
v0 = 20  # начальная скорость, м/с
g = 9.81  # ускорение свободного падения, м/с^2
angles = [30, 45, 60]  # углы запуска

# Параметрические уравнения траектории
t = np.linspace(0, 2 * v0 * np.sin(np.radians(60)) / g, 500)
plt.figure(figsize=(10, 6))

for alpha in angles:
    x = v0 * np.cos(np.radians(alpha)) * t
    y = v0 * np.sin(np.radians(alpha)) * t - 0.5 * g * t**2
    y = np.maximum(y, 0)  # Ограничиваем значение y, чтобы оно не опускалось ниже нуля
    plt.plot(x, y, label=f'α = {alpha}°')

plt.xlabel("Расстояние x (м)")
plt.ylabel("Высота y (м)")
plt.title("Траектории снаряда без трения (начальная точка высоты = 0)")
plt.legend()
plt.grid()
plt.show()
