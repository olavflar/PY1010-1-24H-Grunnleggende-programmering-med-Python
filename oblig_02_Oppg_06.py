# 6: Plotting av funksjonen f(x) = -x^2 - 5

import numpy as np
import matplotlib.pyplot as plt
import math  # Add this line to import the math module

# Definer funksjonen
def f(x):
    return -x**2 - 5

# Generer x-verdier
x = np.linspace(-10, 10, 200)

# Beregn y-verdier
y = f(x)

# Plot funksjonen
plt.plot(x, y, label='f(x) = -x^2 - 5')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot av funksjonen f(x) = -x^2 - 5')
plt.legend()
plt.grid(True)
plt.show()