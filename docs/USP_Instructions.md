# Running the Unified Substrate Processor (USP)

This prototype implements the **9-Component Agency Architecture** defined in your theoretical models. It is a runnable Python class that simulates a cognitive cycle of Perception → Prediction → Error Correction → Action.

### **System Requirements**

*   **Python 3.8+**
*   **NumPy** (for matrix algebra)
*   **Matplotlib** (for visualizations)

Install dependencies:
```bash
pip install numpy matplotlib
```

### **How to Run**

Execute the script directly in your terminal:

```bash
python3 unified_mind_processor.py
```

### **What to Look For (Intelligence Indicators)**

The output graphs will display three key metrics that demonstrate "proto-intelligence":

1.  **Stream of Consciousness (Top Graph):**
    *   Watch how the **Cyan Line (Flow)** behaves.
    *   *Intelligence Test:* Does it rise *after* the conflict at t=50 and t=100? If the system successfully synthesizes the "Plus" and "Minus" inputs, the Flow should dominate by t=200. This indicates **Concept Formation**.

2.  **Cognitive Surprise (Middle Graph):**
    *   This measures `Prediction Error`.
    *   *Intelligence Test:* You should see spikes at t=50, t=100, and t=150 (when new data arrives).
    *   **Crucial:** Does the error line *decrease* after the spike? If the curve slopes downward, the system is **Learning** the pattern of the input.

3.  **Global Workspace Broadcast (Bottom Graph):**
    *   This represents the "Action" or "Speech" of the system.
    *   *Intelligence Test:* Look for coherent oscillations. Random noise means confusion. A stable rhythmic wave suggests a **Stable Mental State**.

### **Experiments to Try**

Open `unified_mind_processor.py` and modify the `inputs` dictionary at the bottom:

```python
    inputs = {
        50: np.array([0.1, 0.8, 0.0]),   # The Anomaly (Problem)
        100: np.array([0.8, 0.1, 0.0]),  # The Counter-Evidence
        150: np.array([0.2, 0.2, 0.9])   # The Solution Key
    }
```

*   **Test 1 (Dogmatism):** massive input to `Plus` (e.g., `[5.0, 0.0, 0.0]`). Does the system get stuck?
*   **Test 2 (Confusion):** fast alternating inputs every 10 steps. Does the "Flow" line collapse to zero?
