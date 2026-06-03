<img width="1382" height="1155" alt="__results___0_1" src="https://github.com/user-attachments/assets/42dc3786-df12-4b8f-828a-588af7e50420" />
# 📍 Neon Light-Path Grid
## *An Optimized 2D Traveling Salesperson Problem (TSP) Solver*

A high-performance Python simulation that solves the Traveling Salesperson Problem (TSP) for 300 randomized cities using a hybrid Nearest Neighbor and 2-opt heuristic algorithm, featuring a stunning neon-phosphor visual grid.

## 🚀 Overview

This project provides an efficient geometric optimization solution for a 300-city TSP deployment. By combining a fast greedy routing approach with an iterative 2-opt inversion loop, the algorithm eliminates path intersections to find a highly optimized global route, rendered in a high-resolution cosmic dark aesthetic.

## 📊 How It Works

1. **Nearest Neighbor Initialization:** Builds the initial route from a fixed seed layout (`1234`) by sequentially connecting the closest unvisited city using Euclidean distance.
2. **2-opt Heuristic Optimization:** Iterates through the generated path, inverting sub-route segments to untangle overlapping lines and minimize the total geometric distance.
3. **Advanced Visualization:** Generates a 150 DPI high-resolution grid plotting a fraction of background alternative rays to visualize the density, topped with a glowing neon optimal light path.

## 🛠️ Requirements

Make sure you have Python installed, then install the required dependencies:

```bash
pip install numpy matplotlib
```

## 💻 Usage

Save the script as `tsp_optimization.py` and run the following command:

```bash
python tsp_optimization.py
```

## 🖼️ Outputs

Upon successful execution, the script will:
- Print a completion message in your terminal.
- Save a high-resolution figure named `tsp_300_cities_grid.png` directly to your root workspace directory.
- Open an interactive window displaying the finalized neon-phosphor light nodes and the optimized global path.
