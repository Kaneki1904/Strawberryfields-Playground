import strawberryfields as sf
from strawberryfields import ops
from strawberryfields import plot
import numpy as np
import matplotlib.pyplot as plt 

prog=sf.Program(1)
with prog.context as q:
    ops.Dgate(5,np.pi/4)| q
    ops.Sgate(0.7,np.pi/2)| q
eng=sf.Engine("fock", backend_options= {'cutoff_dim': 50})
result = eng.run(prog)
state = result.state
fock_probs = state.all_fock_probs()
n = np.array([i for i in range(50)])
plt.plot(n , fock_probs,'.')
plt.show()