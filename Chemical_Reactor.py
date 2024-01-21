# Simulation of chamical reactor
# Initial concentration of A: 1.0 mole per liter, B: 0.5 mole per liter and C: 0.0 mole per liter

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

A = [1.0]
B = [0.5]
C = [0.0]

total_time = 100
steps = 500
k1 = k2 = 0.05
t = dt = total_time / steps
time = [t]

figure, axis = plt.subplots()

axis.set_xlim(0, total_time)
axis.set_ylim(0, max(A[-1], B[-1]))

line_A, = axis.plot([], label="A", color="blue")
line_B, = axis.plot([], label="B", color='green')
line_C, = axis.plot([], label="C", color='red')


def animate(x):
    global t, total_time
    if t <= total_time:

        A.append(A[-1] + (k2 * C[-1] - k1 * A[-1] * B[-1]) * dt)
        B.append(B[-1] + (k2 * C[-1] - k1 * A[-1] * B[-1]) * dt)
        C.append(C[-1] + (2 * k1 * A[-1] * B[-1] - 2 * k2 * C[-1]) * dt)
        time.append(t)
        t += dt

    line_A.set_data(time, A)
    line_B.set_data(time, B)
    line_C.set_data(time, C)


animation = FuncAnimation(figure, animate, frames=1, interval=1)

plt.legend()
plt.title("Chemical Reactor")
plt.xlabel("Time (s)")
plt.ylabel("Mole per liter")
plt.show()
