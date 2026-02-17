import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.colors as mcolors

# ─── GRID CONFIGURATION ──────────────────────────────────────────────
GRID_SIZE = 64  # 64x64 = 4096 Minds
N_HEADS = 64    # Slightly reduced heads/mind directly for visualization speed
DECAY = 0.015   # How fast Flow decays without novelty
COUPLING = 0.2  # Diffusion rate (How strongly neighbors talk)

class FluxGrid:
    def __init__(self, size=GRID_SIZE):
        self.size = size
        self.total = size * size
        
        # State: Size x Size x 3 (Plus, Minus, Flow)
        # Initialize as Skeptical (High Minus)
        self.psi = np.zeros((size, size, 3))
        self.psi[:, :, 1] = 0.9  # Minus (Red)
        self.psi[:, :, 0] = 0.1  # Plus (Green)
        self.psi[:, :, 2] = 0.1  # Flow (Blue)
        self.normalize()
        
        # Laplacians for diffusion (pre-allocate)
        self.diff_buffer = np.zeros_like(self.psi)

    def normalize(self):
        # Norm across the last axis (channels)
        norms = np.linalg.norm(self.psi, axis=2, keepdims=True)
        self.psi /= (norms + 1e-9)

    def apply_diffusion(self):
        # Simple finite difference spatial diffusion
        # Shift Up, Down, Left, Right
        p = self.psi
        
        # Periodic Boundary Conditions (Toroidal World)
        # N, S, E, W neighbors
        n = np.roll(p, 1, axis=0)
        s = np.roll(p, -1, axis=0)
        e = np.roll(p, 1, axis=1)
        w = np.roll(p, -1, axis=1)
        
        # Laplacian = Neighbors - 4*Center
        laplacian = (n + s + e + w) - 4*p
        
        # Apply strict topological update
        self.psi += COUPLING * laplacian

    def step(self):
        # 1. Internal Dynamics
        # - decay Flow
        self.psi[:, :, 2] *= (1.0 - DECAY)
        
        # - "Reaction": If Plus and Minus collide, they generate Flow
        #   Synthesis Logic: flow += alpha * (plus * minus)
        conflict = self.psi[:, :, 0] * self.psi[:, :, 1]
        self.psi[:, :, 2] += 0.3 * conflict
        
        # 2. Opinion Dynamics (simplified phase logic for speed)
        #   Plus grows if Flow is high (enlightened positivity)
        flow_boost = self.psi[:, :, 2] * 0.05
        self.psi[:, :, 0] += flow_boost
        
        # 3. Spatial Diffusion (The "Social Network")
        self.apply_diffusion()
        
        # 4. Renormalize (The Unity Constraint)
        self.normalize()

    def inject_idea(self, x, y, radius=3, type_idx=0, strength=2.0):
        # Inject a burst of belief at (x,y)
        x, y = int(x), int(y)
        for i in range(-radius, radius+1):
            for j in range(-radius, radius+1):
                if 0 <= x+i < self.size and 0 <= y+j < self.size:
                    dist = np.sqrt(i**2 + j**2)
                    if dist <= radius:
                        self.psi[x+i, y+j, type_idx] += strength
        self.normalize()

# ─── VISUALIZATION ───────────────────────────────────────────────────

# Setup Simulation
print("Initializing Collective Consciousness Grid...")
grid = FluxGrid()
print(f"Populated {grid.total} Neural Minds.")

fig, ax = plt.subplots(figsize=(8, 8))
fig.canvas.manager.set_window_title('Flux Dynamics: Societal Simulator')

# Initial Image
# Mapping: Plus->Green, Minus->Red, Flow->Blue
# We just pass the Psi array directly as RGB! 
# (Since Psi is normalized 0-1 and 3-channels, it maps perfectly to RGB)
im = ax.imshow(grid.psi, origin='lower', interpolation='bilinear')
ax.set_axis_off()

title_text = ax.text(0.5, 1.02, "Click to Inject Truth (Green)", 
                     transform=ax.transAxes, ha="center", fontsize=12, color='black')

# Stats Text
stats_text = ax.text(0.5, -0.05, "", transform=ax.transAxes, ha="center", fontsize=10)

def update(frame):
    grid.step()
    
    # Visualization:
    # To make it look "Sci-Fi", let's boost contrast
    p = grid.psi ** 0.8 # Gamma correction
    
    # CORRECT COLOR MAPPING FOR INTUITION
    # Display buffer: [Red, Green, Blue]
    # We want: 
    #   Red   = Minus (Skepticism/Resistance) -> index 1 in psi
    #   Green = Plus  (Truth/Growth)         -> index 0 in psi
    #   Blue  = Flow  (Synthesis)            -> index 2 in psi
    
    vis_data = np.dstack([p[:,:,1], p[:,:,0], p[:,:,2]])
    
    im.set_data(vis_data)
    
    # Calculate global stats
    avg_plus = np.mean(grid.psi[:,:,0])
    avg_minus = np.mean(grid.psi[:,:,1])
    avg_flow = np.mean(grid.psi[:,:,2])
    
    stats_text.set_text(f"Global Beliefs ->  Invariant(G): {avg_plus:.2f}  |  Skeptic(R): {avg_minus:.2f}  |  Synthesis(B): {avg_flow:.2f}")
    
    return [im, stats_text]

# Interaction
def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        # Left Click: Inject Truth (Plus/Green)
        # Right Click: Inject Confusion (Minus/Red)
        if event.button == 1:
            grid.inject_idea(event.ydata, event.xdata, type_idx=0, strength=5.0) # Green
            title_text.set_text("Injecting Truth Signal...")
        elif event.button == 3:
            grid.inject_idea(event.ydata, event.xdata, type_idx=1, strength=5.0) # Red
            title_text.set_text("Injecting Doubt/Skepticism...")
        elif event.button == 2: # Middle click
            grid.inject_idea(event.ydata, event.xdata, type_idx=2, strength=5.0) # Blue
            title_text.set_text("Injecting Pure Synthesis...")

cid = fig.canvas.mpl_connect('button_press_event', onclick)

print("Starting Animation loop...")

# Force GIF generation for headless environments
print("Rendering simulation to 'flux_society_demo.gif'...")

# Scenario: Drop truth in the middle at frame 10
from matplotlib.animation import PillowWriter
writer = PillowWriter(fps=30)

grid.inject_idea(GRID_SIZE//2, GRID_SIZE//2, radius=4, type_idx=0, strength=10.0) # Big Green Drop

# We need to manually drive the animation for saving since we aren't using plt.show()
# Create the animation object with a fixed number of frames
ani = FuncAnimation(fig, update, frames=100, interval=20, blit=True) 

ani.save("flux_society_demo.gif", writer=writer)
print("GIF Saved.")
