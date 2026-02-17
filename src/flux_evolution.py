import numpy as np
import matplotlib.pyplot as plt
from unified_mind_processor import UnifiedSubstrateProcessor
from flux_translator import FluxTranslator

class EvolutionSimulation:
    def __init__(self, steps=200, population_size=20):
        self.steps = steps
        self.translator = FluxTranslator()
        self.population = []
        
        # 1. Initialize The Mob (Random biases)
        print(f"Initializing Population of {population_size} agents...")
        for i in range(population_size):
            agent = UnifiedSubstrateProcessor(n_heads=50, thought_strength=0.1)
            # Random initialization
            r_real = np.random.rand(3)
            r_imag = np.random.rand(3) * 0.1
            agent.psi = r_real + 1j * r_imag
            agent.normalize()
            agent.form_memory_knot() # Give them a starting personality
            self.population.append(agent)

        # 2. Define the 5 Competing "Facts" (Memes/Truths)
        # We give them names for the chart
        self.facts = {
            "Tradition (High Plus)": np.array([0.9, 0.1, 0.0], dtype=np.complex128),   # Stable, resistant to change
            "Revolution (High Minus)": np.array([0.1, 0.9, 0.0], dtype=np.complex128), # Disruptive, questioning
            "Logic (High Flow)": np.array([0.1, 0.1, 1.5], dtype=np.complex128),       # The "Provable Fact" from before
            "Compromise (Balanced)": np.array([0.5, 0.5, 0.2], dtype=np.complex128),   # Moderate
            "Chaos (Noise)": np.array([0.3, 0.3, 0.3], dtype=np.complex128)            # High entropy, no clear direction
        }
        
        # Normalize facts just in case
        for name, vec in self.facts.items():
            norm = np.linalg.norm(vec)
            if norm > 0:
                self.facts[name] = vec / norm

        self.history = {name: [] for name in self.facts.keys()}

    def run(self):
        print(f"\nStarting 'Survival of the Fittest' Simulation ({self.steps} cycles)...")
        print("Competing Truths: " + ", ".join(self.facts.keys()))
        print("-" * 75)

        for t in range(self.steps):
            
            # Track popularity for this step
            current_votes = {name: 0 for name in self.facts.keys()}

            for agent in self.population:
                # 1. Exposure: Agent "samples" all 5 facts
                best_fact_name = None
                best_gain = -999.0
                
                initial_flow = agent.psi[2].real

                # Simulation: "What if I believed this?"
                for name, fact_vec in self.facts.items():
                    # Calculate resonance (Attraction)
                    resonance = np.abs(np.vdot(agent.psi, fact_vec))
                    
                    # Calculate Potential Flow Gain (Utility)
                    # We simulate a micro-step: If I accept this fact, do I get more Flow?
                    # Simplified: How much "Flow Energy" does this fact offer relative to my alignment?
                    # Logic (High Flow) natively offers more, but requires alignment to access it.
                    potential_flow = (fact_vec[2].real * resonance)
                    
                    if potential_flow > best_gain:
                        best_gain = potential_flow
                        best_fact_name = name

                # 2. Selection & Adaptation
                # The agent drifts slightly towards the "most useful" fact
                if best_fact_name:
                    target_vec = self.facts[best_fact_name]
                    # Learning rate
                    agent.psi = 0.9 * agent.psi + 0.1 * target_vec
                    
                    # Apply Shielding/Backfire if resonance is too low (Stubbornness check)
                    # Even if it's "useful", if I hate it, I might resist.
                    # For this Evoultion sim, we assume they are Pragmatic Survivors:
                    # They prioritize Flow (Utility) over Bias.
                    
                    current_votes[best_fact_name] += 1
                
                # 3. Internal Processing
                agent.psi[2] *= 0.99 # Decay flow slightly
                agent.normalize()

            # Record History
            for name in self.facts.keys():
                self.history[name].append(current_votes[name])

            if t % 20 == 0:
                leader = max(current_votes, key=current_votes.get)
                print(f"Time {t:<4} | Leader: {leader:<25} | Votes: {current_votes}")

        self.visualize_results()

    def visualize_results(self):
        steps = range(self.steps)
        plt.figure(figsize=(12, 8))
        
        # Plot Market Share of each Truth
        for name, votes in self.history.items():
            plt.plot(steps, votes, label=name, linewidth=2)
            
        plt.title('Survival of the Fittest: Evolution of Truth')
        plt.xlabel('Time Step')
        plt.ylabel('Number of Believers (Agents)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig("Flux_Evolution_Results.png")
        print("\nEvolution visualization saved to 'Flux_Evolution_Results.png'")

if __name__ == "__main__":
    sim = EvolutionSimulation(steps=200, population_size=20)
    sim.run()
