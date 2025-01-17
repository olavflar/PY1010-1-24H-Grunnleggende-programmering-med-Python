# 3: Fra grader til radianer
import numpy as np

v_grad = float(input("Skriv inn gradtallet: "))
v_rad = v_grad * np.pi / 180

print(f"{v_grad} grader tilsvarer {v_rad:.4f} radianer.")
