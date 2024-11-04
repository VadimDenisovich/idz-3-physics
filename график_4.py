import numpy as np
import matplotlib.pyplot as plt

# Параметры
v0 = 20  # начальная скорость, м/с
g = 9.81  # ускорение свободного падения, м/с^2
k = 0.1  # коэффициент сопротивления, кг/с
m = 1  # масса, кг
dt = 0.01  # шаг времени
t_max = 5  # максимальное время моделирования, с
t = np.linspace(0, 2 * v0 * np.sin(np.radians(60)) / g, 500)  # время, с
# Углы для построения траекторий
angles = np.linspace(10, 80, 8)
plt.figure(figsize=(10, 6))

# Построение траекторий и огибающей
for alpha in angles:
    x = v0 * np.cos(np.radians(alpha)) * t
    y = v0 * np.sin(np.radians(alpha)) * t - 0.5 * g * t**2
    y = np.maximum(y, 0)  # Ограничиваем значение y, чтобы оно не опускалось ниже нуля
    plt.plot(x, y, alpha=0.5)

# Огибающая
x_envelope = np.linspace(0, (v0**2) / g, 100)
y_envelope = (v0**2) / (2 * g) - (g * x_envelope**2) / (2 * v0**2)
y_envelope = np.maximum(y_envelope, 0)  # Ограничиваем огибающую тоже

plt.plot(x_envelope, y_envelope, 'k--', label='Огибающая')
plt.xlabel("Расстояние x (м)")
plt.ylabel("Высота y (м)")
plt.title("Огибающая траекторий (начальная точка высоты = 0)")
plt.legend()
plt.grid()
plt.show()
