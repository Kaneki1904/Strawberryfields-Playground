import strawberryfields as sf
import numpy as np
from strawberryfields import ops
from strawberryfields import plot  
         


prog = sf.Program(1)

with prog.context as q:
    ops.Fock(3)|q
eng = sf.Engine("fock", backend_options = {"cutoff_dim": 20})
result = eng.run(prog)

state = result.state
print(state.mean_photon(0))
plot.plot_wigner(state,0, np.linspace(-8,8,500),np.linspace(-8,8,500))

