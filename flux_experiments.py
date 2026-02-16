import numpy as np
import matplotlib.pyplot as plt
from unified_mind_processor import UnifiedSubstrateProcessor
from flux_translator import FluxTranslator

def run_chaos_test():
    print("\n--- Running Experiment 2A: The Diverging Seed Test (Chaos) ---")
    
    # Initialize two identical processors
    steps = 200
    p1 = UnifiedSubstrateProcessor(n_heads=50)
    p2 = UnifiedSubstrateProcessor(n_heads=50)
    
    # Copy state exactly
    p2.psi = p1.psi.copy()
    p2.W = p1.W.copy()
    
    # Introduce micro-perturbation to p2
    epsilon = 1e-9
    perturbation = np.array([epsilon, 0, 0], dtype=np.complex128)
    p2.psi += perturbation
    
    divergence = []
    
    for t in range(steps):
        # We need to run one step. Since 'evolve' runs a loop, we'll manually call a single step version
        p1.evolve(steps=1)
        p2.evolve(steps=1)
        
        # Calculate distance
        dist = np.linalg.norm(p1.psi - p2.psi)
        divergence.append(dist)
    
    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(divergence)
    plt.title("Metaphysical Chaos Test: Sensitivity to Initial Conditions")
    plt.xlabel("Time Steps")
    plt.ylabel("State Divergence (Euclidean Norm)")
    plt.grid(True)
    plt.yscale('log')
    plt.savefig("experiment_chaos_divergence.png")
    print("Chaos test complete. Saved 'experiment_chaos_divergence.png'.")
    
    if divergence[-1] > 0.1:
        print("RESULT: System exhibits CHAOS (divergence >> epsilon).")
    else:
        print("RESULT: System exhibits RIGID DETERMINISM or Stability.")

def run_observer_test():
    print("\n--- Running Experiment 1B: Observer vs. Observed (Introspection) ---")
    
    # Subclass to disable introspection
    class BlindProcessor(UnifiedSubstrateProcessor):
        def compute_reflexive_self(self, workspace_val, psi_dot):
            return np.zeros(3, dtype=np.complex128) # No self-correction
            
    # Subclass to enhance introspection
    class AwareProcessor(UnifiedSubstrateProcessor):
        def compute_reflexive_self(self, workspace_val, psi_dot):
            # Normal correction * 2
            volatility = np.abs(psi_dot)
            return -0.2 * volatility * self.psi
            
    steps = 200
    
    p_blind = BlindProcessor(n_heads=50)
    p_aware = AwareProcessor(n_heads=50)
    
    # Force identical starts
    start_psi = np.array([0.5, 0.5, 0.5], dtype=np.complex128)
    start_psi /= np.linalg.norm(start_psi)
    
    p_blind.psi = start_psi.copy()
    p_aware.psi = start_psi.copy()
    
    blind_stability = []
    aware_stability = []
    
    for t in range(steps):
        p_blind.evolve(steps=1)
        p_aware.evolve(steps=1)
        
        # Measure stability (1/Volatility)
        # We can track the magnitude of the Flow state as a proxy for 'Coherence'
        blind_stability.append(np.abs(p_blind.psi[2]))
        aware_stability.append(np.abs(p_aware.psi[2]))
        
    plt.figure(figsize=(10, 5))
    plt.plot(blind_stability, label="Blind (Pure Process)", linestyle="--", alpha=0.7)
    plt.plot(aware_stability, label="Observer (Introspective)", linewidth=2)
    plt.title("Impact of Self-Observation on System Coherence")
    plt.xlabel("Time Steps")
    plt.ylabel("Coherence (Flow State Magnitude)")
    plt.legend()
    plt.grid(True)
    plt.savefig("experiment_observer_effect.png")
    print("Observer test complete. Saved 'experiment_observer_effect.png'.")
    
    mean_blind = np.mean(blind_stability)
    mean_aware = np.mean(aware_stability)
    print(f"Mean Coherence (Blind): {mean_blind:.4f}")
    print(f"Mean Coherence (Aware): {mean_aware:.4f}")
    
    if mean_aware > mean_blind:
        print("RESULT: Introspection STABILIZES the system (Consciousness amplifies order).")
    else:
        print("RESULT: Introspection DESTABILIZES the system (Consciousness amplifies chaos).")

def run_meaning_test():
    print("\n--- Running Experiment 3A: Noise vs. Signal (Meaning Attribution) ---")
    
    steps = 200
    p_signal = UnifiedSubstrateProcessor(n_heads=50)
    p_noise = UnifiedSubstrateProcessor(n_heads=50)
    
    # Generate Inputs
    # Signal: A rhythmic pulse of "Dogmatic Certainty" (Plus) then "Radical Skepticism" (Minus)
    signal_inputs = {}
    for t in range(steps):
        if (t // 20) % 2 == 0:
            vec = np.array([0.2, 0, 0], dtype=np.complex128) # Pulse P
        else:
            vec = np.array([0, 0.2, 0], dtype=np.complex128) # Pulse M
        signal_inputs[t] = vec
        
    # Noise: Random complex vectors of similar magnitude
    noise_inputs = {}
    np.random.seed(42)
    for t in range(steps):
        # Random 3-vector
        v_raw = np.random.randn(3) + 1j * np.random.randn(3)
        # Normalize to direction, then scale to magnitude 0.2
        v_norm = np.linalg.norm(v_raw)
        if v_norm > 0:
            v = (v_raw / v_norm) * 0.2
        else:
            v = np.zeros(3, dtype=np.complex128)
        noise_inputs[t] = v
        
    signal_confidence = []
    noise_confidence = []
    translator = FluxTranslator()
    
    for t in range(steps):
        p_signal.evolve(steps=1, sensory_inputs=signal_inputs)
        p_noise.evolve(steps=1, sensory_inputs=noise_inputs)
        
        # Measure Semantic Confidence
        _, conf_s = translator.decode(p_signal.psi)
        _, conf_n = translator.decode(p_noise.psi)
        
        signal_confidence.append(conf_s)
        noise_confidence.append(conf_n)

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(signal_confidence, label="Structured Input (Signal)", color='green')
    plt.plot(noise_confidence, label="Random Input (Noise)", color='gray', alpha=0.5)
    plt.title("Intrinsic Meaning: Semantic Confidence under Signal vs. Noise")
    plt.xlabel("Time Steps")
    plt.ylabel("Semantic Confidence (0-1)")
    plt.legend()
    plt.grid(True)
    plt.savefig("experiment_meaning_signal_noise.png")
    print("Meaning test complete. Saved 'experiment_meaning_signal_noise.png'.")
    
    avg_s = np.mean(signal_confidence)
    avg_n = np.mean(noise_confidence)
    print(f"Mean Confidence (Signal): {avg_s:.4f}")
    print(f"Mean Confidence (Noise): {avg_n:.4f}")
    
    if avg_s > avg_n * 1.05:
        print("RESULT: System RECOGNIZES SIGNAL (Intrinsic Meaning). Structure creates higher confidence states.")
    else:
        print("RESULT: System is AGNOSTIC (Constructed Meaning). Signal and Noise produce similar confidence.")

def run_utility_test():
    print("\n--- Running Experiment 3B: Utility-Based Evolution (Emergent Purpose) ---")
    
    # Subclass with dynamic goal weights (Values evolve based on experience)
    class EvolvingProcessor(UnifiedSubstrateProcessor):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            # Start with random values (Tabula Rasa / Moral Confusion)
            # Weights: Negative = Desired (Potential Basin), Positive = Repulsed
            np.random.seed(101) 
            self.goal_weights = np.random.uniform(-0.5, 0.5, 3) 
            self.goal_history = []

        def update_values(self):
            # The "Habit" Theory of Value: We value what we frequently experience.
            # If the system spends time in state k, does it learn to desire k?
            # We implemented: Successful existence in state K reinforces the desire for K.
            
            # current experience magnitude
            experience = np.abs(self.psi)
            
            # Update weights: Shift weights towards the current state configuration.
            # If we are in Flow (index 2), experience[2] is high.
            # We want weight[2] to become more NEGATIVE (attractor).
            # So we subtract a fraction of experience.
            
            learning_rate = 0.02
            self.goal_weights = self.goal_weights - (learning_rate * experience * 0.1)
            
            # Decay weights back to zero to prevent runaway? 
            # Or let them solidify? Let's add slight decay to normalize
            self.goal_weights *= 0.99
            
            self.goal_history.append(self.goal_weights.copy())

    p = EvolvingProcessor(n_heads=50)
    # Give it a "kick" of inputs initially to see where it settles
    initial_inputs = {0: np.array([0,0,0.5], dtype=np.complex128)} 
    
    steps = 300
    
    for t in range(steps):
        # We supply inputs only at start
        p.evolve(steps=1, sensory_inputs=initial_inputs if t == 0 else None)
        p.update_values()
        
    history = np.array(p.goal_history)
    
    plt.figure(figsize=(10, 5))
    labels = ["Plus (Dogma)", "Minus (Skepticism)", "Flow (Synthesis)"]
    colors = ['red', 'blue', 'purple']
    
    for i in range(3):
        plt.plot(history[:, i], label=f"Value of {labels[i]}", color=colors[i])
        
    plt.title("Evolution of Values (Teleology)")
    plt.xlabel("Time Steps")
    plt.ylabel("Goal Weight (Lower = More Desired)")
    plt.legend()
    plt.grid(True)
    plt.savefig("experiment_utility_evolution.png")
    print("Utility test complete. Saved 'experiment_utility_evolution.png'.")
    
    # Analyze convergence
    final_weights = history[-1]
    
    print("Final Goal Weights (Lower is better):", final_weights)
    
    # Check if they stabilized
    variance = np.var(history[-50:], axis=0) # Variance of last 50 steps
    if np.all(variance < 0.001):
        print("RESULT: Values CONVERGE. The system evolves a stable Purpose.")
        most_desired_idx = np.argmin(final_weights)
        print(f"Emergent Purpose: Maximize {labels[most_desired_idx]}")
    else:
        print("RESULT: Values DIVERGE or FLUCTUATE. No inherent purpose stabilizes.")

def run_gradient_test():
    print("\n--- Running Experiment 4A: Parameter Gradient Test (Duality vs Continuum) ---")
    
    # We will test how the system behaves under different levels of "Quantization"
    # Levels: 2 (Binary), 3 (Ternary), 10 (Lo-Fi), 100 (Effective Continuum)
    
    levels_to_test = [2, 3, 5, 100] 
    results = {}
    
    steps = 200
    
    for levels in levels_to_test:
        p = UnifiedSubstrateProcessor(n_heads=50)
        flow_history = []
        
        for t in range(steps):
            p.evolve(steps=1)
            
            # QUANTIZATION FORCE
            # Snap vector components to nearest 1/(N-1) increments.
            p.normalize()
            real = np.real(p.psi)
            imag = np.imag(p.psi)
            
            def quantize(val, k):
                return np.round(val * (k-1)) / (k-1)
            
            p.psi = quantize(real, levels) + 1j * quantize(imag, levels)
            
            flow_history.append(np.abs(p.psi[2]))
        
        results[levels] = np.mean(flow_history)
        
    plt.figure(figsize=(8, 5))
    x_vals = [str(l) for l in levels_to_test]
    y_vals = [results[l] for l in levels_to_test]
    
    plt.bar(x_vals, y_vals, color='orange')
    plt.title("System Vitality (Flow) vs. Reality Granularity")
    plt.xlabel("Quantization Levels (2 = Binary, 100 = Continuous)")
    plt.ylabel("Average Flow Magnitude")
    plt.grid(axis='y')
    plt.savefig("experiment_duality_gradient.png")
    print("Gradient test complete. Saved 'experiment_duality_gradient.png'.")
    
    if results[100] > results[2] * 1.5:
        print("RESULT: System requires GRADIENTS (Non-Dual). Binary collapse kills the Flow.")
    else:
        print("RESULT: System thrives in BINARY (Dualistic). Discrete states are sufficient.")

def run_opposites_test():
    print("\n--- Running Experiment 4B: Complementary Opposites (Harmony vs Dominance) ---")
    
    steps = 300
    p = UnifiedSubstrateProcessor(n_heads=50)
    
    # Initialize with Conflict: 50% Dogma (Plus), 50% Skepticism (Minus), 0% Flow
    p.psi = np.array([0.707, 0.707, 0.0], dtype=np.complex128) 
    
    plus_hist = []
    minus_hist = []
    flow_hist = []
    
    for t in range(steps):
        p.evolve(steps=1)
        plus_hist.append(np.abs(p.psi[0]))
        minus_hist.append(np.abs(p.psi[1]))
        flow_hist.append(np.abs(p.psi[2]))
        
    plt.figure(figsize=(10, 5))
    plt.plot(plus_hist, label="Plus (Order)", color='red', alpha=0.6)
    plt.plot(minus_hist, label="Minus (Chaos)", color='blue', alpha=0.6)
    plt.plot(flow_hist, label="Flow (Synthesis)", color='purple', linewidth=2)
    
    plt.title("Dynamic Interplay of Opposites")
    plt.xlabel("Time Steps")
    plt.ylabel("State Magnitude")
    plt.legend()
    plt.grid(True)
    plt.savefig("experiment_duality_opposites.png")
    print("Opposites test complete. Saved 'experiment_duality_opposites.png'.")
    
    final_plus = plus_hist[-1]
    final_minus = minus_hist[-1]
    final_flow = flow_hist[-1]
    
    if final_flow > final_plus and final_flow > final_minus:
        print("RESULT: System seeks HARMONY/SYNTHESIS. The third state emerges from the two.")
    elif abs(final_plus - final_minus) < 0.1:
        print("RESULT: System seeks BALANCE (Dualistic Stasis). P and M coexist equally.")
    else:
        print("RESULT: System seeks DOMINANCE. One side wins.")


if __name__ == "__main__":
    run_chaos_test()
    run_observer_test()
    run_meaning_test()
    run_utility_test()
    run_gradient_test()
    run_opposites_test()
