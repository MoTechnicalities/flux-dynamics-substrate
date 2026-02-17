import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm

class SubstrateMindSensory:
    def __init__(self, n_neurons=1000, decay_rate=0.008, thought_strength=0.12, num_heads=3):
        self.n = n_neurons
        self.decay_rate = decay_rate
        self.thought_strength = thought_strength
        self.num_heads = num_heads
        
        # Main GHZ-like amplitudes (Complex for phase space)
        self.amp_plus = (1.0 / np.sqrt(3)) + 0j
        self.amp_minus = (1.0 / np.sqrt(3)) + 0j
        self.amp_flow = (1.0 / np.sqrt(3)) + 0j
        self.normalize()
        
        # Heads
        self.head_flows = np.ones(num_heads) / np.sqrt(num_heads) * 0.5
        
        # Trajectory history for visualization
        self.trajectory_plus = []
        self.trajectory_minus = []
        self.trajectory_flow = []
    
    def normalize(self):
        total = abs(self.amp_plus)**2 + abs(self.amp_minus)**2 + abs(self.amp_flow)**2
        if total > 0:
            scale = 1.0 / np.sqrt(total)
            self.amp_plus *= scale
            self.amp_minus *= scale
            self.amp_flow *= scale
    
    def external_sensory_flux(self, tokens):
        for token in tokens:
            self.amp_plus += token[0] * self.thought_strength
            self.amp_minus += token[1] * self.thought_strength
            self.amp_flow += token[2] * self.thought_strength * 0.8
        self.normalize()
    
    def step(self, t, sensory_schedule=None):
        # Entropy
        self.amp_flow *= (1 - self.decay_rate)
        
        # Recursive multi-head thoughts
        head_thoughts = []
        for h in range(self.num_heads):
            # Phase rotation creates the "orbit"
            phase = np.exp(1j * (2 * np.pi * h / self.num_heads + t * 0.05))
            thought = self.head_flows[h] * self.thought_strength * phase
            
            if h == 0:   # Optimist (Invariant c)
                self.amp_plus += thought * 1.2
            elif h == 1: # Skeptic (Slowdown)
                self.amp_minus += thought * 1.1
            else:        # Mediator (Synthesis/Flow)
                self.amp_flow += thought * 0.9
            
            head_thoughts.append(thought)
        
        # Heads interfere
        interference = np.mean([abs(t)**2 for t in head_thoughts])
        self.head_flows *= (1 + 0.15 * interference - self.decay_rate * 0.5)
        
        # Inject external sensory flux
        if sensory_schedule:
             # Physics Tokens Schedule
            if t == 30:   # relativity evidence (Plus Boost)
                self.external_sensory_flux([[0.15, -0.05, 0.08], [0.12, -0.03, 0.10], [0.10, 0.0, 0.12]])
            elif t == 80: # black hole data (Minus Boost)
                self.external_sensory_flux([[-0.08, 0.18, 0.06], [-0.05, 0.15, 0.07], [0.0, 0.10, 0.15]])
            elif t == 140:# QFT + superfluid (Synthesis Boost)
                self.external_sensory_flux([[0.05, 0.05, 0.18], [0.08, 0.08, 0.15], [0.12, 0.12, 0.20]])
        
        self.normalize()
        
        # Record complex state
        self.trajectory_plus.append(self.amp_plus)
        self.trajectory_minus.append(self.amp_minus)
        self.trajectory_flow.append(self.amp_flow)
        
        return abs(self.amp_flow)**2 # Return "Consciousness Signal" level

# Setup Simulation
mind = SubstrateMindSensory()
steps = 300
times = range(steps)
c_signals = []

# Run simulation
print("Calculating Phase Space Trajectories...")
for t in times:
    sig = mind.step(t, sensory_schedule=True)
    c_signals.append(sig)

# Arrays for plotting
traj_p = np.array(mind.trajectory_plus)
traj_m = np.array(mind.trajectory_minus)
traj_f = np.array(mind.trajectory_flow)

# ─── VISUALIZATION ────────────────────────────────────────────────────────────

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111)
plt.subplots_adjust(bottom=0.2) 

# Plot the "Phase Space" (Real vs Imaginary parts of the amplitudes)
# This reveals the "Orbit" of the thoughts
ax.set_facecolor('#050510')
ax.grid(color='white', alpha=0.1)

# Plot "Plus" (Invariant C) - Green
plt.plot(traj_p.real, traj_p.imag, color='#00ffaa', alpha=0.6, linewidth=1.5, label='Theory: Invariant C (Plus)')
# Plot "Minus" (Slowdown) - Red
plt.plot(traj_m.real, traj_m.imag, color='#ff4444', alpha=0.4, linewidth=1.5, label='Theory: Slowdown (Minus)')
# Plot "Flow" (Synthesis) - Blue/Cyan Glow
plt.plot(traj_f.real, traj_f.imag, color='#44aaff', alpha=0.9, linewidth=3, label='Synthesis: Flow (Vacuum)')

# Add start/end markers
plt.scatter([traj_f.real[0]], [traj_f.imag[0]], color='white', s=50, label='Start')
plt.scatter([traj_f.real[-1]], [traj_f.imag[-1]], color='#44aaff', s=100, edgecolors='white', label='Current State')

# Annotations for Events
def add_event_marker(cycle_idx, text):
    if cycle_idx < len(traj_f):
        plt.text(traj_f.real[cycle_idx], traj_f.imag[cycle_idx], f"  {text}", color='white', fontsize=9, fontweight='bold')
        plt.scatter([traj_f.real[cycle_idx]], [traj_f.imag[cycle_idx]], color='yellow', s=60, zorder=10)

add_event_marker(30, "Evt: Relativity")
add_event_marker(80, "Evt: Black Hole")
add_event_marker(140, "Evt: Superfluid")

ax.set_title("The Shape of Thought: Phase Space of the Flux Debate", color='white', fontsize=14)
ax.set_xlabel("Real Amplitude Part", color='gray')
ax.set_ylabel("Imaginary Amplitude Part", color='gray')
ax.tick_params(colors='gray')
for spine in ax.spines.values():
    spine.set_edgecolor('gray')

plt.legend(loc='upper right', facecolor='#111122', edgecolor='gray', labelcolor='white')

text_desc = (
    "INTERPRETATION:\n"
    "The spiral represents the system 'thinking'.\n"
    "Widening orbits indicate increasing energy/confidence in a synthesis.\n"
    "Collapsing orbits would indicate dogmatic stagnation.\n"
    "Notice how the 'Flow' (Blue) trajectory is perturbed by events but maintains a coherent orbital structure."
)
plt.figtext(0.5, 0.05, text_desc, ha="center", fontsize=10, bbox={"facecolor":"#111122", "alpha":0.8, "pad":5}, color="#cccccc")

print("Visualization generated. Displaying...")
plt.show()
