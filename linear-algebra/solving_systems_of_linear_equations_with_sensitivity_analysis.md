# 🧩 Solving Systems of Linear Equations with Sensitivity Analysis

## 🔍 Overview
This challenge delves into **linear systems** and how small changes in the system’s coefficients or constants can significantly affect solutions. Participants will learn various methods (e.g., Gaussian elimination, LU factorization) to solve \(Ax = b\), then perform a **sensitivity analysis** to understand the impact of perturbations. By gaining insights into stability and condition numbers, you’ll be able to evaluate the reliability of solutions in practical contexts.

## 🚀 Scenario
Imagine you are an **operations researcher** optimizing supply chain logistics. You have a large system of linear equations representing distribution constraints, inventory levels, and cost parameters. A slight alteration in cost or demand can shift the entire solution strategy. Understanding the **sensitivity** of your linear system—whether small changes lead to drastic solution revisions—can be critical for robust decision-making. By combining efficient solution methods with sensitivity analysis, you can ensure your supply chain remains resilient and cost-effective.

## 📝 Problem Tasks

### ⚙️ Task 1: Fundamentals of Linear System Solving
- **Task Description:** Implement or utilize standard algorithms to solve \(Ax = b\) for various sizes and types of matrices.
  - **Sub-tasks:**
    - 🧮 Use direct methods (Gaussian elimination, LU/Cholesky factorization) and compare them with iterative methods (e.g., Jacobi, Gauss-Seidel).
    - 📏 Distinguish between well-conditioned (non-singular) and ill-conditioned or nearly singular matrices.
    - 🔧 Provide examples in both small-scale (2×2, 3×3) and larger random matrices.

### 🔬 Task 2: Measuring Sensitivity and Condition Numbers
- **Task Description:** Investigate how small perturbations in \(A\) or \(b\) affect the solution \(x\).
  - **Sub-tasks:**
    - 🎚️ Introduce **condition numbers** (\(\kappa(A)\)) and discuss how they quantify sensitivity.
    - 🔎 Experiment with random perturbations in \(A\) or \(b\), observing how \(\Delta x\) changes.
    - 🏷️ Document outcomes for both well-conditioned and ill-conditioned systems.

### 🏗️ Task 3: Practical Scenarios and Applications
- **Task Description:** Apply linear system solving and sensitivity analysis to real or simulated case studies.
  - **Sub-tasks:**
    - 🚚 Formulate a **supply chain** or **network flow** problem, solve it, then alter parameters to see how the solution shifts.
    - 📈 Model a **financial portfolio** optimization scenario, where small changes in asset returns can change the optimal allocation.
    - 🌐 Provide visual or tabular results illustrating the before-and-after solutions in each scenario.

### 🖼️ Task 4: Numerical Stability and Precision
- **Task Description:** Delve into floating-point arithmetic and how it affects the reliability of linear system solutions.
  - **Sub-tasks:**
    - 🖥️ Compare single precision (`float32`) vs. double precision (`float64`) solutions for the same problem.
    - 📊 Observe how rounding errors can accumulate in iterative methods vs. direct methods.
    - 🧩 Summarize best practices for mitigating numerical issues (e.g., pivoting strategies, preconditioning).

## 📦 Deliverables
- **💻 Code Implementation:**
  A Python script or Jupyter Notebook that:
  1. Demonstrates multiple methods of solving linear systems (direct & iterative).  
  2. Includes a procedure to measure and report condition numbers.  
  3. Highlights sensitivity analyses under different perturbation scenarios.

- **📊 Analysis Report:**
  A concise write-up discussing:
  1. The core theory behind solution methods and condition numbers.  
  2. Observations from your experimentation with perturbations and numerical stability.  
  3. Real-world implications of ill-conditioned systems.

- **🖼️ Visualizations:**
  - Plots or tables showing solution changes in response to small parameter tweaks.  
  - Graphical or tabular representations of condition numbers across multiple test matrices.

## 🎁 Bonus Section
1. **🕹️ Interactive Sensitivity Explorer:**
   Build a small dashboard (e.g., Streamlit or Dash) allowing users to adjust parameters in \(A\) and \(b\) and immediately see the new solution.

2. **🚀 Large-Scale Systems:**
   Investigate advanced solvers (e.g., Conjugate Gradient, GMRES) for large sparse matrices, comparing performance and memory usage.

3. **🔄 Mixed-Integer Extensions:**
   Demonstrate how sensitivity insights carry over to **mixed-integer linear programming** (MILP) for discrete resource allocation.

4. **🌐 Domain-Specific Case Studies:**
   Provide deeper dives into specialized industries (e.g., engineering, energy grids) where linear systems and sensitivity analysis are paramount.

5. **🎥 Presentation Materials:**
   Create a short video or slide deck that explains your solution methods, sensitivity results, and real-world applications.

## 🏅 Bonus Section Deliverables
- **🕹️ Interactive Sensitivity Explorer Deliverable:**
  A running app where matrix entries or vector entries can be tweaked, instantly displaying the new solution and metrics (e.g., norm of \(\Delta x\)).

- **🚀 Large-Scale Systems Deliverable:**
  Benchmarks showing the runtime and memory footprint for iterative methods vs. direct factorization on large sparse matrices.

- **🔄 Mixed-Integer Extensions Deliverable:**
  Sample code or notebook applying sensitivity principles to a MILP problem (e.g., small supply chain with discrete capacities).

- **🌐 Domain-Specific Case Studies Deliverable:**
  Detailed write-ups illustrating how your approach aids in real-world industry scenarios, including references to domain literature or data sources.

- **🎥 Presentation Materials Deliverable:**
  A concise recorded presentation or slide deck highlighting your key findings, solution demos, and best practices.

## 📚 Resources

- **🔗 [Systems of Linear Equations (MIT OCW)](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/)**

- **🔗 [LU Decomposition and Pivoting](https://en.wikipedia.org/wiki/LU_decomposition)**

- **🔗 [Condition Number Explanation](https://en.wikipedia.org/wiki/Condition_number)**

- **🔗 [Iterative Methods (CG, GMRES, etc.)](https://en.wikipedia.org/wiki/Iterative_method)**

- **🔗 [Floating-Point Arithmetic Issues](https://docs.python.org/3/tutorial/floatingpoint.html)**

---
