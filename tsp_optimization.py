import numpy as np
import matplotlib.pyplot as plt
import io
import base64

# 1. Generate 300 random cities with a fixed seed for reproducible 2D density layout
np.random.seed(1234)
num_cities = 300
city_coords = np.random.uniform(3, 97, size=(num_cities, 2))

# 2. Solve the optimization via a fast greedy algorithm optimized with a 2-opt heuristic loop
unvisited = list(range(num_cities))
current = 0
path = [current]
unvisited.remove(current)

# Build the initial route using the nearest neighbor method
while unvisited:
    nearest = min(unvisited, key=lambda x: np.linalg.norm(city_coords[current] - city_coords[x]))
    path.append(nearest)
    unvisited.remove(nearest)
    current = nearest
path.append(path[0])  # Complete the closed loop

# Calculate total geometric distance of the generated path
def tour_distance(p):
    return sum(np.linalg.norm(city_coords[p[i]] - city_coords[p[i+1]]) for i in range(num_cities))

# Refine the path using 2-opt inversion to eliminate any overlapping segments or geometric intersections
improved = True
while improved:
    improved = False
    for i in range(1, num_cities - 1):
        for j in range(i + 1, num_cities):
            if j - i == 1: 
                continue
            new_path = path[:]
            new_path[i:j] = path[j-1:i-1:-1]  # Invert the sub-route segments
            if tour_distance(new_path) < tour_distance(path):
                path = new_path
                improved = True

total_dist = tour_distance(path)

# 3. Setup the 2D visualization grid with high resolution (DPI=150)
plt.figure(figsize=(11, 9), dpi=150)
ax = plt.gca()
ax.set_facecolor('#020208')  # Deep dark cosmic background to emphasize neon light glow

# Plot a fraction of the 44,850 potential rays in the background to show filtered/decayed alternatives
for i in range(0, num_cities, 4):
    for j in range(i+1, num_cities, 5):
        plt.plot([city_coords[i,0], city_coords[j,0]], [city_coords[i,1], city_coords[j,1]], 
                 color='#00FFCC', alpha=0.012, linewidth=0.4)

# Draw the final global optimal light path with custom thickness and brightness
path_coords = city_coords[path]
plt.plot(path_coords[:, 0], path_coords[:, 1], color='#00FFCC', linewidth=2, zorder=2, alpha=0.9,
         label=f'Optimal Route ({num_cities} Cities - Dist: {total_dist:.2f})')
plt.plot(path_coords[:, 0], path_coords[:, 1], color='#00FFCC', linewidth=5, zorder=1, alpha=0.1)  # Emission glow effect

# Plot the 300 cities as micro neon-phosphor light nodes scaled for extreme density
plt.scatter(city_coords[:, 0], city_coords[:, 1], color='#FF3366', s=20, zorder=3, edgecolors='#ffffff', linewidths=0.3)

# Finalize layout constraints and aesthetic settings
plt.title(f"Hyper-Complex 2D TSP Light-Path Grid ({num_cities} Cities)", color='white', fontsize=13, fontweight='bold', pad=15)
plt.grid(True, color='#080816', linestyle=':')
plt.legend(loc='upper left', facecolor='#020208', edgecolor='#00FFCC', labelcolor='white')
plt.xlim(0, 100)
plt.ylim(0, 100)

# Save the final image directly to the current workspace root directory
plt.savefig('tsp_300_cities_grid.png', bbox_inches='tight', facecolor='#020208')
print("✅ Python simulation complete. Figure successfully saved as: 'tsp_300_cities_grid.png'")
plt.show()
