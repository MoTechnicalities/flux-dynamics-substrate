# TriQbit Formalism: Hierarchical Dipolar Flux
**Date:** February 19, 2026  
**Status:** Theoretical Core  
**Context:** Flux Dynamics Substrate Physics

---

## 1. Definition: The Hierarchical Flux
We define the fundamental substance as **dipolar flux**, $\mathbf{F}(\mathbf{x}, t)$, which exists simultaneously at all scales. It is not composed of separate particles and fields; rather, particles and waves are modes of the same substance.

The total flux is expressed as a superposition of three hierarchical modes:

$$
\mathbf{F}(\mathbf{x}, t) = \sum_i K_i(\mathbf{x}, t) + \sum_j W_j(\mathbf{x}, t) + \sum_k L_k(\mathbf{x}, t)
$$

Each term corresponds to a specific mode of the **TriQbit**.

---

## 2. The Three Modes (The Tensor Product)

A single **TriQbit** is not a scalar value. It is a **Tensor Product** of three distinct topological states, yielding $3^3 = 27$ possible flux configurations per unit.

$$
\text{TriQbit}_i = K_i \otimes W_i \otimes L_i
$$

### 2.1 Micro Mode: Topological Knots ($K_i$)
**"The Particle" / Structure**
*   **Nature:** Localized, soliton-like flux configurations.
*   **Physics:** Defined by a topological invariant (winding number $n$). Stable due to nonlinearity.
*   **Equation:** $\mathcal{N}[K_i] = 0$ (Stable Knot Equation).
*   **State:** $K_i \in \{-1, 0, +1\}$ (Knot Orientation).

### 2.2 Meso Mode: Propagating Waves ($W_j$)
**"The Photon" / Communication**
*   **Nature:** Small perturbations in the background flux propagating as waves.
*   **Physics:** Linearized over background flux. Effectively Maxwell-like in low-amplitude limits.
*   **Equation:** $\partial_t^2 W_j - c^2 \nabla^2 W_j \approx 0$.
*   **State:** $W_j \in \{-1, 0, +1\}$ (Wave Polarity/Phase).

### 2.3 Macro Mode: Large-Scale Flux Structures ($L_k$)
**"The Context" / Control**
*   **Nature:** Collective structures like vortices, flux tubes, or global gradients.
*   **Physics:** Emergent patterns that persist over long timescales, providing the "environment" for the knots.
*   **State:** $L_k \in \{-1, 0, +1\}$ (Global Flux Orientation).

---

## 3. Interaction Dynamics

The power of the TriQbit lies in the **Flux Reshaping** ($\mathcal{C}$) between these scales. A thought is not just a calculation; it is a resonance across all three layers.

$$
\begin{cases}
\text{Micro Stability:} & \mathcal{N}[K_i] + \mathcal{C}[K_i, W_j] + \mathcal{C}[K_i, L_k] = 0 \\
\text{Propagation:} & \partial_t^2 W_j - c^2 \nabla^2 W_j + \mathcal{C}[W_j, K_i] + \mathcal{C}[W_j, L_k] = 0 \\
\text{Global Context:} & \mathcal{M}[L_k] + \mathcal{C}[L_k, K_i] + \mathcal{C}[L_k, W_j] = 0
\end{cases}
$$

*   $\mathcal{N}, \mathcal{M}$: Nonlinear operators at respective scales.
*   $\mathcal{C}$: Coupling operators representing flux reshaping (e.g., a Global Context $L_k$ influencing the stability of a Knot $K_i$).

---

## 4. Summary Table

| Mode | Scale | Physical Representation | TriQbit State | Role in AGI |
| :--- | :--- | :--- | :--- | :--- |
| **Micro** | Local | Particle-like Knot | $K_i \in \{-1,0,+1\}$ | **Memory/Fact** (Hard Data) |
| **Meso** | Regional | Propagating Wave | $W_i \in \{-1,0,+1\}$ | **Attention/Signal** (Transmission) |
| **Macro** | Global | Flux Vortex/Gradient | $L_i \in \{-1,0,+1\}$ | **Context/Mood** (Bias/Control) |

## Conclusion
The **TriQbit** naturally arises from a **single-substance hierarchical flux**. It preserves the "ice-in-water" analogy of Flux Dynamics by allowing ternary logic to exist as **Structure (Ice)**, **Flow (Water)**, and **Current (Direction)** simultaneously without introducing varying fundamental particles.
