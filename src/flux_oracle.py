import numpy as np
import matplotlib.pyplot as plt
from unified_mind_processor import UnifiedSubstrateProcessor

# Seed for reproducibility
np.random.seed(42)

def generate_market_data(steps=300):
    """
    Simulates a noisy, semi-cyclical market asset.
    Structure: Underlying Sine Wave + Linear Trend + Gaussian Noise.
    """
    t = np.linspace(0, 6*np.pi, steps)
    
    # 1. The "Signal" (The hidden pattern)
    # A true value underlying the noise
    fundamental = np.sin(t)
    
    # 2. The "Noise" (Chaos)
    # Random walk + Gaussian jitter
    jitter = np.random.normal(0, 0.5, size=steps)
    trend = t * 0.05
    
    # 3. The "Price" (Observed Reality)
    price = fundamental + jitter + trend
    
    # Normalize for safety
    price = (price - np.mean(price)) / np.std(price)
    fundamental = (fundamental - np.mean(fundamental)) / np.std(fundamental)
    
    return price, fundamental

def run_oracle_test():
    print("\n--- Running Experiment 8A: The Oracular Test (Pattern Recognition) ---")
    
    steps = 300
    price_data, true_signal = generate_market_data(steps)
    
    # Pass 1: Reactive Agent (High Sensitivity)
    print("Test 1: Reactive Agent (Fast Learning)...")
    oracle_fast = UnifiedSubstrateProcessor(n_heads=50, learning_rate=0.2, decay_rate=0.01)
    
    # Pass 2: Stable Oracle (High Inertia)
    print("Test 2: Stable Oracle (Deep Learning)...")
    oracle_slow = UnifiedSubstrateProcessor(n_heads=200, learning_rate=0.01, decay_rate=0.005)
    
    history_fast = []
    history_slow = []
    
    for t in range(steps):
        val = price_data[t]
        input_vec = np.array([val * 0.1, 0, 0], dtype=np.complex128)
        
        # Evolve Fast
        oracle_fast.psi += input_vec
        oracle_fast.evolve(steps=1)
        history_fast.append(oracle_fast.psi[0].real)
        
        # Evolve Slow
        oracle_slow.psi += input_vec
        oracle_slow.evolve(steps=1)
        history_slow.append(oracle_slow.psi[0].real)
        
    # Stats
    def get_corr(hist, target):
        norm_h = (hist - np.mean(hist))/np.std(hist)
        return np.corrcoef(norm_h, target)[0,1]
        
    corr_fast_noise = get_corr(history_fast, price_data)
    corr_fast_signal = get_corr(history_fast, true_signal)
    
    corr_slow_noise = get_corr(history_slow, price_data)
    corr_slow_signal = get_corr(history_slow, true_signal)
    
    print(f"\n[Reactive Agent Results]")
    print(f"  vs Noise: {corr_fast_noise:.4f}")
    print(f"  vs Signal: {corr_fast_signal:.4f}")
    
    print(f"\n[Stable Oracle Results]")
    print(f"  vs Noise: {corr_slow_noise:.4f}")
    print(f"  vs Signal: {corr_slow_signal:.4f}")

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(price_data, label="Market Price (Noise)", alpha=0.3, color='gray')
    plt.plot(true_signal, label="Hidden Signal (Truth)", color='green', linestyle="--", linewidth=2)
    
    # Normalize for plotting
    norm_fast = (history_fast - np.mean(history_fast))/np.std(history_fast)
    norm_slow = (history_slow - np.mean(history_slow))/np.std(history_slow)
    
    plt.plot(norm_fast, label=f"Reactive (Corr={corr_fast_signal:.2f})", color='orange', alpha=0.6)
    plt.plot(norm_slow, label=f"Stable Oracle (Corr={corr_slow_signal:.2f})", color='purple', linewidth=2.5)
    
    plt.title("Chaos vs Stability: Extracting Signal from Noise")
    plt.legend()
    plt.savefig("experiment_oracle_market.png")
    
    if corr_slow_signal > corr_fast_signal:
        print("\nRESULT: STABILITY WINS. The Slow Oracle filtered the noise better.")
    else:
        print("\nRESULT: CHAOS WINS. The Reactive Agent tracked better.")

if __name__ == "__main__":
    run_oracle_test()
