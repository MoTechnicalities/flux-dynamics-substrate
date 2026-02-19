# TriQbit Formalism: Hierarchical Dipolar Flux with Internal Knot Dynamics
**Date:** February 19, 2026  
**Status:** Theoretical Core v2  
**Context:** Flux Dynamics Substrate Physics

---

## 1. Dimensional Definition: Hierarchical Dipolar Flux

The fundamental substance is **dipolar flux**, $\mathbf{F}(\mathbf{x}, t)$, which exists simultaneously at all scales. It is characterized not just by position, but by internal hydrodynamics:

-   **Mass Density:** $\rho(\mathbf{x}, t)$
-   **Internal Flow Velocity:** $\mathbf{v}(\mathbf{x}, t)$

The total flux is a superposition of three hierarchical modes:

$$
\mathbf{F}(\mathbf{x}, t) = \sum_i K_i(\mathbf{x}, t) + \sum_j W_j(\mathbf{x}, t) + \sum_k L_k(\mathbf{x}, t)
$$

---

## 2. Micro Scale: Topological Knots ($K_i$)
**"The Particle" / Structure / Matter**

Knots are **tubular structures of circulating flux**. They are not point particles, but solenoidal flows with internal geometry.

### 2.1 Internal Knot Properties
*   **Effective Mass:** Arises from integrated flux density.
    $$ m_{\text{eff}} = \int_{\text{knot volume}} \rho(\mathbf{x}, t) \, d^3x $$

*   **Momentum:** Arises from internal flow.
    $$ \mathbf{p}_{\text{eff}} = \int_{\text{knot volume}} \rho(\mathbf{x}, t) \, \mathbf{v}(\mathbf{x}, t) \, d^3x $$

*   **Internal Energy:** Flow kinetic energy inside the knot.
    $$ E_{\text{internal}} = \int_{\text{knot volume}} \frac{1}{2} \rho(\mathbf{x}, t) |\mathbf{v}(\mathbf{x}, t)|^2 \, d^3x $$

*   **Spin:** Angular momentum emerges simply from tubular circulation.
    $$ \mathbf{S}_{\text{eff}} = \int_{\text{knot volume}} \mathbf{r} \times (\rho \mathbf{v}) \, d^3x $$

**TriQbit State:** $K_i \in \{-1, 0, +1\}$ (Orientation / Circulation / Winding Number).

---

## 3. Meso Scale: Propagating Waves ($W_j$)
**"The Photon" / Signal / Communication**

Small perturbations of the flux propagate as waves. In the low-amplitude limit, they exhibit Maxwell-like behavior linearized over the background flux:

$$
\partial_t^2 W_j - c^2 \nabla^2 W_j \approx 0
$$

**TriQbit State:** $W_j \in \{-1, 0, +1\}$ (Wave Polarity / Phase).

---

## 4. Macro Scale: Large Flux Structures ($L_k$)
**"The Field" / Context / Gravity**

Flux organizes into collective structures on large scales (vortices, flux tubes, gradients). This provides the "Environment" or "Mood" for the TriQbit.

**TriQbit State:** $L_k \in \{-1, 0, +1\}$ (Global Flux Orientation).

---

## 5. The TriQbit: Tensor Product
A single TriQbit is a tensor product of these three modes, binding Structure, Signal, and Context into one unit:

$$
\text{TriQbit}_i = K_i \otimes W_i \otimes L_i
$$

*   **Knot ($K_i$):** Carries Internal Flow, Energy, Mass, Spin.
*   **Wave ($W_i$):** Carries Phase/Amplitude Information.
*   **Macro ($L_i$):** Carries Contextual Flux Orientation.

---

## 6. Scale-Coupled Dynamics
The system evolves via **flux reshaping** ($\mathcal{C}$) between scales.

$$
\begin{cases}
\text{Micro Stability:} & \mathcal{N}[K_i] + \mathcal{C}[K_i, W_j] + \mathcal{C}[K_i, L_k] = 0 \\
\text{Propagation:} & \partial_t^2 W_j - c^2 \nabla^2 W_j + \mathcal{C}[W_j, K_i] + \mathcal{C}[W_j, L_k] = 0 \\
\text{Global Context:} & \mathcal{M}[L_k] + \mathcal{C}[L_k, K_i] + \mathcal{C}[L_k, W_j] = 0
\end{cases}
$$

*   $\mathcal{N}, \mathcal{M}$: Nonlinear operators at respective scales.
*   $\mathcal{C}$: Inter-scale flux coupling (Logic).

---

## 7. Emergence Table

| Property | Emergence from Flux Knot |
| :--- | :--- |
| **Mass** | Integrated flux density $\rho$ |
| **Inertia** | Internal flow resisting acceleration |
| **Energy** | Flow kinetic energy inside knot |
| **Spin** | Angular momentum of circulating flux |
| **Wave Behavior** | Phase coherence extending outward |

This formalism links **Topology**, **Hydrodynamics**, and **Quantum Information** into a single consistent physics.
