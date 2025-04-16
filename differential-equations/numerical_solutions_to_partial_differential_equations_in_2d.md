# 🧮 *Proving Grounds | GridForce Edition*  
## 🌐 Numerical Solutions to Partial Differential Equations in 2D

## 🔍 Overview
Partial Differential Equations (PDEs) in **two spatial dimensions** model a wide range of physical systems—from **heat conduction** and **fluid flow** to **electromagnetic fields**. While analytic solutions exist for idealized cases, most real-world problems require **numerical methods** like **Finite Difference**, **Finite Volume**, or **Finite Element** techniques.

---

## 🚀 Scenario
You’re part of a research team developing a simulation to model **temperature distribution across a metal plate** subjected to different edge conditions. Your job: build a 2D PDE solver that shows how heat evolves over time. The output will inform decisions about cooling system placement and structural safety.

---

## 📝 Problem Tasks

### 🔢 Task 1: Discretize the 2D Heat Equation

> **Objective:** Start with the 2D heat equation and discretize it using **Finite Difference Method (FDM)**.

**Equation:**
\[
\frac{\partial u}{\partial t} = \alpha \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)
\]

**Steps:**
- Use a uniform grid: (x_i, y_j) \in [0, L_x] \times [0, L_y]
- Discretize space using central differences:
\[
  \frac{\partial^2 u}{\partial x^2} \approx \frac{u_{i+1,j} - 2u_{i,j} + u_{i-1,j}}{\Delta x^2}
\]
- Discretize time using explicit Euler:
\[
  u_{i,j}^{n+1} = u_{i,j}^n + \Delta t \cdot \alpha \left( \text{Laplacian}_{i,j} \right)
\]

> 💡 **Hint:** Use a 2D NumPy array to store grid values for u(x, y, t)

---

### 🧮 Task 2: Implement the Simulation

> **Objective:** Build a function that updates the 2D temperature grid over time.

**Requirements:**
- Create a grid with initial condition u(x, y, 0)
- Apply **Dirichlet boundary conditions** (e.g., fixed temps at edges)
- Evolve the system using a time loop

> 🔥 **Tip:** Ensure your timestep satisfies the **CFL condition** for stability:  
> 
> \Delta t \leq \frac{\Delta x^2 \Delta y^2}{2 \alpha (\Delta x^2 + \Delta y^2)}
>

---

### 🧊 Task 3: Visualize Heat Flow

> **Objective:** Animate the evolution of temperature on the grid.

**Tools:** Use `matplotlib.pyplot.imshow()` or `plotly` heatmaps

**Tasks:**
- Plot snapshots at selected time intervals
- Show animated evolution using `FuncAnimation` or interactive sliders

> 💡 **Hint:** Color gradients help show heat diffusion clearly. Use `coolwarm` or `plasma` colormaps.

---

### 🧩 Task 4: Experiment with Boundary Conditions

> **Objective:** Change edge behavior to simulate different physical setups.

**Variations:**
- **Neumann (insulated):** Set spatial derivatives at edges to zero.
- **Mixed:** Combine Dirichlet on some sides and Neumann on others.

> 🔥 **Tip:** Edge logic gets tricky—wrap boundary conditions in functions for reuse.

---

## 📦 Core Deliverables

- **💻 Python Script / Notebook:** Working 2D solver for the heat equation using FDM.
- **📈 Heatmap Visuals:** Plots of temperature distribution at different time points.
- **📝 Summary Report:** Covers stability criteria, boundary condition handling, and numerical performance.

---

## 🏅 Bonus Section

### ⚙️ Finite Volume Method (FVM)
> Re-implement the solver using the FVM approach for conservation-based systems.  
> 💡 **Hint:** Divide grid into control volumes and balance inflow/outflow.

---

### 🧠 Solve Laplace’s Equation (Steady-State)
> Set \partial u / \partial t = 0 and solve:
\[
\nabla^2 u = 0
\]
- Use **iterative methods**: Jacobi, Gauss-Seidel, or SOR.

---

### 🌪️ Add Internal Heat Sources
> Modify the heat equation to include a source term:
\[
\frac{\partial u}{\partial t} = \alpha \nabla^2 u + Q(x, y)
\]
- Model a **hotspot** or **localized heat injector**

---

### 📐 Irregular Geometries (FEM)
> Extend to complex domains using **FEniCS** or **scikit-fem**.

---

### 🧪 Real-Time Sensor Overlay
> Simulate vs. actual data by overlaying sensor readings on your animated grid.

---

## 🏅 Bonus Deliverables

- **🔄 FVM-Based Solver**
- **🧘 Steady-State Solver with Gauss-Seidel**
- **🔥 Source-Term Variant with Custom Hotspots**
- **📦 FEniCS Implementation (Irregular Domains)**
- **📊 Sensor Overlay Heatmap (Real vs Sim)**

---

## 📚 Resources

- **Finite Difference Methods Tutorial (MIT):**  
  https://math.mit.edu/~gs/18.336/FD_handout.pdf

- **Numerical PDEs with Python:**  
  https://scipy-lectures.org/advanced/finite_differences/

- **FEniCS FEM Library:**  
  https://fenicsproject.org/

- **Matplotlib Animation Tutorial:**  
  https://matplotlib.org/stable/gallery/animation/index.html

---
