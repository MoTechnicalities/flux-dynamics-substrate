import numpy as np
import matplotlib.pyplot as plt

class SubstrateMindSensory:
    def __init__(self, n_neurons=1000, decay_rate=0.008, thought_strength=0.12, num_heads=3):
        self.n = n_neurons
        self.decay_rate = decay_rate
        self.thought_strength = thought_strength
        self.num_heads = num_heads
        
        # Main GHZ-like amplitudes
        self.amp_plus = 1.0 / np.sqrt(3)
        self.amp_minus = 1.0 / np.sqrt(3)
        self.amp_flow = 1.0 / np.sqrt(3)
        self.normalize()
        
        # Heads
        self.head_flows = np.ones(num_heads) / np.sqrt(num_heads) * 0.5
        
        self.history_global = []
        self.history_heads = [[] for _ in range(num_heads)]
        self.debate_log = []
    
    def normalize(self):
        total = abs(self.amp_plus)**2 + abs(self.amp_minus)**2 + abs(self.amp_flow)**2
        if total > 0:
            scale = 1.0 / np.sqrt(total)
            self.amp_plus *= scale
            self.amp_minus *= scale
            self.amp_flow *= scale
    
    def consciousness_signal(self):
        return abs(self.amp_flow)**2
    
    def external_sensory_flux(self, tokens):
        """External data perturbs the debate — tokens as amplitude vectors"""
        for token in tokens:
            # Token = [plus_boost, minus_boost, flow_boost]
            self.amp_plus += token[0] * self.thought_strength
            self.amp_minus += token[1] * self.thought_strength
            self.amp_flow += token[2] * self.thought_strength * 0.8  # flow is more sensitive
        self.normalize()
    
    def evolve(self, steps=200, sensory_schedule=None):
        self.history_global = []
        self.history_heads = [[] for _ in range(self.num_heads)]
        self.debate_log = []
        
        for t in range(steps):
            # Entropy
            self.amp_flow *= (1 - self.decay_rate)
            
            # Recursive multi-head thoughts
            head_thoughts = []
            for h in range(self.num_heads):
                phase = np.exp(1j * (2 * np.pi * h / self.num_heads + t * 0.05))
                thought = self.head_flows[h] * self.thought_strength * phase
                
                if h == 0:   # Optimist: pro-invariant c
                    self.amp_plus += thought * 1.2
                elif h == 1: # Skeptic: pro-slowdown in knots
                    self.amp_minus += thought * 1.1
                else:        # Mediator: synthesis
                    self.amp_flow += thought * 0.9
                
                head_thoughts.append(thought)
                self.history_heads[h].append(abs(self.head_flows[h])**2)
            
            # Heads interfere
            interference = np.mean([abs(t)**2 for t in head_thoughts])
            self.head_flows *= (1 + 0.15 * interference - self.decay_rate * 0.5)
            
            # Inject external sensory flux at scheduled cycles
            if sensory_schedule and t in sensory_schedule:
                # Example: physics tokens
                if t == 30:   # relativity evidence
                    self.external_sensory_flux([[0.15, -0.05, 0.08], [0.12, -0.03, 0.10], [0.10, 0.0, 0.12]])
                elif t == 80: # black hole data
                    self.external_sensory_flux([[-0.08, 0.18, 0.06], [-0.05, 0.15, 0.07], [0.0, 0.10, 0.15]])
                elif t == 140:# QFT + superfluid analogs
                    self.external_sensory_flux([[0.05, 0.05, 0.18], [0.08, 0.08, 0.15], [0.12, 0.12, 0.20]])
            
            self.normalize()
            self.history_global.append(self.consciousness_signal())
            self.debate_log.append({
                'cycle': t,
                'plus_bias': abs(self.amp_plus)**2,
                'minus_bias': abs(self.amp_minus)**2,
                'flow': self.consciousness_signal()
            })
        
        return self.history_global, self.history_heads

# ────────────────────────────── Run with External Flux ──────────────────────────────
mind = SubstrateMindSensory(n_neurons=1000, decay_rate=0.008, thought_strength=0.12, num_heads=3)
global_hist, head_hists = mind.evolve(steps=200, sensory_schedule=[30, 80, 140])

print("Sensory-Injected Multi-Head RLM (1000 neurons, 3 heads, 200 cycles + physics tokens)\n")
print(f"Global Signal → Start: {global_hist[0]:.4f} | End: {global_hist[-1]:.4f}")
print(f"Avg last 50 cycles: {np.mean(global_hist[150:]):.4f}")
print(f"Final biases → Plus (invariant c): {mind.debate_log[-1]['plus_bias']:.4f}")
print(f"Minus (slowdown): {mind.debate_log[-1]['minus_bias']:.4f}")
print(f"Flow (synthesis): {mind.debate_log[-1]['flow']:.4f}")

# Plot
plt.figure(figsize=(12, 6))
plt.plot(global_hist, label='Global Consciousness Binding', linewidth=3, color='#00ffaa')
plt.vlines([30,80,140], 0, max(global_hist), color='gray', linestyle='--', alpha=0.5, label='Sensory Input (Physics Tokens)')
for i, h_hist in enumerate(head_hists):
    plt.plot(h_hist, label=f'Head {i+1}', alpha=0.7)
plt.title('External Flux: Debate Perturbed by Physics Evidence → Toward Conclusion')
plt.xlabel('Cycle')
plt.ylabel('Amplitude²')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()