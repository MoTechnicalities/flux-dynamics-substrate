import numpy as np

class FluxTranslator:
    """
    Translates 3-component Quantum/Flux States into Semantic Concepts.
    Uses vector similarity to map the continuous state space to a discrete lexicon using Barycentric classification.
    """
    def __init__(self):
        # Define the Semantic landmarks in the 3D State Space
        # Vectors are normalized [Plus, Minus, Flow]
        self.lexicon = {
            # CORNERS (Pure States)
            "Dogmatic Certainty": np.array([1.0, 0.0, 0.0]),
            "Radical Skepticism": np.array([0.0, 1.0, 0.0]),
            "Pure Synthesis":     np.array([0.0, 0.0, 1.0]),

            # EDGES (Mixed States)
            "Cognitive Dissonance": np.array([0.5, 0.5, 0.0]), # Plus vs Minus collision
            "Progressive Growth":   np.array([0.5, 0.0, 0.5]), # Plus + Flow
            "Critical Analysis":    np.array([0.0, 0.5, 0.5]), # Minus + Flow
            
            # CENTER (Balance)
            "Equilibrium": np.array([0.333, 0.333, 0.333]),
            
            # NUANCED STATES
            "Establishment":      np.array([0.7, 0.2, 0.1]),
            "Rejecting":          np.array([0.1, 0.8, 0.1]),
            "Wonder/Curiosity":   np.array([0.1, 0.2, 0.7]),
            "Paradigm Shift":     np.array([0.3, 0.1, 0.6]),
        }
        
        # Pre-normalize lexicon vectors for accurate cosine similarity
        for key in self.lexicon:
            norm = np.linalg.norm(self.lexicon[key])
            if norm > 0:
                self.lexicon[key] /= norm

    def decode(self, state_vector):
        """
        Input: array [psi_plus, psi_minus, psi_flow]
        Output: (Concept String, Confidence Score, ColorCode)
        """
        # Ensure input is normalized real vector (magnitudes)
        if np.iscomplexobj(state_vector):
            v = np.abs(state_vector)
        else:
            v = np.array(state_vector)
            
        norm = np.linalg.norm(v)
        if norm > 0:
            v = v / norm
            
        # Find closest match
        best_word = "Undefined"
        best_score = -1.0
        
        for word, ref_vec in self.lexicon.items():
            # Dot product is cosine similarity for normalized vectors
            score = np.dot(v, ref_vec)
            if score > best_score:
                best_score = score
                best_word = word
                
        return best_word, best_score

    def describe_trajectory(self, trajectory):
        """
        Takes a list of states and generates a narrative log.
        """
        print(f"{'TIME':<6} | {'STATE VECTOR [+, -, F]':<25} | {'INTERPRETED CONCEPT'}")
        print("-" * 75)
        
        last_word = None
        for t, state in enumerate(trajectory):
            word, score = self.decode(state)
            
            # Log significant semantic shifts or periodic updates
            if word != last_word or t % 5 == 0:
                # Format vector nicely
                if np.iscomplexobj(state): state = np.abs(state)
                vec_str = f"[{state[0]:.2f}, {state[1]:.2f}, {state[2]:.2f}]"
                
                print(f"{t:<6} | {vec_str:<25} | {word}")
                last_word = word

# ─── DEMO: REPLAYING THE OPINION DYNAMICS ────────────────────────────────
if __name__ == "__main__":
    translator = FluxTranslator()
    
    print("Testing Semantic Decoder on simulated data...\n")
    
    # Generate a synthetic trajectory representing the "Truth Bomb" scenario
    # 1. Start Skeptical
    # 2. Truth hits (Collision/Dissonance)
    # 3. Flow rises (Synthesis)
    # 4. Truth stabilizes (Certainty)
    
    traj = []
    
    # Phase 1: Skepticism (High Minus)
    for i in range(5):
        traj.append([0.1, 0.9, 0.05])
        
    # Phase 2: Impact (Plus spikes, Minus still high)
    for i in range(5):
        traj.append([0.6, 0.7, 0.1]) # Unnormalized, decoder handles it
        
    # Phase 3: Reaction (Flow generated from conflict)
    for i in range(5):
        traj.append([0.5, 0.4, 0.8])
    
    # Phase 4: Resolution (Plus dominates, Flow supports, Minus fades)
    for i in range(5):
        traj.append([0.8, 0.1, 0.4])

    translator.describe_trajectory(traj)
