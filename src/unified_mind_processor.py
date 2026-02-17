import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict, Optional
from flux_translator import FluxTranslator

class UnifiedSubstrateProcessor:
    """
    Implements the 9-Component Agency Architecture within a unified Flux Q-Tribit Substrate.
    Adheres to the formal specifications of:
    1. Unified-Field Dynamical Model (Base Physics)
    2. Implementing Agency Inside a Unified Flux Q-Tribit Substrate (Cognitive Layer)
    
    The state is always normalized to Unit Norm (Unity of Experience).
    """

    def __init__(self, 
                 n_heads: int = 256, 
                 learning_rate: float = 0.05,
                 thought_strength: float = 0.12,
                 decay_rate: float = 0.008, 
                 spatial_coupling: float = 0.05):
        
        # ─── 0. State Space Implementation ────────────────────
        # Psi = [psi_plus, psi_minus, psi_flow]
        # Initialized to neutral synthesis
        self.psi = np.array([0.577+0j, 0.577+0j, 0.577+0j], dtype=np.complex128)
        self.normalize()
        
        # ─── Internal Generators ("Heads") ────────────────────
        self.H = n_heads
        self.W = np.ones(n_heads) * 0.1  # Head weights
        self.omega = 0.05                # Base rotation speed
        
        # ─── 9. Stability (Lyapunov params) ──────────────────
        self.mu = 0.01  # Stability correction rate
        
        # ─── 6. Memory Manifolds (Slow State) ────────────────
        self.M = np.zeros_like(self.psi)
        self.kappa = 0.02 # Memory update rate (slow)
        
        # ─── MEMORY KNOTS (Structural Plasticity) ────────────
        self.translator = FluxTranslator()
        self.memory_knots = []
        self.knot_bias = np.zeros(3, dtype=np.complex128) # Permanent structural deformities
        
        # ─── 4. Goal Architecture (Potential Function) ───────
        # Goals: Maximize Flow (Synthesis), Minimize Dogma
        # This creates a "Goal" to find synthesis in data
        self.goal_weights = np.array([0.1, 0.1, -0.5]) # Negative weight on Flow = Positive incentive
        self.rho = 0.2  # Synergy bonus
        self.gamma = 0.01 # Gradient descent rate for goals
        
        # ─── 2. World Model (Prediction Matrices) ────────────
        # A simple linear predictor: Psi(t+1) ~ G * Psi(t)
        self.G = np.eye(3, dtype=np.complex128)
        self.eta = learning_rate # Learning rate
        
        # ─── Config & History ────────────────────────────────
        self.alpha = thought_strength
        self.gamma_decay = decay_rate
        self.kappa_spatial = spatial_coupling
        
        self.history = {'psi': [], 'flow': [], 'prediction_error': [], 'action': []}
        self.time = 0

    def normalize(self):
        norm = np.linalg.norm(self.psi)
        if norm > 0:
            self.psi /= norm

    def get_phase_dynamics(self, t):
        # ─── 1. Internal Phases ──────────────────────────────
        # Returns vector of complex influence terms: theta_h
        phases = 2 * np.pi * np.arange(self.H) / self.H + self.omega * t
        thetas = self.W * self.alpha * np.exp(1j * phases)
        return thetas

    def compute_global_workspace(self):
        # ─── 1. Global Workspace (Gating) ────────────────────
        # "Attention" is the projection of the current state magnitude
        # W(t) acts as a broadcast signal strength
        gating = np.abs(self.psi) # Simple magnitude gating
        workspace = np.sum(gating * self.psi)
        return workspace

    def compute_world_model_prediction(self):
        # ─── 2. World Model Prediction ───────────────────────
        return np.dot(self.G, self.psi)

    def compute_reflexive_self(self, workspace_val, psi_dot):
        # ─── 3. Self-Model (Meta-State) ──────────────────────
        # S(t) is a function of State, Derivative, and Broadcast
        # Here simplified to a stabilizer dependent on rate of change
        volatility = np.abs(psi_dot)
        reflexive_correction = -0.1 * volatility * self.psi # Dampen if moving too fast (Homeostasis)
        return reflexive_correction

    def compute_goal_gradient(self):
        # ─── 4. Goal Architecture ────────────────────────────
        # U = -Sum(w|psi|^2)
        # Gradient of U with respect to Psi
        # Effectively: pushes state towards desired energy configuration
        # Logic: If psi_flow is desired, gradient pulls us there.
        grad = -2 * self.goal_weights * self.psi
        return grad

    def form_memory_knot(self):
        """If a state is stable, freeze it into the topology."""
        # Decode current state
        word, confidence = self.translator.decode(self.psi)
        
        # Conditions for Knotting:
        # 1. High Confidence (>0.9)
        # 2. Not already knotted (prevent duplicates)
        if confidence > 0.9 and word not in self.memory_knots:
            print(f"CRITICAL: Substrate has 'Knotted' a new core belief: {word}")
            self.memory_knots.append(word)
            
            # The Knot crystallizes, adding permanent structural bias.
            # This makes the mind 'heavier' in this direction (harder to flip).
            # We add a small permanent bias (Real-valued structure)
            knot_vector = np.abs(self.psi) 
            self.knot_bias += 0.08 * knot_vector # 0.08 is the 'Mass' of the knot

    def evolve(self, steps=100, sensory_inputs: Optional[Dict[int, np.ndarray]] = None):
        """
        Main evolution loop implementing the Unified Field dynamics.
        """
        print(f"Starting Evolution: {steps} cycles.")
        
        for t in range(steps):
            self.time += 1
            
            # Save prior state for differential calculation
            psi_prev = self.psi.copy()
            
            # --- A. PREDICTION PHASE (Cognition) ---
            psi_predicted = self.compute_world_model_prediction()
            
            # --- B. PHYSICS UPDATE (The Substrate) ---
            
            # 1. Decay on Flow
            self.psi[2] *= (1 - self.gamma_decay)
            
            # 2. Heads contribution
            thetas = self.get_phase_dynamics(self.time)
            
            # Sum head influences (simplified mapping to 3-vector)
            # 0..H/3 -> Plus, H/3..2H/3 -> Minus, Rest -> Flow
            split = self.H // 3
            influence_plus = np.sum(thetas[:split])
            influence_minus = np.sum(thetas[split:2*split])
            influence_flow = np.sum(thetas[2*split:])
            
            self.psi[0] += 1.2 * influence_plus
            self.psi[1] += 1.1 * influence_minus
            self.psi[2] += 0.9 * influence_flow

            # --- C. SENSORY INJECTION --- 
            if sensory_inputs and t in sensory_inputs:
                input_vec = sensory_inputs[t] # Expecting 3-vector
                self.psi += self.alpha * input_vec
                # "Surprise" signal for learning
                # High energy input = high attention moment

            # --- D. AGENCY & CONTROL CORRECTIONS ---
            
            # 1. Goal Seeking (Gradient Descent on Potential)
            grad_goal = self.compute_goal_gradient()
            self.psi -= self.gamma * grad_goal 
            
            # 2. Prediction Error Correction (Learning)
            pred_error = self.psi - psi_predicted
            self.psi -= 0.5 * self.eta * pred_error  # Correct state towards prediction (Active Inferenceish)
            
            # Update Internal Model G (Hebbian-like Learning)
            # G += eta * error * input.T (Simplified)
            delta_G = 0.01 * np.outer(pred_error, np.conj(psi_prev))
            self.G += delta_G
            
            # 3. Reflexive Self (Stability)
            psi_dot = self.psi - psi_prev
            ws = self.compute_global_workspace()
            self.psi += self.compute_reflexive_self(ws, psi_dot)
            
            # 4. Memory Integration
            # M(t+1) = (1-k)M + k*Psi
            self.M = (1 - self.kappa) * self.M + self.kappa * self.psi
            # Memory creates a "gravity" pulling current thought back to context
            self.psi += 0.05 * self.M
            
            # 5. Structural Knots (Long-term crystallized beliefs)
            # Permanent bias from past certitudes
            self.psi += self.knot_bias
            
            # Check for new knots periodically (Computational resource saving)
            if self.time % 5 == 0:
                self.form_memory_knot()

            # --- E. RENORMALIZATION (The Collapse) ---
            self.normalize()
            
            # --- F. HEAD UPDATE (Spatial Logic) ---
            # Update weights W using Laplacian (Spatial Coupling)
            # Head Power
            P = np.abs(thetas)**2 / (self.alpha**2 + 1e-9)
            global_interference = np.mean(P)
            
            # Laplacian Diffusion: W[i] gets signal from neighbors
            laplacian = np.roll(self.W, 1) - 2*self.W + np.roll(self.W, -1)
            
            # Update Rule
            self.W = self.W * (1 + 0.15*global_interference - 0.5*self.gamma_decay) + \
                     self.kappa_spatial * laplacian
            
            # Clip weights to prevent explosion
            self.W = np.clip(self.W, 0, 2.0)

            # --- G. LOGGING ---
            self.history['psi'].append(self.psi.copy())
            self.history['flow'].append(np.abs(self.psi[2])**2)
            self.history['prediction_error'].append(np.linalg.norm(pred_error))
            
            # "Action" is just the Real component of the workspace broadcast
            self.history['action'].append(np.real(ws))

    def report(self):
        flow_hist = np.array(self.history['flow'])
        pred_err = np.array(self.history['prediction_error'])
        
        print("\n─── UNIFIED SUBSTRATE REPORT ───")
        print(f"Final State: {self.psi}")
        print(f"Goal Alignment (Flow Strength): {flow_hist[-1]:.4f}")
        print(f"Prediction Error (Surprise): {pred_err[-1]:.4f}")
        
        # Plotting
        fig, axs = plt.subplots(3, 1, figsize=(10, 12), sharex=True)
        
        # Plot 1: Consciousness Stream (Amplitudes)
        psis = np.array(self.history['psi'])
        axs[0].plot(np.abs(psis[:,0])**2, label='Plus (Invariant)', color='green', alpha=0.7)
        axs[0].plot(np.abs(psis[:,1])**2, label='Minus (Slowdown)', color='red', alpha=0.7)
        axs[0].plot(np.abs(psis[:,2])**2, label='Flow (Synthesis)', color='cyan', linewidth=2)
        axs[0].set_title("Stream of Consciousness (Normalized Amplitudes)")
        axs[0].legend()
        axs[0].grid(True, alpha=0.2)
        
        # Plot 2: Prediction Error (Learning)
        axs[1].plot(pred_err, color='orange')
        axs[1].set_title("Cognitive Surprise (Prediction Error)")
        axs[1].set_ylabel("Error Magnitude")
        axs[1].grid(True, alpha=0.2)
        
        # Plot 3: Action Output
        axs[2].plot(self.history['action'], color='violet')
        axs[2].set_title("Global Workspace Broadcast (Action Signal)")
        axs[2].set_xlabel("Time Step (Cycle)")
        axs[2].grid(True, alpha=0.2)
        
        plt.tight_layout()
        output_file = "USP_Results.png"
        plt.savefig(output_file)
        print(f"Results plot saved to {output_file}")
        # plt.show()

# ─── RUNNER ────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Create the Artificial Organism
    brain = UnifiedSubstrateProcessor(n_heads=100)
    
    # Define a scenario
    # At t=50, a strong contradiction appears (High Minus)
    # At t=100, a supporting fact appears (High Plus)
    # At t=150, a synthesis cue appears (High Flow)
    inputs = {
        50: np.array([0.1, 0.8, 0.0]),   # The Anomaly (Problem)
        100: np.array([0.8, 0.1, 0.0]),  # The Counter-Evidence
        150: np.array([0.2, 0.2, 0.9])   # The Solution Key
    }
    
    # Run the mind
    brain.evolve(steps=300, sensory_inputs=inputs)
    brain.report()
