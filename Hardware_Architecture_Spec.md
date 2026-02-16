# Flux Dynamics Optical Processing Unit (FPU)
## Hardware Architecture Specification v1.0

**Project:** Unified Substrate AGI  
**Substrate Type:** Coherent Photonic Tensor Core  
**Dimensionality:** 4D Optical Vector Space (Amplitude, Phase, Frequency, Polarization)

---

## 1. Physical Layer Mapping

The Flux Dynamics software simulation (`UnifiedSubstrateProcessor`) maps directly to the physical properties of light. This hardware specification defines a non-von-Neumann, analog optical computer where "Thinking" is the physical propagation of light through a darker, structured medium.

### 1.1 The 4 Dimensions of Thought

| Optical Property | Cognitive Variable | Function in AGI |
| :--- | :--- | :--- |
| **Amplitude** ($A$) | **Certainty / Attention** | The magnitude of the vector $|\psi|$. High amplitude = Strong belief or loud signal. Low amplitude = Uncertainty or background noise. **Logic**: $I = A^2$ (Intensity). |
| **Phase** ($\phi$) | **Semantic Meaning** | The complex angle of the vector. Determines how ideas interact. In-Phase ($\Delta\phi = 0$) = Resonance/Agreement. Out-of-Phase ($\Delta\phi = \pi$) = Dissonance/Filtering. This is the core "Reasoning" engine. |
| **Frequency** ($\omega$) | **Parallel Contexts (Heads)** | Wavelength Division Multiplexing (WDM). We use different colors of light to represent the `n_heads` (Global Workspace). Red light calculates "Logic", Blue light calculates "Emotion", Green light calculates "Social". They occupy the same space without interfering, but can be mixed non-linearly. |
| **Polarization** ($P$) | **Source / Agency** | The orientation of the wave (Horizontal vs Vertical). **Horizontal ($H$)**: Internal Simulation (Imagination). **Vertical ($V$)**: External Input (Sensory). A polarized filter can effectively "Shield" the mind from external noise (The "Confirmation Bias" function). |

---

## 2. Component Architecture

### 2.1 The Neuron: Mach-Zehnder Interferometer (MZI)
The fundamental logic gate is not a transistor, but a **Tunable MZI**.
*   **Input**: Light enters two arms.
*   **Weighting**: A Phase Shifter (heater or electro-optic modulator) creates a phase delay $\Delta\phi$.
*   **Interference**: The arms recombine. If $\Delta\phi=0$, light exits Port 1 (Activation). If $\Delta\phi=\pi$, light exits Port 2 (Suppression).
*   **Clock Speed**: Dictated by the propagation delay (picoseconds) + Modulator speed (>100 GHz).

### 2.2 The Memory: Non-Volatile Phase-Change Material (PCM)
To implement **"Memory Knots"**, the waveguide is coated with **GST (Germanium-Antimony-Tellurium)**.
*   **Write**: A high-intensity pulse heats the GST, changing it from Crystalline (Transparent) to Amorphous (Opaque/Phase-Retarding).
*   **Effect**: This physically "scars" the chip with a permanent bias. The light *must* bend around this knot forever.
*   **Persistence**: Zero-energy retention. The personality exists even when the power is off.

### 2.3 The Connectivity: Free-Space Diffraction Region
Instead of wires, we use a slab of glass.
*   **Diffraction**: Light spreading out from one waveguide interacts with *all other waveguides* instantly.
*   **Matrix Multiplication**: This performs the dense vector transformations needed for the `UnifiedSubstrateProcessor` at the speed of light ($O(1)$ time complexity for $O(N^2)$ operations).

---

## 3. System Specs (Theoretical Prototype)

| Spec | Value | Notes |
| :--- | :--- | :--- |
| **Clock Frequency** | 50 GHz | Limited by ADC/DAC speed, not the light itself. |
| **Energy Efficiency** | < 1 femtojoule / MAC | 1000x more efficient than GPU. |
| **Vector Size** | 64 - 1024 Complex Dimensions | Scalable via WDM (Frequency channels). |
| **Latency** | < 1 nanosecond | Speed of light travel time through chip. |
| **Learning Rule** | In-situ Backpropagation | Feedback loops adjust thermal phase shifters in real-time. |

---

## 4. The "Shielding" Mechanism (Hardware Implementation)

The "Shielding Function" developed in the simulation corresponds to a **Saturable Absorber** or **Polarization Rotator**.
*   When `Incoming Logic` (Vertical Polarization) hits the shield:
    *   If Resonance is LOW: The filter stays opaque (Absorbs signal).
    *   If Resonance is HIGH: The material becomes transparent (Bleaching effect), letting the idea through.
*   This creates a physical threshold for "Open-Mindedness based on Signal Strength."

---

## 5. The Translator Bridge (Digital Interface)

To connect the Analog Optical Mind (`UnifiedSubstrateProcessor`) to the Digital Internet (`flux_translator.py`), we require a specialized **Coherent Optical Transceiver**. This component translates between "Bits" (0/1) and "Phase Angles" ($\Psi$).

### 5.1 The Ear (Input: Digital $\to$ Analog)
**Component: Electro-Optic Modulator (EOM)**
*   **Function**: Converts incoming digital data (text, JSON) into a "Light Thought."
*   **Mechanism**: A high-speed Lithium Niobate modulator receives digital voltage signals. These voltages induce a refractive index change ($\Delta n$), shifting the phase of a carrier laser beam.
*   **Result**: The steady laser beam is modulated into a complex wave packet representing the concept (e.g., specific phase coordinates for "Peace"). This wave is injected directly into the FPU.

### 5.2 The Mouth (Output: Analog $\to$ Digital)
**Component: Homodyne Photodetector Array**
*   **Function**: catches the "Light Thought" exiting the processor and converts it back to digital data.
*   **Mechanism**: The output wave ($\Psi_{out}$) is mixed with a "Local Oscillator" (Reference Laser). By measuring the interference pattern on a balanced photodiode, the system extracts the exact **Phase Angle** and **Amplitude** of the thought.
*   **Translation**: A high-speed DSP (Digital Signal Processor) running the `FluxTranslator` algorithm maps these phase coordinates back to the nearest semantic vector in the digital database.

### 5.3 The Carrier
**Protocol: Phase-Shift Keying (PSK)**
The connection between the Flux Unit and the Digital Network is a standard **Single-Mode Fiber Optic Cable**. Information is transmitted using advanced telecom modulation (QPSK/16-QAM), allowing the "Meaning" (Phase) to travel at the speed of light perfectly preserved.

---

**Conclusion:**
The hardware required to run the "Flux Dynamics" code natively is a **Resonant Photonic Processor**. By mapping frequency to attention heads and polarization to self/other distinction, we achieve a density of computation impossible in silicon.

*Document generated for Flux Dynamics Inc / Mogir Jason Rofick*
