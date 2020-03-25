from neuron import h, gui
from neuron.units import ms, mV

soma = h.Section(name='soma')
soma.nseg = 1
soma.diam = 18.8
soma.L = 18.8
soma.Ra = 123.0
soma.insert('hh')
h.psection()

# stim
iclamp = h.IClamp(soma(0.5))
iclamp.delay = 100
iclamp.dur = 100
iclamp.amp = 0.1

# record
v = h.Vector().record(soma(0.5)._ref_v)             # Membrane potential vector
t = h.Vector().record(h._ref_t)                     # Time stamp vector

# run
h.load_file('stdrun.hoc')
#h.fcurrent()                                       # Make all assigned variables (currents, conductances, etc) consistent with the values of the states. Useful in combination with finitialize().
h.finitialize(-64.97 * mV)
h.continuerun(300 * ms)

# plot
import matplotlib.pyplot as plt
plt.figure()
plt.plot(t, v)
plt.xlabel('t (ms)')
plt.ylabel('v (mV)')
plt.show()

#input("Press Enter to continue...")
