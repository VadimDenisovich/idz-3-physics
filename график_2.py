import numpy as np
import matplotlib.pyplot as plt

# Параметры
v0 = 20  # начальная скорость, м/с
g = 9.81  # ускорение свободного падения, м/с^2
angles = np.linspace(0, 90, 100)
H_max = (v0**2 * np.sin(np.radians(angles))**2) / (2 * g)

plt.figure(figsize=(10, 6))
plt.plot(angles, H_max)
plt.xlabel("Угол α (°)")
plt.ylabel("Максимальная высота H (м)")
plt.title("Зависимость максимальной высоты от угла запуска")
plt.grid()
plt.show()
