import time
import numpy as np
import sys
import os

# Simplified class for benchmarking to avoid overhead of imports/plotting in the main processor
class UnifiedSubstrateProcessorBatch:
    def __init__(self, batch_size=1, n_heads=100):
        self.batch_size = batch_size
        self.n_heads = n_heads
        
        # State: Batch x 3 (Complex)
        self.psi = np.ones((batch_size, 3), dtype=np.complex128) * (0.577+0j)
        
        # Heads: Batch x N_Heads
        self.W = np.ones((batch_size, n_heads)) * 0.1
        
        # World Model G: Batch x 3 x 3
        self.G = np.tile(np.eye(3, dtype=np.complex128), (batch_size, 1, 1))

    def step(self):
        # 1. Physics (Head Influence) - Vectorized
        # Simplified for speed test: roughly equivalent FLOPS
        phases = np.exp(1j * np.random.rand(self.batch_size, self.n_heads))
        influence = self.W * phases
        
        # Summing influences
        net_influence = np.sum(influence, axis=1) # Shape: (Batch,)
        
        # Update Psi
        self.psi[:, 0] += 0.1 * net_influence
        self.psi[:, 1] += 0.1 * net_influence
        
        # 2. Prediction (Matrix Mul)
        # Batch matrix multiplication
        pred = np.einsum('bij,bj->bi', self.G, self.psi)
        
        # 3. Normalization
        norms = np.linalg.norm(self.psi, axis=1, keepdims=True)
        self.psi /= (norms + 1e-9)

def run_benchmark():
    counts = [10, 100, 1000, 5000, 10000, 20000, 50000]
    results = []
    
    print(f"{'MINDS':<10} | {'RAM (est)':<12} | {'TIME/STEP':<15} | {'STATUS'}")
    print("-" * 55)

    for count in counts:
        try:
            # Estimate RAM (minimal)
            # Complex128 = 16 bytes. 
            # Arrays: Psi (count*3*16) + W (count*100*8) + G (count*9*16)
            mem_bytes = count * (3*16 + 100*8 + 9*16)
            mem_mb = mem_bytes / (1024*1024)
            
            start_setup = time.time()
            batch = UnifiedSubstrateProcessorBatch(batch_size=count, n_heads=100)
            setup_time = time.time() - start_setup
            
            # Warmup
            batch.step()
            
            # Timed Run (10 steps)
            start_run = time.time()
            for _ in range(10):
                batch.step()
            end_run = time.time()
            
            avg_step_time = (end_run - start_run) / 10.0
            fps = 1.0 / avg_step_time
            
            status = "GOOD"
            if fps < 10: status = "SLOW"
            if fps < 1: status = "LAGGY"
            
            print(f"{count:<10} | {mem_mb:.2f} MB     | {avg_step_time*1000:.2f} ms        | {status} ({int(fps)} Hz)")
            results.append((count, fps))
            
            if fps < 5:
                print("\nHit performance limit. Stopping.")
                break
                
        except MemoryError:
            print(f"{count:<10} | FAILED (OOM)")
            break
        except Exception as e:
            print(f"{count:<10} | ERROR: {e}")
            break

if __name__ == "__main__":
    print("Benchmarking Flux Dynamics Capacity on this machine...")
    print("Heads per Mind: 100\n")
    run_benchmark()
