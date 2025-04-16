# 🚧 *Proving Grounds | Thermo Ops Edition*  
## ♨️ Applying Differential Equations to Heat Flow Problems

## 🔍 Overview
Differential equations are essential for modeling **heat conduction** and understanding how temperature evolves in physical systems. At the heart of this lies the **heat equation**, a PDE that describes the flow of thermal energy in a medium.

---

## 🚀 Scenario
You're a thermal systems engineer working on a **heat shield** for a Mars lander. The spacecraft's outer hull will endure intense friction and temperature gradients during atmospheric entry. You'll need to apply the heat equation to predict temperature distribution in the material over time—and ensure that internal instruments stay safe.

---

## 📝 Problem Tasks

### 🔥 Task 1: Derive the 1D Heat Equation

> **Objective:** Use physical principles to derive the partial differential equation that governs heat flow along a thin, insulated rod.

**Steps:**
- Let u(x, t) be the temperature at point x and time t.
- Use **Fourier’s Law**:  
\[
  q = -k \frac{\partial u}{\partial x}
\]
  where k is the thermal conductivity.
- Apply **conservation of energy** over a slice \Delta x of the rod.
- Use Taylor expansion to approximate temperature changes.

**Final Result:**  
\[
\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}
\]
where \alpha = \frac{k}{\rho c} is thermal diffusivity.

> 💡 **Hint:** Assume no internal heat generation and constant material properties.

---

### 🧮 Task 2: Solve the 1D Heat Equation (Separation of Variables)

> **Objective:** Solve the heat equation with fixed boundary temperatures using the **separation of variables** method.

**Setup:**
- Rod length: L
- Boundary conditions:  
\[
  u(0, t) = 0,\quad u(L, t) = 0
\]
- Initial condition:  
\[
  u(x, 0) = f(x)
\]

**Solution Form:**  
\[
u(x, t) = \sum_{n=1}^{\infty} B_n \sin\left( \frac{n\pi x}{L} \right) e^{-\alpha \left( \frac{n\pi}{L} \right)^2 t}
\]

> 💡 **Hint:** Use **orthogonality** of sine functions to find coefficients B_n via Fourier series.

---

### 🧊 Task 3: Analyze Steady-State vs Transient Behavior

> **Objective:** Understand the difference between **transient** and **steady-state** heat distributions.

**Key Concepts:**
- **Transient:** Time-varying solution before equilibrium.
- **Steady-state:** Long-term behavior as t \to \infty.

> 🔥 **Tip:** In steady-state, \frac{\partial u}{\partial t} = 0, reducing the PDE to an **ODE**:  
> 
> \frac{d^2 u}{dx^2} = 0
>

> 💡 **Hint:** Analyze decay rates of different Fourier modes—higher modes vanish faster.

---

### 🌐 Task 4: Extend to 2D and 3D Domains

> **Objective:** Generalize the 1D heat equation to model 2D plates or 3D blocks.

**Multidimensional Heat Equation:**
\[
\frac{\partial u}{\partial t} = \alpha \nabla^2 u
\]
where  
\[
\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2}
\]

> 💡 **Hint:** For numerical solutions, discretize the domain using **finite difference** or **finite element** methods.

> 🔥 **Tip:** Boundary conditions matter! Dirichlet (fixed temp), Neumann (insulated), and Robin (mixed) affect the evolution.

---

## 📦 Core Deliverables

- **💻 Python Implementation:** A script or notebook that solves the 1D and optionally 2D heat equation using numerical methods (e.g., Finite Difference).
- **📊 Analysis Report:** Explains assumptions, boundary conditions, and includes both analytical and numerical comparisons.
- **🖼️ Visualizations:** Matplotlib or Plotly plots showing temperature distribution over time.

---

## 🏅 Bonus Section

### 🕹️ Interactive Heat Simulator
> Create an interface (e.g., Streamlit or Dash) that lets users tweak parameters like:
- Rod length
- Initial heat distribution
- Boundary conditions
- Time resolution

And watch the simulation live!

---

### 🔄 Nonlinear Heat Flow
> Explore conductivity as a function of temperature:  
\[
\frac{\partial u}{\partial t} = \frac{\partial}{\partial x} \left( k(u) \frac{\partial u}{\partial x} \right)
\]

- Can be solved using **iterative numerical schemes** like Newton-Raphson or implicit FDM.

---

### 🔥 Internal Heat Source
> Add a time-varying heat source Q(x, t):  
\[
\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2} + Q(x, t)
\]

> 💡 **Hint:** Use sinusoidal or pulsed sources to mimic heating coils or spot welders.

---

### 🛰️ Physical Validation
> Compare the simulation to a real-world heat sensor array or thermal imaging data.

---

### 🎥 Presentation Deck
> Create a slide deck or 2-minute narrated video that walks through:
- Derivation
- Real-world scenario
- Code demonstration
- Key takeaways

---

## 🏅 Bonus Deliverables

- **🕹️ Interactive Control Panel App**
- **📈 Plots for Nonlinear vs. Linear Conduction**
- **🔥 Source-Term Simulation Notebook**
- **📡 Side-by-Side Simulation & Sensor Graph**
- **🎥 Project Walkthrough Video or Slide Deck**

---

## 📚 Resources

- **MIT OCW: Heat Equation**  
  https://ocw.mit.edu/courses/mathematics/18-303-linear-partial-differential-equations-fall-2006/lecture-notes/
  
- **Fourier Series Notes**  
  https://tutorial.math.lamar.edu/Classes/DE/FourierSeries.aspx

- **FEniCS PDE Solver**  
  https://fenicsproject.org/

- **SciPy PDE Tools**  
  https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html

---
