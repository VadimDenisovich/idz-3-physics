import numpy as np
import matplotlib.pyplot as plt

# Параметры
v0 = 20  # начальная скорость, м/с
g = 9.81  # ускорение свободного падения, м/с^2
k = 0.1  # коэффициент сопротивления, кг/с
m = 1  # масса, кг
dt = 0.01  # шаг времени
t_max = 5  # максимальное время моделирования, с

angles = [30, 45, 60]
plt.figure(figsize=(10, 6))

for alpha in angles:
    vx, vy = v0 * np.cos(np.radians(alpha)), v0 * np.sin(np.radians(alpha))
    x, y = [0], [0]
    t = 0
    while y[-1] >= 0:
        vx -= (k / m) * vx * dt
        vy -= (g + (k / m) * vy) * dt
        x.append(x[-1] + vx * dt)
        y.append(y[-1] + vy * dt)
        t += dt
    plt.plot(x, y, label=f'α = {alpha}°')

plt.xlabel("Расстояние x (м)")
plt.ylabel("Высота y (м)")
plt.title("Траектории снаряда с учётом трения")
plt.legend()
plt.grid()
plt.show()


