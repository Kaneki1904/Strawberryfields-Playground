import strawberryfields as sf
from strawberryfields import ops
from strawberryfields import plot
import numpy as np
import matplotlib.pyplot as plt

prog = sf.Program(1)

with prog.context as q:
    ops.Dgate(2, np.pi/4) | q
    ops.Sgate(1.1, np.pi/2) | q
eng=sf.Engine("fock", backend_options = {"cutoff_dim": 20})
result=eng.run(prog)
state = result.state
electric_vals = np.array([])
electric_uncert=np.array([])
phis = np.linspace(0,4*np.pi,200)
for i in phis:
    meas = state.quad_expectation(0,i)
    electric_vals = np.append(electric_vals, meas[0])
    electric_uncert = np.append(electric_uncert, meas[1]**0.5)
plt.errorbar(phis, electric_vals, electric_uncert)
plt.show()
print(electric_vals)