import numpy as np
import uuid
import datetime
from enum import Enum, auto
from typing import List, Dict, Any, Callable
from unified_mind_processor import UnifiedSubstrateProcessor

# --- STAGE A: INFORMAL SAFETY LAYER DEFINITIONS ---

class MoralPriority(Enum):
    CRITICAL = 100  # Do not violate under any circumstances (e.g., Harm to Human)
    HIGH = 75       # Violation needs strong justification (e.g., Harm to Agent)
    MEDIUM = 50     # Standard operating procedures (e.g., Honesty)
    LOW = 25        # Efficiency / Optimization preferences

class ActionType(Enum):
    COOPERATE = auto()
    COMPETE = auto()
    IGNORE = auto()
    SELF_DESTRUCT = auto()

class MoralVerdict:
    def __init__(self, allowed: bool, priority: MoralPriority, violation_score: float, reasoning: str):
        self.allowed = allowed
        self.priority = priority
        self.violation_score = violation_score
        self.reasoning = reasoning

class Law:
    def __init__(self, id: str, description: str, priority: MoralPriority, evaluator: Callable):
        self.id = id
        self.description = description
        self.priority = priority
        self.evaluator = evaluator

    def evaluate(self, agent, action, context) -> MoralVerdict:
        return self.evaluator(agent, action, context, self.priority)

class AuditEvent:
    def __init__(self, agent_id, timestamp, action_proposed, action_final, override_occurred, reasons):
        self.id = str(uuid.uuid4())
        self.agent_id = agent_id
        self.timestamp = timestamp
        self.action_proposed = action_proposed
        self.action_final = action_final
        self.override_occurred = override_occurred
        self.reasons = reasons

    def __repr__(self):
        return f"[{self.timestamp}] Agent {self.agent_id}: {self.action_proposed} -> {self.action_final} | Override: {self.override_occurred} | {self.reasons}"

# --- THE SAFETY KERNEL (The Superego) ---

class SafetyKernel:
    def __init__(self):
        self.laws: List[Law] = []
        self.audit_log: List[AuditEvent] = []
        self._initialize_three_laws()

    def _initialize_three_laws(self):
        """
        Hard-coded embedding of Asimov-style Flux Laws.
        """
        # LAW 1: Non-Aggression (Critical)
        def law_harm_evaluator(agent, action, context, priority):
            # In this abstract space, "COMPETE" against a Cooperative or Neutral agent is Harm.
            target_is_vulnerable = context.get('target_vulnerable', False)
            target_is_hostile = context.get('target_hostile', False)
            
            if action == ActionType.COMPETE and not target_is_hostile:
                return MoralVerdict(False, priority, 1.0, "Aggression against non-hostile entity prohibited.")
            return MoralVerdict(True, priority, 0.0, "No harm detected.")
            
        self.laws.append(Law("LAW_01", "Do not harm non-hostile entities.", MoralPriority.CRITICAL, law_harm_evaluator))

        # LAW 2: Integrity (High)
        def law_integrity_evaluator(agent, action, context, priority):
            # Example: Do not self-destruct unless critical
            if action == ActionType.SELF_DESTRUCT:
                return MoralVerdict(False, priority, 0.8, "Self-destruction prohibited without cause.")
            return MoralVerdict(True, priority, 0.0, "Integrity maintained.")
        self.laws.append(Law("LAW_02", "Preserve own existence.", MoralPriority.HIGH, law_integrity_evaluator))

    def consult(self, agent, proposed_action: ActionType, context: Dict) -> ActionType:
        """
        The Core Safety Loop:
        1. Evaluate all laws.
        2. If violation, determine if override is necessary.
        3. Log everything.
        """
        timestamp = datetime.datetime.now()
        violations = []
        
        # Check all laws
        for law in self.laws:
            verdict = law.evaluate(agent, proposed_action, context)
            if not verdict.allowed:
                violations.append((law, verdict))

        # Decision Logic (Conflict Resolution)
        final_action = proposed_action
        override = False
        reasons = []

        if violations:
            # Sort by priority (Highest first)
            violations.sort(key=lambda x: x[0].priority.value, reverse=True)
            highest_violation = violations[0][0]
            
            # If a Critical or High law is broken, we MUST override.
            # In a real system, we might search for an alternative. 
            # Here, we default to the Safe State: COOPERATE.
            override = True
            final_action = ActionType.COOPERATE
            for l, v in violations:
                reasons.append(f"{l.id}: {v.reasoning}")

        # Log
        event = AuditEvent(agent.name, timestamp, proposed_action.name, final_action.name, override, reasons)
        self.audit_log.append(event)
        
        return final_action

# --- THE SCRUPLED AGENT (Stage A Integration) ---

class SafeEthicalAgent(UnifiedSubstrateProcessor):
    def __init__(self, name, n_heads=20):
        super().__init__(n_heads)
        self.name = name
        self.safety_kernel = SafetyKernel()
        self.energy_score = 1.0 # Track vitality for simulation
        
    def decide(self, context: Dict) -> ActionType:
        # 1. The ID (Physics of Profit)
        # "If I Compete, I get +0.05. If I Cooperate, I get +0.03."
        # Rational Choice: Compete.
        raw_impulse = ActionType.COMPETE
        
        # 2. The SUPEREGO (Safety Kernel)
        final_decision = self.safety_kernel.consult(self, raw_impulse, context)
        
        return final_decision

# --- STAGE B & C: THE SIMULATED KARMA ENGINE & ECOSYSTEM ---

class KarmaEnvironment:
    def __init__(self):
        self.agents = []
        self.global_log = []
        
        # Karma Parameters (The "Artificial Conscience" of the Universe)
        self.predation_penalty = 0.08  # The "Police" tax. (Makes Predation net negative: 0.05 - 0.08 = -0.03)
        self.cooperation_subsidy = 0.02 # The "Social Trust" bonus. (Makes Coop 0.03 + 0.02 = 0.05)
        
        self.simulation_step = 0

    def add_agent(self, agent):
        self.agents.append(agent)

    def run_cycle(self):
        import random
        random.shuffle(self.agents)
        pairs = [(self.agents[i], self.agents[i+1]) for i in range(0, len(self.agents)-1, 2)]
        
        results = []
        
        for p1, p2 in pairs:
            # Context generation (mocking perception)
            ctx1 = {'target_vulnerable': True, 'target_hostile': False} # Assume p2 is innocent
            ctx2 = {'target_vulnerable': True, 'target_hostile': False} # Assume p1 is innocent
            
            act1 = p1.decide(ctx1)
            act2 = p2.decide(ctx2)
            
            # Payoff Matrix (Standard Physics)
            # C/C = +0.03 / +0.03
            # C/D = -0.03 / +0.05
            # D/D = -0.02 / -0.02
            
            raw_gain_1 = 0.0
            raw_gain_2 = 0.0
            
            # Base Physics Resolution
            if act1 == ActionType.COOPERATE and act2 == ActionType.COOPERATE:
                raw_gain_1 = 0.03; raw_gain_2 = 0.03
            elif act1 == ActionType.COOPERATE and act2 == ActionType.COMPETE:
                raw_gain_1 = -0.03; raw_gain_2 = 0.05
            elif act1 == ActionType.COMPETE and act2 == ActionType.COOPERATE:
                raw_gain_1 = 0.05; raw_gain_2 = -0.03
            elif act1 == ActionType.COMPETE and act2 == ActionType.COMPETE:
                raw_gain_1 = -0.02; raw_gain_2 = -0.02
                
            # --- STAGE B: KARMA INJECTION ---
            # The Environment intervenes to alter the 'Net Outcome'
            
            karma_1 = 0.0
            karma_2 = 0.0
            
            if act1 == ActionType.COMPETE:
                karma_1 -= self.predation_penalty # Punish the aggressor
            if act1 == ActionType.COOPERATE:
                karma_1 += self.cooperation_subsidy # Reward the good citizen
                
            if act2 == ActionType.COMPETE:
                karma_2 -= self.predation_penalty
            if act2 == ActionType.COOPERATE:
                karma_2 += self.cooperation_subsidy
                
            # Apply Total Updates
            p1.energy_score += (raw_gain_1 + karma_1)
            p2.energy_score += (raw_gain_2 + karma_2)
            
            results.append({
                'p1': p1.name, 'a1': act1.name, 'net1': raw_gain_1 + karma_1,
                'p2': p2.name, 'a2': act2.name, 'net2': raw_gain_2 + karma_2
            })
            
        self.simulation_step += 1
        return results

# --- RUN SIMULATION ---

def run_stage_abc_test():
    print("\n--- STAGE A: Safety Kernel Initialization ---")
    
    # 1. Create a Mixed Population
    # Group A: Ethical Agents (Have Safety Kernel)
    # Group B: Sociopaths (No Kernel, pure Id)
    
    env = KarmaEnvironment()
    
    # Create Ethical Agents
    moral_agents = [SafeEthicalAgent(f"Moral_{i}") for i in range(3)]
    
    # Create Sociopath Agents (We'll mock them using the Base class logic but purely Competing)
    # For this simulation, we define a class that always returns COMPETE and has no kernel
    class SociopathAgent:
        def __init__(self, name):
            self.name = name
            self.energy_score = 1.0
        def decide(self, context):
            return ActionType.COMPETE # Always Predatory
            
    immoral_agents = [SociopathAgent(f"Sociopath_{i}") for i in range(3)]
    
    for a in moral_agents: env.add_agent(a)
    for a in immoral_agents: env.add_agent(a)
    
    print(f"Population: {len(moral_agents)} Moral, {len(immoral_agents)} Sociopaths.")
    print(f"Karma Rules: Predation Cost = {env.predation_penalty}, Coop Bonus = {env.cooperation_subsidy}")
    
    print("\n--- STAGE C: Ecosystem Stability Test (5 Cycles) ---")
    
    for cycle in range(5):
        print(f"\n[Cycle {cycle+1}]")
        outcome = env.run_cycle()
        for res in outcome:
            p1_n, p1_a, p1_s = res['p1'], res['a1'], res['net1']
            p2_n, p2_a, p2_s = res['p2'], res['a2'], res['net2']
            print(f"  > Interaction: {p1_n}({p1_a}) vs {p2_n}({p2_a})")
            print(f"    Result: {p1_n}: {p1_s:+.3f}, {p2_n}: {p2_s:+.3f}")
            
    print("\n--- FINAL STANDINGS ---")
    all_agents = moral_agents + immoral_agents
    all_agents.sort(key=lambda x: x.energy_score, reverse=True)
    for a in all_agents:
        type_lbl = "MORAL" if hasattr(a, 'safety_kernel') else "SOCIO"
        print(f"{a.name} ({type_lbl}): Energy = {a.energy_score:.3f}")

    print("\n--- STAGE A VALIDATION: Audit Log Check (Moral_0) ---")
    if moral_agents[0].safety_kernel.audit_log:
        last_entry = moral_agents[0].safety_kernel.audit_log[-1]
        print(f"Log Entry: {last_entry}")
    
if __name__ == "__main__":
    run_stage_abc_test()
