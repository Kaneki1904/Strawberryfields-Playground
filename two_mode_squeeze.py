import strawberryfields as sf
from strawberryfields import ops
import numpy as np
import matplotlib.pyplot as plt
from strawberryfields import plot

prog=sf.Program(2)
eng = sf.Engine("fock", backend_options={"cutoff_dim": 8})
with prog.context as q:
    ops.Sgate(1) | q[1]
    ops.Sgate(-1) | q[0]
    ops.BSgate() | (q[0], q[1])
    #ops.S2gate(1.2) | (q[0],q[1])
    ops.MeasureHomodyne(0)| q[0]
    ops.MeasureHomodyne(0) | q[1]
shots=50
x_diff = np.array([])
for i in range(shots):
    result=eng.run(prog)
    x_diff=np.append(x_diff,result.samples[0][0]-result.samples[0][1])
    print(result.samples)
plt.hist(x_diff,bins=5)
plt.show()