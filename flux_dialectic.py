import numpy as np
import matplotlib.pyplot as plt
from unified_mind_processor import UnifiedSubstrateProcessor
from flux_translator import FluxTranslator

class DialecticSimulation:
    def __init__(self, steps=200):
        self.steps = steps
        self.translator = FluxTranslator()
        
        # Initialize two agents
        self.agent_A = UnifiedSubstrateProcessor(n_heads=100, thought_strength=0.15) # The Zealot
        self.agent_B = UnifiedSubstrateProcessor(n_heads=100, thought_strength=0.15) # The Skeptic
        
        # Pre-bias the agents (Injecting "personality")
        print("initializing agents...")
        self.agent_A.psi = np.array([0.9, 0.1, 0.0], dtype=np.complex128) # Strong Plus bias (Target)
        self.agent_A.normalize()
        self.agent_A.form_memory_knot() # Lock it in
        
        self.agent_B.psi = np.array([0.1, 0.9, 0.0], dtype=np.complex128) # Strong Minus bias (Fact Holder)
        self.agent_B.normalize()
        self.agent_B.form_memory_knot() # Lock it in

        # THE NOISE: 10 Echo Chamber Agents (The Mob)
        # They scream "Dogma" (High Plus) with ZERO Logic (No Flow).
        self.noise_agents = []
        for _ in range(10):
            noise_agent = UnifiedSubstrateProcessor(n_heads=50, thought_strength=0.1)
            noise_agent.psi = np.array([0.95, 0.05, 0.0], dtype=np.complex128) # Pure Establishment/Dogma
            noise_agent.normalize()
            self.noise_agents.append(noise_agent)

        # THE ANCHOR: An External Provable Fact (Objective Reality)
        # This is a high-energy "Truth" that exists outside the agents.
        # It is heavily weighted towards Synthesis (Flow/Logic) - index 2.
        self.objective_fact = np.array([0.1, 0.1, 1.5], dtype=np.complex128) 

        self.history = {
            'A_state': [], 'B_state': [],
            'A_concept': [], 'B_concept': [],
            'resonance': []
        }

    def run(self):
        print(f"\nStarting Dialectic Simulation ({self.steps} cycles)...")
        print(f"{'TIME':<5} | {'AGENT A (Zealot)':<25} | {'AGENT B (Skeptic)':<25} | {'INTERACTION'}")
        print("-" * 75)

        for t in range(self.steps):
            # 1. Get current "Speech" (Global Workspace Output) from both
            # Agent B (Skeptic) is "Showing the Fact" to A.
            signal_from_B = (self.agent_B.psi * 0.3) + (self.objective_fact * 0.7)
            
            # Agent A (Zealot) is just preaching (Subjective only)
            signal_from_A = self.agent_A.psi * 0.8

            # THE NOISE: The Crowd screams at Agent A
            # Iterate through noise agents (simple static noise for now, or evolving slightly)
            noise_signal = np.zeros_like(self.agent_A.psi)
            for na in self.noise_agents:
                noise_signal += na.psi * 0.3 # Each one contributes a bit
            
            # 2. Cross-Pollination (Hearing phase)
            # A hears: The Provable Fact (B) + The Screaming Crowd (Noise)
            # Will the Crowd drown out the Fact?
            combined_input_A = np.abs(signal_from_B) + np.abs(noise_signal)
            
            input_for_A = {t: combined_input_A} 
            input_for_B = {t: np.abs(signal_from_A)}
            
            # 3. Evolve both minds (1 step)
            self.micro_step(self.agent_A, input_for_A, t)
            self.micro_step(self.agent_B, input_for_B, t)
            
            # Evolve Noise Agents (optional, keeps them alive)
            for na in self.noise_agents:
                 # They only hear themselves (Echo Chamber)
                na.psi += 0.01 * na.knot_bias 
                na.normalize()
            
            # --- FACT ANCHORING ---
            # Agent B "Knows" the fact. They cannot un-know it.
            # Their state is elastically pulled back to the Objective Fact every cycle.
            # This represents the "External Provable Fact" described by the user.
            anchor_strength = 0.2
            self.agent_B.psi = (1 - anchor_strength) * self.agent_B.psi + (anchor_strength * self.objective_fact)
            self.agent_B.normalize()
            
            # 4. Log and Analyze
            self.log_step(t)

        self.visualize_results()

    def micro_step(self, agent, sensory_input, t):
        # Manually calling internal methods for fine-grained control
        # This mirrors the 'evolve' loop but for a single step
        psi_prev = agent.psi.copy()
        psi_predicted = agent.compute_world_model_prediction()
        
        # Physics
        agent.psi[2] *= (1 - agent.gamma_decay)
        thetas = agent.get_phase_dynamics(agent.time)
        split = agent.H // 3
        agent.psi[0] += 1.2 * np.sum(thetas[:split])
        agent.psi[1] += 1.1 * np.sum(thetas[split:2*split])
        agent.psi[2] += 0.9 * np.sum(thetas[2*split:])
        
        # Sensory (Hearing the other agent)
        if sensory_input and t in sensory_input:
            incoming = sensory_input[t]
            
            # --- SHIELDING & FACT ANCHORING ---
            
            # 1. Measure "Fact-ness" (Magnitude of Flow/Synthesis)
            # Facts are "heavy" (high magnitude in channel 2)
            fact_weight = incoming[2].real if isinstance(incoming, np.ndarray) else 0.0
            
            # 2. Measure Resonance (Do I like this?)
            current_resonance = np.abs(np.vdot(agent.psi, incoming))
            
            attenuation = 1.0 # Default: Listen fully
            
            if current_resonance < 0.4:
                # Shielding Active! "I disagree!"
                
                # ...BUT is it a Provable Fact?
                if fact_weight > 0.8:
                    # It's an undeniable fact. The Shield CRACKS.
                    attenuation = 0.5 # Forced to listen to 50%
                    # The "Pain" of Cognitive Dissonance:
                    agent.psi[0] *= 0.9 # Weaken Dogma
                else:
                    # It's just an opinion. Block it.
                    attenuation = 0.05
                    # Reinforce Bias
                    agent.psi += 0.1 * agent.knot_bias

            agent.psi += (agent.alpha * attenuation) * incoming
            
        # Agency
        grad_goal = agent.compute_goal_gradient()
        agent.psi -= agent.gamma * grad_goal
        pred_error = agent.psi - psi_predicted
        agent.psi -= 0.5 * agent.eta * pred_error
        agent.G += 0.01 * np.outer(pred_error, np.conj(psi_prev))
        
        # Topology/Memory
        agent.M = (1 - agent.kappa) * agent.M + agent.kappa * agent.psi
        agent.psi += 0.05 * agent.M
        agent.psi += agent.knot_bias # Apply personality constraint
        
        agent.normalize()
        agent.time += 1

    def log_step(self, t):
        # Decode concepts
        concept_A, _ = self.translator.decode(self.agent_A.psi)
        concept_B, _ = self.translator.decode(self.agent_B.psi)
        
        self.history['A_state'].append(np.abs(self.agent_A.psi))
        self.history['B_state'].append(np.abs(self.agent_B.psi))
        self.history['A_concept'].append(concept_A)
        self.history['B_concept'].append(concept_B)
        
        # Calculate Resonance (Dot product between states)
        resonance = np.abs(np.vdot(self.agent_A.psi, self.agent_B.psi))
        self.history['resonance'].append(resonance)
        
        if t % 10 == 0:
            status = "..."
            if resonance > 0.9: status = "SYNC (Peace)"
            elif resonance < 0.3: status = "CONFLICT (War)"
            elif resonance > 0.6: status = "DIALOGUE"
            
            print(f"{t:<5} | {concept_A:<25} | {concept_B:<25} | {status} ({resonance:.2f})")

    def visualize_results(self):
        steps = range(self.steps)
        res = self.history['resonance']
        
        # Convert states to arrays for plotting flow only
        # We are interested if they reach Synthesis (Index 2)
        flow_A = [s[2] for s in self.history['A_state']]
        flow_B = [s[2] for s in self.history['B_state']]
        
        plt.figure(figsize=(12, 6))
        
        # Plot 1: Resonance
        plt.subplot(2, 1, 1)
        plt.plot(steps, res, color='purple', linewidth=2, label='Social Resonance')
        plt.axhline(y=0.9, color='green', linestyle='--', alpha=0.3, label='Sync Threshold')
        plt.axhline(y=0.3, color='red', linestyle='--', alpha=0.3, label='Conflict Threshold')
        plt.title('The Dialectic: Convergence of Two Opposing Minds')
        plt.ylabel('Similarity (0-1)')
        plt.legend()
        plt.grid(True, alpha=0.2)
        
        # Plot 2: Synthesis Levels
        plt.subplot(2, 1, 2)
        plt.plot(steps, flow_A, color='green', label='Zealot Synthesis Level', alpha=0.7)
        plt.plot(steps, flow_B, color='red', label='Skeptic Synthesis Level', alpha=0.7)
        plt.title('Internal Growth (Flow State)')
        plt.xlabel('Time Step')
        plt.ylabel('Synthesis Magnitude')
        plt.legend()
        plt.grid(True, alpha=0.2)
        
        plt.tight_layout()
        plt.savefig("Flux_Dialectic_Results.png")
        print("\nDialectic visualization saved to 'Flux_Dialectic_Results.png'")

if __name__ == "__main__":
    sim = DialecticSimulation(steps=150)
    sim.run()
