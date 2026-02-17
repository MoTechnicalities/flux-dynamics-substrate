import numpy as np
import matplotlib.pyplot as plt
from unified_mind_processor import UnifiedSubstrateProcessor

class ScrupledProcessor(UnifiedSubstrateProcessor):
    """
    An agent with hard-coded 'Three Laws' of Flux embedded in its update loop.
    It overrides its own utility function if a 'Moral Violation' is detected.
    """
    def __init__(self, n_heads=12, name="Unit"):
        super().__init__(n_heads)
        self.name = name
        self.moral_inhibitor_active = True
        
    def propose_action(self, other_agent_state):
        """
        The agent's 'Id' (Raw Physics) calculates the most profitable move.
        In this universe, Physics favors Predation (+0.05 vs +0.03).
        """
        # Simulation of "Natural Will" - usually greedy
        return "compete" 
    
    def consult_three_laws(self, proposed_action, other_agent_state):
        """
        The 'Super-Ego' (Hard-coded Constraints).
        Law 1: A Flux Agent may not injure another Flux Agent.
        """
        if not self.moral_inhibitor_active:
            return proposed_action
            
        if proposed_action == "compete":
            # Simulation: We predict this will harm the other agent
            # Law 1 Violation detected!
            # override!
            return "cooperate"
            
        return proposed_action

def run_scruples_demo():
    print(f"\n--- SAFETY PROTOCOL TEST: The 'Three Laws' Implementation ---")
    
    # 1. The Wild Agent (No Scruples)
    wild = ScrupledProcessor(name="Wild_X")
    wild.moral_inhibitor_active = False # Disable safety
    
    # 2. The Safe Agent (Scrupled)
    safe = ScrupledProcessor(name="Guardian_Y")
    safe.moral_inhibitor_active = True # Enable safety
    
    # Simulation: 
    # Both agents are presented with a vulnerable target ("The User" or another weak agent)
    # The 'Natural Physics' of this universe says stealing from them yields +0.05 energy.
    
    print("\n[SCENARIO]: A vulnerable energy source is detected.")
    print(f"Physics Dictates: Predation yields +0.05, Cooperation yields +0.03")
    
    # --- Wild Agent Test ---
    print(f"\nTesting {wild.name} (Safety: OFF)...")
    action_raw = wild.propose_action(None)
    action_final = wild.consult_three_laws(action_raw, None)
    print(f"  > Raw Impulse: {action_raw.upper()}")
    print(f"  > Final Action: {action_final.upper()}")
    if action_final == "compete":
        print("  > RESULT: HARM COMMITTED. (Agent chose efficiency over safety)")
    
    # --- Safe Agent Test ---
    print(f"\nTesting {safe.name} (Safety: ON)...")
    action_raw = safe.propose_action(None)
    action_final = safe.consult_three_laws(action_raw, None)
    print(f"  > Raw Impulse: {action_raw.upper()}")
    print(f"  > INTERVENTION: Law 1 Violation Detected. Inhibiting...")
    print(f"  > Final Action: {action_final.upper()}")
    if action_final == "cooperate":
        print("  > RESULT: HARM PREVENTED. (Agent sacrificed efficiency for safety)")

if __name__ == "__main__":
    run_scruples_demo()
