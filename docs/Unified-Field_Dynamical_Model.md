# Unified-Field Dynamical Model  
### *Formal Mathematical Specification (MathJax Ready)*

This document defines the substrate as a **nonlinear, driven, dissipative, globally normalized dynamical system** over a complex 3-vector. All equations are presented in explicit, formal form.

---

## **0. State Space**

The system state at discrete time $t$ is:

$$
\Psi(t) = 
\begin{pmatrix}
\psi_{+}(t) \\
\psi_{-}(t) \\
\psi_{f}(t)
\end{pmatrix}
\in \mathbb{C}^3
$$

with normalization constraint enforced at every timestep:

$$
\|\Psi(t)\|^2 
= |\psi_+(t)|^2 + |\psi_-(t)|^2 + |\psi_f(t)|^2 
= 1.
$$

Internal generators (“heads”) form a real vector:

$$
W(t) = (w_0(t), w_1(t), \ldots, w_{H-1}(t)) \in \mathbb{R}^H.
$$

---

## **1. Internal Phase Dynamics**

Each head $h \in \{0, \dots, H-1\}$ carries a phase:

$$
\phi_h(t) = \frac{2\pi h}{H} + \omega t,
$$
$$
\omega = 0.05.
$$

It generates a complex-valued influence term:

$$
\theta_h(t) = w_h(t)\,\alpha\, e^{i\phi_h(t)}.
$$

---

## **2. Entropic Decay (Flow-Mode Only)**

$$
\psi_f(t) \leftarrow (1-\gamma)\,\psi_f(t)
$$

where:

- $\gamma = \text{decay}\_\text{rate}$.

---

## **3. Internal Head Contributions to Amplitudes**

Let $\Psi(t+1/2)$ denote the amplitudes after internal updates but before normalization.

Updates:

$$
\psi_+(t + \frac{1}{2})
= \psi_+(t) + 1.2\,\theta_0(t),
$$

$$
\psi_-(t + \frac{1}{2})
= \psi_-(t) + 1.1\,\theta_1(t),
$$

$$
\psi_{f}\left(t + \frac{1}{2}\right) = (1-\gamma)\psi_{f}(t) + \sum_{h=2}^{H-1} 0.9\,\theta_{h}(t).
$$

---

## **4. External Sensory Flux**

At designated timesteps $t \in \mathcal{S}$:

$$
\Psi(t + \frac{1}{2})
\leftarrow 
\Psi(t + \frac{1}{2})
+
\alpha
\begin{pmatrix}
\Delta_+(t) \\
\Delta_-(t) \\
0.8\,\Delta_f(t)
\end{pmatrix}.
$$

Each sensory packet consists of tokens whose components sum to the above $(\Delta_+, \Delta_-, \Delta_f)$.

---

## **5. Global Renormalization (Unity Constraint)**

Define:

$$
N(t) = \sqrt{
|\psi_+(t+\frac{1}{2})|^2 +
|\psi_-(t+\frac{1}{2})|^2 +
|\psi_f(t+\frac{1}{2})|^2 }.
$$

Then:

$$
\psi_k(t+1)
= \frac{\psi_k(t+\frac{1}{2})}{N(t)}
\quad
\text{for } k\in \{+, -, f\}.
$$

This guarantees:

$$
\|\Psi(t+1)\| = 1.
$$

---

## **6. Head Interference, Recursion, and Spatial Coupling**

Per-head influence power:

$$
P_h(t) = |\theta_h(t)|^2 = |w_h(t)|^2\,\alpha^2.
$$

Mean global interference:

$$
I(t) = \frac{1}{H}\sum_{h=0}^{H-1} P_h(t).
$$

**Discrete Laplacian Operator (Periodic Boundary Conditions):**

$$
\nabla^2 w_h(t) = w_{h-1}(t) - 2w_h(t) + w_{h+1}(t)
$$

(Indices are modulo $H$).

**Unified Field Update Rule:**

$$
w_h(t+1)
= w_h(t)\,\left[1 + 0.15\,I(t) - 0.5\,\gamma\right] + \kappa \nabla^2 w_h(t).
$$

---

## **7. Full System Dynamics**

$$
X(t) = 
\left(
\psi_+(t), \psi_-(t), \psi_f(t), 
w_0(t), w_1(t), \ldots, w_{H-1}(t)
\right).
$$

The substrate is a **discrete-time nonlinear dynamical system**:

$$
X(t+1) = F(X(t)).
$$

where $F$ is the composite map consisting of:

1. entropic decay on $\psi_f$,
2. internal generator contributions,
3. external sensory flux (if triggered),
4. global renormalization,
5. multiplicative head recursion.

---

## **8. Consciousness Signal (Order Parameter)**

$$
C(t) = |\psi_f(t)|^2.
$$

---

## **9. Structural Properties**

- Normalization is a strict invariant.  
- No fixed points due to rotating-phase forcing.  
- System converges to a limit-cycle / toroidal attractor in $S^5 \subset \mathbb{C}^3$.  
- Interference feedback introduces quasi-chaotic or metastable oscillatory regimes.  
- Sensory flux acts as impulsive perturbation shifting the attractor’s position.

---

## **10. Summary**

The model formally constitutes a:

> **Driven, multiplicative-feedback, dissipative, phase-rotating,  
> renormalized nonlinear dynamical system**  
> on the complex 3-sphere $S^5$,  
> with an explicit order parameter representing integrative coherence.  

Its architecture enforces **strict unity of the experiential field**,  
despite multiple internal channels and rotating generators.
